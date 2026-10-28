"""Record demo clips of the live apps with Playwright, then encode with ffmpeg.

Usage: python3 scripts/record_clips.py [slug ...]
Writes public/clips/<slug>.mp4 and <slug>.jpg (poster).
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from playwright.sync_api import Page, sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'public' / 'clips'
VIEWPORT = {'width': 1440, 'height': 900}  # 16:10, matches the clip frame

# Headless video has no pointer; draw one so viewers can follow the clicks.
CURSOR_JS = """
window.addEventListener('DOMContentLoaded', () => {
  const c = document.createElement('div');
  c.style.cssText = 'position:fixed;z-index:2147483647;pointer-events:none;width:18px;height:18px;'
    + 'margin:-9px 0 0 -9px;border:2px solid #fff;background:rgba(224,48,30,.85);'
    + 'box-shadow:0 0 0 1px #000;left:-50px;top:-50px;transition:transform .12s';
  document.body.appendChild(c);
  addEventListener('mousemove', e => { c.style.left = e.clientX + 'px'; c.style.top = e.clientY + 'px'; }, true);
  addEventListener('mousedown', () => { c.style.transform = 'scale(.6)'; }, true);
  addEventListener('mouseup', () => { c.style.transform = 'scale(1)'; }, true);
});
"""


def glide(page: Page, selector: str, steps: int = 25) -> None:
    """Move the mouse to an element in visible steps, then click it."""
    box = page.locator(selector).first.bounding_box()
    page.mouse.move(box['x'] + box['width'] / 2, box['y'] + box['height'] / 2, steps=steps)
    page.wait_for_timeout(250)
    page.locator(selector).first.click()


def scroll_table_left(page: Page) -> None:
    """Bring the table's horizontal scroll back to the name column."""
    page.evaluate(
        """() => {
          let el = document.querySelector('table').parentElement;
          while (el && el.scrollWidth <= el.clientWidth) el = el.parentElement;
          if (el) el.scrollTo({ left: 0, behavior: 'smooth' });
        }"""
    )
    page.wait_for_timeout(700)


def first_rows(page: Page, col: int, n: int = 2) -> list[str]:
    return page.eval_on_selector_all(
        'tbody tr', f'rs => rs.slice(0, {n}).map(r => r.children[{col}].innerText.trim())'
    )


def pct(text: str) -> float:
    try:
        return float(text.replace('%', '').replace('+', ''))
    except ValueError:
        return float('-inf')


def scottstats(page: Page) -> None:
    # AI universe: map, highlights, research.
    page.goto('https://scott-stats.vercel.app/ai/map', wait_until='networkidle')
    page.wait_for_timeout(4000)
    for tab in ['Highlights', 'Research']:
        glide(page, f'a:text-is("{tab}")')
        page.wait_for_load_state('networkidle')
        page.wait_for_timeout(2500)
        page.mouse.wheel(0, 400)
        page.wait_for_timeout(1300)

    # Universes menu: pause on each, then open All.
    glide(page, 'button:has-text("Universes")')
    page.wait_for_timeout(600)
    for href in ['/ai', '/robotics', '/space', '/biotech', '/software', '/crypto']:
        box = page.locator(f'a[href="{href}"]').first.bounding_box()
        page.mouse.move(box['x'] + 30, box['y'] + box['height'] / 2, steps=10)
        page.wait_for_timeout(1000)
    glide(page, 'a[href="/all"]:has-text("All")')
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(1500)
    close = page.locator('button:has-text("×")')
    if close.count():
        close.first.click()

    # Sort by 1D, biggest gainer first, open it.
    one_d = 'th span.cursor-pointer:text-is("1D")'
    glide(page, one_d)
    page.wait_for_timeout(900)
    top, second = first_rows(page, 8)
    if pct(top) < pct(second):
        page.locator(one_d).click()
        page.wait_for_timeout(900)
    scroll_table_left(page)
    glide(page, 'tbody tr:nth-child(1) td:nth-child(5)')
    page.wait_for_timeout(2500)

    # Sort by signal, strongest first, click through a few.
    signal = 'th span.cursor-pointer:has-text("Signal")'
    glide(page, signal)
    page.wait_for_timeout(900)
    if '★' not in first_rows(page, 2, 1)[0]:
        page.locator(signal).first.click()
        page.wait_for_timeout(900)
    for row in (1, 2, 3):
        glide(page, f'tbody tr:nth-child({row}) td:nth-child(5)')
        page.wait_for_timeout(2000)

    # Watchlist the open stock and set an alert at the current price.
    glide(page, 'tbody tr:nth-child(3) input[type=checkbox]')
    page.wait_for_timeout(1000)
    glide(page, 'button:has-text("+ Add Alert")')
    page.wait_for_timeout(3000)


def magicstats(page: Page) -> None:
    page.goto('https://magicthestats.vercel.app/', wait_until='networkidle')
    page.wait_for_timeout(2000)
    glide(page, 'a[href="/?w=12m"]')
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(1800)
    glide(page, 'button:has-text("Collector")')
    page.wait_for_timeout(2200)
    page.mouse.wheel(0, 500)
    page.wait_for_timeout(1500)
    page.mouse.wheel(0, -500)
    page.wait_for_timeout(1000)
    glide(page, 'a[href^="/sets/"]')
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(3000)
    page.mouse.wheel(0, 600)
    page.wait_for_timeout(2500)
    glide(page, 'a[href="/charts"]')
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(3500)


FLOWS = {'scottstats': scottstats, 'magicstats': magicstats}
# Seconds cut from the start: page load and first chart render.
TRIM = {'scottstats': 3.5, 'magicstats': 1.0}


def encode(raw: Path, slug: str) -> None:
    mp4 = OUT / f'{slug}.mp4'
    # Cut the load-in, 1280x800, H.264 for universal playback.
    subprocess.run(
        ['ffmpeg', '-y', '-loglevel', 'error', '-ss', str(TRIM[slug]), '-i', str(raw), '-an',
         '-vf', 'scale=1280:800:flags=lanczos,fps=30', '-c:v', 'libx264', '-preset', 'slow',
         '-crf', '30', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(mp4)],
        check=True,
    )
    subprocess.run(
        ['ffmpeg', '-y', '-loglevel', 'error', '-ss', '1', '-i', str(mp4), '-frames:v', '1',
         '-q:v', '4', str(OUT / f'{slug}.jpg')],
        check=True,
    )


def main(slugs: list[str]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for slug in slugs:
            tmp = Path(tempfile.mkdtemp())
            ctx = browser.new_context(viewport=VIEWPORT, record_video_dir=str(tmp), record_video_size=VIEWPORT)
            ctx.add_init_script(CURSOR_JS)
            page = ctx.new_page()
            FLOWS[slug](page)
            ctx.close()
            encode(next(tmp.glob('*.webm')), slug)
            shutil.rmtree(tmp)
            size = (OUT / f'{slug}.mp4').stat().st_size / 1e6
            print(f'{slug}: {size:.1f} MB')
        browser.close()


if __name__ == '__main__':
    main(sys.argv[1:] or list(FLOWS))
