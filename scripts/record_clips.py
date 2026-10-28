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


def glide(page: Page, selector: str, steps: int = 25) -> None:
    """Move the mouse to an element in visible steps, then click it."""
    box = page.locator(selector).first.bounding_box()
    page.mouse.move(box['x'] + box['width'] / 2, box['y'] + box['height'] / 2, steps=steps)
    page.wait_for_timeout(250)
    page.locator(selector).first.click()


def scottstats(page: Page) -> None:
    page.goto('https://scott-stats.vercel.app/all', wait_until='networkidle')
    page.wait_for_timeout(1500)
    close = page.locator('button:has-text("×")')
    if close.count():
        close.first.click()
    page.wait_for_timeout(1200)
    for name in ['Apple', 'Bitcoin', 'Micron Technology']:
        glide(page, f'td:has-text("{name}")')
        page.wait_for_timeout(2200)
    glide(page, 'button:has-text("3m")')
    page.wait_for_timeout(2200)
    glide(page, 'button:has-text("1yr")')
    page.wait_for_timeout(1500)
    page.locator('input[placeholder="Search..."]').click()
    page.keyboard.type('nvda', delay=140)
    page.wait_for_timeout(1500)
    glide(page, 'td:has-text("Nvidia")')
    page.wait_for_timeout(2500)


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
