"""Export /resume/ to PDF (print styles, US Letter).

Needs the dev server on :4321 (npx astro dev --port 4321) and Python Playwright.
Writes public/Scott-Neil-Resume.pdf (served for the Download link). If a sibling
../JobSearch/resume/ folder exists, also copies it there. Re-run after every resume change.
Setup: npm install; pip install playwright; python3 -m playwright install chromium.
"""
import re
import shutil
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'public' / 'Scott-Neil-Resume.pdf'
COPY = ROOT.parent / 'JobSearch' / 'resume' / 'Scott-Neil-Resume.pdf'

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('http://localhost:4321/resume/')
    page.wait_for_load_state('networkidle')
    page.emulate_media(media='print')
    page.pdf(path=str(OUT), format='Letter', print_background=True)
    browser.close()

if COPY.parent.is_dir():
    shutil.copyfile(OUT, COPY)
    print(f'copied to {COPY}')
data = OUT.read_bytes()
pages = len(re.findall(rb'/Type\s*/Page[^s]', data))
links = [u.decode() for u in re.findall(rb'/URI\s*\(([^)]*)\)', data)]
print(f'{OUT.relative_to(ROOT)}: {pages} page(s), links: {links}')
if pages != 1:
    raise SystemExit('resume PDF is not 1 page')
