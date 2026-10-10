from pathlib import Path
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parent.parent
out = root / '.impeccable/review'
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe', headless=True)
    page = browser.new_page()
    page.goto('http://127.0.0.1:8000')
    page.evaluate('document.fonts.ready')
    page.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager')")
    page.wait_for_function("[...document.querySelectorAll('img')].every(i=>i.complete&&i.naturalWidth>0)")
    page.emulate_media(reduced_motion='reduce')
    for width, height, name in [(1440,1000,'desktop'),(390,844,'mobile')]:
        page.set_viewport_size({'width':width,'height':height})
        page.evaluate("window.scrollTo({top:0,behavior:'instant'})")
        page.screenshot(path=str(out/f'{name}.png'),full_page=True)
        page.locator('.about').screenshot(path=str(out/f'{name}-about.png'),style='.site-header { visibility:hidden; }')
        text = page.locator('.about-media figcaption').inner_text()
        assert 'Momentnur' not in text
        print(name,repr(text))
    browser.close()
