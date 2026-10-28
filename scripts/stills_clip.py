"""Build a demo clip from still screenshots: eased pans/zooms, highlight boxes, captions.

Usage: python3 scripts/stills_clip.py fomo-wallet-surfacer
Reads clip-src/<slug>/*.png, writes public/clips/<slug>.mp4 and <slug>.jpg.
"""
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
W, H, FPS = 1600, 1000, 30
ASPECT = W / H
BG = (12, 12, 18)
HILITE = (224, 48, 30)
FONT = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf', 26)


def ease(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def fit(img: Image.Image) -> tuple[float, float, float]:
    """Camera (cx, cy, width) that shows the whole image."""
    w = max(img.width, img.height * ASPECT)
    return img.width / 2, img.height / 2, w


# Each shot: image, list of (time, camera) keyframes, highlights (t_on, box), caption.
# Cameras are (cx, cy, width) in image pixels; height follows the 16:10 aspect.
def shots(src: Path) -> list[dict]:
    holders = Image.open(src / 'token-holders.png').convert('RGB')
    traders = Image.open(src / 'top-traders.png').convert('RGB')
    profile = Image.open(src / 'profile.png').convert('RGB')
    return [
        {
            'img': holders, 'dur': 9.0,
            'keys': [(0, fit(holders)), (1.5, fit(holders)), (3.5, (625, 1180, 1260)),
                     (4.5, (625, 1180, 1260)), (6.5, (235, 1105, 480)), (9.0, (235, 1105, 480))],
            'boxes': [(7.0, (122, 1056, 150, 1083)), (7.8, (108, 1120, 136, 1147))],
            'captions': [(0.3, 'PONS · TOKEN PAGE'), (3.5, 'HOLDERS'), (6.8, 'COPY WALLET ADDRESS')],
        },
        {
            'img': traders, 'dur': 8.0,
            'keys': [(0, fit(traders)), (1.2, fit(traders)), (3.2, (176, 100, 360)), (8.0, (176, 100, 360))],
            'boxes': [(3.6, (148, 13, 192, 38)), (4.3, (172, 75, 216, 99)), (5.0, (152, 139, 196, 163))],
            'captions': [(0.3, 'TOP TRADERS'), (3.4, 'SOLANA + EVM WALLETS LINKED')],
        },
        {
            'img': profile, 'dur': 7.5,
            'keys': [(0, fit(profile)), (1.2, fit(profile)), (3.2, (124, 264, 270)), (7.5, (124, 264, 270))],
            'boxes': [(3.6, (2, 258, 107, 283)), (4.3, (118, 258, 240, 283))],
            'captions': [(0.3, 'TRADER PROFILE'), (3.4, 'LINKED WALLETS')],
        },
    ]


def camera_at(keys: list, t: float) -> tuple[float, float, float]:
    for (t0, c0), (t1, c1) in zip(keys, keys[1:]):
        if t <= t1:
            k = ease((t - t0) / (t1 - t0)) if t1 > t0 else 1
            return tuple(a + (b - a) * k for a, b in zip(c0, c1))
    return keys[-1][1]


def render(shot: dict, t: float) -> Image.Image:
    img = shot['img']
    cx, cy, cw = camera_at(shot['keys'], t)
    ch = cw / ASPECT
    x0, y0 = cx - cw / 2, cy - ch / 2
    scale = W / cw
    frame = Image.new('RGB', (W, H), BG)
    # Paste only the part of the image inside the camera, so out-of-bounds stays BG.
    ix0, iy0 = max(0, int(x0)), max(0, int(y0))
    ix1, iy1 = min(img.width, int(x0 + cw) + 1), min(img.height, int(y0 + ch) + 1)
    if ix1 > ix0 and iy1 > iy0:
        part = img.crop((ix0, iy0, ix1, iy1))
        pw, ph = round((ix1 - ix0) * scale), round((iy1 - iy0) * scale)
        frame.paste(part.resize((pw, ph), Image.LANCZOS), (round((ix0 - x0) * scale), round((iy0 - y0) * scale)))
    d = ImageDraw.Draw(frame)
    for t_on, (bx0, by0, bx1, by1) in shot['boxes']:
        if t >= t_on:
            pad = 4
            d.rectangle(
                [(bx0 - x0) * scale - pad, (by0 - y0) * scale - pad, (bx1 - x0) * scale + pad, (by1 - y0) * scale + pad],
                outline=HILITE, width=4,
            )
    caption = [c for t_on, c in shot['captions'] if t >= t_on]
    if caption:
        text = caption[-1]
        tw = d.textlength(text, font=FONT)
        d.rectangle([0, H - 64, tw + 56, H], fill=(10, 10, 10))
        d.rectangle([24, H - 38, 34, H - 28], fill=HILITE)
        d.text((46, H - 48), text, font=FONT, fill=(214, 214, 208))
    return frame


def main(slug: str) -> None:
    src = ROOT / 'clip-src' / slug
    out = ROOT / 'public' / 'clips' / f'{slug}.mp4'
    plan = shots(src)
    xfade = 0.5
    ff = subprocess.Popen(
        ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
         '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-preset', 'slow', '-crf', '20',
         '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(out)],
        stdin=subprocess.PIPE,
    )
    for i, shot in enumerate(plan):
        n = int(shot['dur'] * FPS)
        for f in range(n):
            t = f / FPS
            frame = render(shot, t)
            # Crossfade the tail of this shot into the head of the next.
            if i + 1 < len(plan) and t > shot['dur'] - xfade:
                k = (t - (shot['dur'] - xfade)) / xfade
                frame = Image.blend(frame, render(plan[i + 1], 0), k)
            ff.stdin.write(frame.tobytes())
    ff.stdin.close()
    ff.wait()
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', '0.5', '-i', str(out), '-frames:v', '1',
                    '-q:v', '3', str(out.with_suffix('.jpg'))], check=True)
    print(f'{slug}: {out.stat().st_size / 1e6:.1f} MB')


if __name__ == '__main__':
    main(sys.argv[1])
