"""Build a demo clip from still screenshots.

Each screenshot sits on a dark backdrop as a card. A gentle camera eases
between framings, and key regions pop out under a magnifier while the rest of
the frame dims. Captions slide in as a lower third.

Usage: python3 scripts/stills_clip.py fomo-wallet-surfacer
Reads clip-src/<slug>/*.png, writes public/clips/<slug>.mp4 and <slug>.jpg.
"""
import math
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
W, H, FPS = 1920, 1200, 30
MARGIN = 90
ACCENT = (139, 92, 246)  # fomo violet
FONT = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf', 30)
FONT_SMALL = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 22)


# --- easing -----------------------------------------------------------------

def clamp01(t: float) -> float:
    return max(0.0, min(1.0, t))


def smooth(t: float) -> float:
    t = clamp01(t)
    return t * t * (3 - 2 * t)


def out_back(t: float) -> float:
    t = clamp01(t)
    c = 1.4
    return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2


# --- shot plan --------------------------------------------------------------
# Camera keyframes are (time, (focus_x, focus_y, zoom)) in image pixels; zoom 1 = whole image fits.
# Magnifiers are (t_on, t_off, (x0, y0, x1, y1), scale_vs_source).

def plan(src: Path) -> list[dict]:
    holders = Image.open(src / 'token-holders.png').convert('RGB')
    traders = Image.open(src / 'top-traders.png').convert('RGB')
    profile = Image.open(src / 'profile.png').convert('RGB')

    def whole(img):
        return (img.width / 2, img.height / 2, 1.0)

    return [
        {
            'img': holders, 'dur': 10.0,
            'keys': [(0, whole(holders)), (1.4, whole(holders)), (3.4, (742, 1430, 1.6)), (10, (742, 1430, 1.6))],
            'mags': [(4.0, 6.4, (45, 1362, 330, 1440), 2.0), (6.7, 9.3, (45, 1462, 300, 1542), 2.0)],
            'captions': [(0.3, '01', 'PONS · TOKEN PAGE'), (3.0, '02', 'HOLDERS · ONE-CLICK WALLET COPY')],
        },
        {
            'img': traders, 'dur': 8.6,
            'keys': [(0, whole(traders)), (1.2, whole(traders)), (3.0, (335, 175, 1.3)), (8.6, (335, 175, 1.3))],
            'mags': [(3.3, 4.9, (75, 30, 352, 105), 2.0), (5.1, 6.7, (75, 128, 432, 208), 2.0),
                     (6.9, 8.4, (75, 228, 414, 308), 2.0)],
            'captions': [(0.3, '03', 'TOP TRADERS'), (2.8, '03', 'SOLANA + EVM WALLETS LINKED')],
        },
        {
            'img': profile, 'dur': 7.6,
            'keys': [(0, whole(profile)), (1.2, whole(profile)), (2.9, (560, 560, 1.2)), (7.6, (560, 560, 1.2))],
            'mags': [(3.3, 7.4, (18, 610, 548, 664), 2.3)],
            'captions': [(0.3, '04', 'TRADER PROFILE'), (2.8, '04', 'LINKED WALLETS · COPY EITHER')],
        },
    ]


# --- drawing helpers ----------------------------------------------------------

def backdrop() -> Image.Image:
    bg = Image.new('RGB', (W, H))
    px = ImageDraw.Draw(bg)
    for y in range(H):
        k = y / H
        px.line([(0, y), (W, y)], fill=(int(11 - 5 * k), int(10 - 5 * k), int(20 - 8 * k)))
    glow = Image.new('L', (W // 4, H // 4), 0)
    ImageDraw.Draw(glow).ellipse([W // 16, H // 20, W // 4 - W // 16, H // 4 - H // 20], fill=70)
    glow = glow.filter(ImageFilter.GaussianBlur(40)).resize((W, H), Image.BILINEAR)
    bg = Image.composite(Image.new('RGB', (W, H), (38, 24, 74)), bg, glow)
    dots = ImageDraw.Draw(bg)
    for y in range(16, H, 32):
        for x in range(16, W, 32):
            dots.point((x, y), fill=(34, 34, 48))
    return bg


def rounded_mask(size: tuple[int, int], r: int) -> Image.Image:
    m = Image.new('L', size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, size[0] - 1, size[1] - 1], r, fill=255)
    return m


def shadow_under(frame: Image.Image, box: tuple[int, int, int, int], blur: int, strength: int, dy: int) -> None:
    """Soft drop shadow under box, drawn at quarter scale for speed."""
    q = 4
    sh = Image.new('L', (W // q, H // q), 0)
    x0, y0, x1, y1 = box
    ImageDraw.Draw(sh).rounded_rectangle([x0 / q, (y0 + dy) / q, x1 / q, (y1 + dy) / q], 4, fill=strength)
    sh = sh.filter(ImageFilter.GaussianBlur(blur / q)).resize((W, H), Image.BILINEAR)
    frame.paste(Image.new('RGB', (W, H), (0, 0, 0)), (0, 0), sh)


def camera_at(keys: list, t: float) -> tuple[float, float, float]:
    for (t0, c0), (t1, c1) in zip(keys, keys[1:]):
        if t <= t1:
            k = smooth((t - t0) / (t1 - t0)) if t1 > t0 else 1
            return tuple(a + (b - a) * k for a, b in zip(c0, c1))
    return keys[-1][1]


def layout(img: Image.Image, cam: tuple[float, float, float]) -> tuple[float, float, float]:
    """Card scale and top-left position for a camera."""
    fx, fy, zoom = cam
    s = min((W - 2 * MARGIN) / img.width, (H - 2 * MARGIN) / img.height) * zoom
    cw, ch = img.width * s, img.height * s

    def place(size, canvas, focus):
        if size <= canvas - 2 * MARGIN:
            return (canvas - size) / 2
        return max(canvas - MARGIN - size, min(MARGIN, canvas / 2 - focus * s))

    return s, place(cw, W, fx), place(ch, H, fy)


def caption(frame: Image.Image, shot: dict, t: float) -> None:
    live = [(t_on, n, text) for t_on, n, text in shot['captions'] if t >= t_on]
    if not live:
        return
    t_on, num, text = live[-1]
    k = smooth((t - t_on) / 0.4)
    d = ImageDraw.Draw(frame, 'RGBA')
    tw = d.textlength(text, font=FONT)
    x = 60 - (1 - k) * 40
    y = H - 118
    d.rectangle([x, y, x + tw + 150, y + 64], fill=(8, 8, 12, int(225 * k)))
    d.rectangle([x, y, x + 6, y + 64], fill=ACCENT + (int(255 * k),))
    d.text((x + 28, y + 20), num, font=FONT_SMALL, fill=(150, 130, 220, int(255 * k)))
    d.text((x + 80, y + 15), text, font=FONT, fill=(232, 232, 236, int(255 * k)))


def magnify(frame: Image.Image, img: Image.Image, mag: tuple, s: float, ox: float, oy: float, t: float) -> Image.Image:
    t_on, t_off, (bx0, by0, bx1, by1), target = mag
    if t < t_on or t > t_off:
        return frame
    p_in = out_back((t - t_on) / 0.5)
    p_out = 1 - smooth((t - (t_off - 0.35)) / 0.35)
    p = min(p_in, p_out)
    fade = clamp01(min((t - t_on) / 0.3, (t_off - t) / 0.3))

    # Dim and soften everything behind the lens.
    behind = frame.filter(ImageFilter.GaussianBlur(5))
    behind = Image.blend(behind, Image.new('RGB', (W, H), (4, 4, 8)), 0.45)
    frame = Image.blend(frame, behind, 0.85 * fade)

    pad = 12
    region = img.crop((max(0, bx0 - pad), max(0, by0 - pad), min(img.width, bx1 + pad), min(img.height, by1 + pad)))
    scale = s + (target - s) * p
    pw, ph = max(1, round(region.width * scale)), max(1, round(region.height * scale))
    cx = ox + (bx0 + bx1) / 2 * s
    cy = oy + (by0 + by1) / 2 * s
    x0 = int(min(max(cx - pw / 2, 40), W - 40 - pw))
    y0 = int(min(max(cy - ph / 2, 40), H - 160 - ph))

    shadow_under(frame, (x0, y0, x0 + pw, y0 + ph), blur=48, strength=int(200 * fade), dy=22)
    lens = region.resize((pw, ph), Image.LANCZOS)
    frame.paste(lens, (x0, y0), rounded_mask((pw, ph), 14))
    d = ImageDraw.Draw(frame, 'RGBA')
    d.rounded_rectangle([x0 - 1, y0 - 1, x0 + pw, y0 + ph], 14, outline=ACCENT + (int(230 * fade),), width=3)
    d.rounded_rectangle([x0 - 7, y0 - 7, x0 + pw + 6, y0 + ph + 6], 18, outline=ACCENT + (int(60 * fade),), width=4)
    return frame


def render(shot: dict, t: float, bg: Image.Image) -> Image.Image:
    img = shot['img']
    s, ox, oy = layout(img, camera_at(shot['keys'], t))
    cw, ch = round(img.width * s), round(img.height * s)
    frame = bg.copy()
    box = (int(ox), int(oy), int(ox) + cw, int(oy) + ch)
    shadow_under(frame, box, blur=60, strength=170, dy=30)
    frame.paste(img.resize((cw, ch), Image.LANCZOS), box[:2], rounded_mask((cw, ch), 12))
    ImageDraw.Draw(frame, 'RGBA').rounded_rectangle(
        [box[0] - 1, box[1] - 1, box[2], box[3]], 12, outline=(255, 255, 255, 28), width=1)
    for mag in shot['mags']:
        frame = magnify(frame, img, mag, s, ox, oy, t)
    caption(frame, shot, t)
    return frame


def main(slug: str) -> None:
    src = ROOT / 'clip-src' / slug
    out = ROOT / 'public' / 'clips' / f'{slug}.mp4'
    shots = plan(src)
    bg = backdrop()
    xfade = 0.6
    ff = subprocess.Popen(
        ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
         '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-tune', 'animation',
         '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(out)],
        stdin=subprocess.PIPE,
    )
    for i, shot in enumerate(shots):
        for f in range(int(shot['dur'] * FPS)):
            t = f / FPS
            frame = render(shot, t, bg)
            if i + 1 < len(shots) and t > shot['dur'] - xfade:
                k = smooth((t - (shot['dur'] - xfade)) / xfade)
                frame = Image.blend(frame, render(shots[i + 1], 0, bg), k)
            ff.stdin.write(frame.tobytes())
    ff.stdin.close()
    ff.wait()
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', '4.6', '-i', str(out), '-frames:v', '1',
                    '-q:v', '2', str(out.with_suffix('.jpg'))], check=True)
    print(f'{slug}: {out.stat().st_size / 1e6:.1f} MB')


if __name__ == '__main__':
    main(sys.argv[1])
