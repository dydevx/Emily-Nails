from pathlib import Path
from playwright.sync_api import sync_playwright
import re, json

root = Path(__file__).resolve().parent.parent
old = (root / '.impeccable/backup-magazine/index.html').read_text(encoding='utf-8')
new = (root / 'index.html').read_text(encoding='utf-8')
def prices(html):
    return re.findall(r'<span class="price-label">(.*?)</span>\s*<span class="price-value">(.*?)</span>', html, re.S)
assert prices(old) == prices(new) and len(prices(new)) == 19
def nav(html):
    return re.search(r'<nav class="main-nav".*?</nav>', html, re.S).group()
assert nav(old) == nav(new)
assert re.search(r'<footer.*?</footer>', old, re.S).group() == re.search(r'<footer.*?</footer>', new, re.S).group()
report = {'pricesPreserved': 19, 'navigationAndFooterPreserved': True, 'viewports': [], 'errors': []}
review = root / '.impeccable/review/layout'
review.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe', headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 1000})
    page.on('pageerror', lambda e: report['errors'].append(str(e)))
    assert page.goto('http://127.0.0.1:8000').status == 200
    page.evaluate('document.fonts.ready')
    page.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager')")
    page.wait_for_function("[...document.querySelectorAll('img')].every(i=>i.complete&&i.naturalWidth>0)")
    page.wait_for_timeout(1200)
    for width, height, name in [(1440,1000,'desktop'),(390,844,'mobile'),(320,740,None),(768,1024,None),(1024,768,None),(1280,800,None),(700,900,None)]:
        page.set_viewport_size({'width':width,'height':height})
        page.evaluate("window.scrollTo({top:0,behavior:'instant'})")
        data = page.evaluate('''()=>({width:innerWidth, scrollWidth:document.documentElement.scrollWidth,
          ctaBottom:document.querySelector('.hero-actions .btn').getBoundingClientRect().bottom,
          heroLines:Math.round((document.querySelector('h1').getBoundingClientRect().height-parseFloat(getComputedStyle(document.querySelector('h1')).paddingTop)-parseFloat(getComputedStyle(document.querySelector('h1')).paddingBottom))/parseFloat(getComputedStyle(document.querySelector('h1')).lineHeight)),
          overflow:[...document.querySelectorAll('main *')].filter(e=>e.getBoundingClientRect().right>innerWidth+1).map(e=>e.className).slice(0,6)})''')
        report['viewports'].append(data)
        assert data['width'] == data['scrollWidth'], data
        assert not data['overflow'], data
        assert data['heroLines'] == 2, data
        assert data['ctaBottom'] < height, data
        if name:
            page.screenshot(path=str(review/f'{name}.png'),full_page=True)
            page.screenshot(path=str(review/f'{name}-hero.png'))
            for selector, suffix in [('.services','services'),('.about','about'),('.pricing','pricing'),('.gallery','gallery'),('.contact','contact')]:
                page.locator(selector).screenshot(path=str(review/f'{name}-{suffix}.png'),style='.site-header, .skip-link { visibility: hidden; }')
            page.evaluate("window.scrollTo({top:0,behavior:'instant'})")
    page.set_viewport_size({'width':1440,'height':1000})
    page.locator('[data-service-select="3"]').click()
    assert page.locator('[data-service-panel="3"]').is_visible()
    page.locator('[data-service-select="0"]').click()
    page.set_viewport_size({'width':390,'height':844})
    for i in range(6):
        page.locator(f'[data-service-select="{i}"]').click()
        assert page.locator(f'[data-service-select="{i}"]').get_attribute('aria-pressed') == 'true'
        assert page.locator('.service-select[aria-pressed="true"]').count() == 1
        assert page.locator('.service-preview').is_hidden()
        assert page.locator('.service-image:visible').count() == 1
        assert page.locator(f'[data-service="{i}"] .service-image').is_visible()
    page.locator('[data-service-select="0"]').focus()
    page.keyboard.press('Enter')
    assert page.locator('[data-service="0"] .service-image').is_visible()
    page.locator('[data-service-select="1"]').focus()
    page.keyboard.press('Space')
    assert page.locator('[data-service="1"] .service-image').is_visible()
    page.locator('.nav-toggle').click()
    assert page.locator('.nav-toggle').get_attribute('aria-expanded') == 'true'
    page.keyboard.press('Escape')
    assert page.locator('.nav-toggle').get_attribute('aria-expanded') == 'false'
    page.locator('.nav-toggle').click()
    page.locator('.main-nav a[href="#preise"]').click()
    assert page.locator('.nav-toggle').get_attribute('aria-expanded') == 'false'
    for category in page.locator('.price-category').all():
        assert category.evaluate('(d)=>d.open')
        category.locator('summary').click()
        assert not category.evaluate('(d)=>d.open')
        category.locator('summary').click()
        assert category.evaluate('(d)=>d.open')
    page.locator('[data-menu-open]').click()
    assert page.locator('.menu-dialog').evaluate('(d)=>d.open')
    page.keyboard.press('Escape')
    assert not page.locator('.menu-dialog').evaluate('(d)=>d.open')
    assert page.locator('[data-menu-open]').evaluate('(a)=>a===document.activeElement')
    page.locator('.video-play').click()
    page.wait_for_function("document.querySelector('video').currentTime>0")
    assert page.locator('.video-play').is_hidden()
    page.locator('video').evaluate('(v)=>v.pause()')
    missing=page.evaluate("[...document.querySelectorAll('a[href^=\"#\"]')].filter(a=>!document.querySelector(a.hash)).map(a=>a.hash)")
    assert not missing
    page.emulate_media(reduced_motion='reduce')
    assert page.locator('h1').evaluate('(e)=>getComputedStyle(e).animationName') == 'none'
    assert page.locator('.hero-media').evaluate('(e)=>getComputedStyle(e).animationName') == 'none'
    context = browser.new_context(java_script_enabled=False, viewport={'width':390,'height':844})
    fallback = context.new_page()
    fallback.goto('http://127.0.0.1:8000')
    assert fallback.locator('.main-nav').is_visible()
    assert fallback.locator('.service-image:visible').count() == 6
    assert fallback.locator('.service-preview').is_hidden()
    fallback.locator('.price-category summary').first.click()
    assert not fallback.locator('.price-category').first.evaluate('(d)=>d.open')
    report['interactions'] = 'six service selections, Enter/Space, mobile navigation/Escape, all disclosures, menu dialog/focus restoration, video, reduced motion, no-JS fallback: passed'
    assert not report['errors']
    browser.close()
(review/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=True,indent=2))
