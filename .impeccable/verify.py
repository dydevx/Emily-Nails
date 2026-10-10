from pathlib import Path
from playwright.sync_api import sync_playwright
import re, json
root = Path(__file__).resolve().parent.parent
old = (root / '.impeccable/backup/index.html').read_text(encoding='utf-8')
new = (root / 'index.html').read_text(encoding='utf-8')
def prices(html):
    return re.findall(r'<span class="price-label">(.*?)</span>\s*(?:<span class="price-dots".*?</span>\s*)?<span class="price-value">(.*?)</span>', html, re.S)
assert prices(old) == prices(new), 'Published prices changed'
assert len(prices(new)) == 19
old_nav = re.search(r'<nav class="main-nav".*?</nav>', old, re.S).group()
assert re.findall(r'<a href="(.*?)">(.*?)</a>', old_nav) == re.findall(r'<a href="(.*?)">(.*?)</a>', re.search(r'<nav class="main-nav".*?</nav>',new,re.S).group())
def footer_text(html):
    footer = re.search(r'<footer class="site-footer">.*?</footer>',html,re.S).group()
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', footer)).strip()
assert footer_text(old) == footer_text(new), 'Footer information changed'
results = {'pricesPreserved':len(prices(new)), 'navigationPreserved':True,'footerPreserved':True,'viewports':[], 'errors':[]}
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',headless=True)
    page = browser.new_page(viewport={'width':1440,'height':1000})
    page.on('pageerror',lambda error:results['errors'].append(str(error)))
    response=page.goto('http://127.0.0.1:8000')
    assert response.status == 200
    page.evaluate('document.fonts.ready')
    page.wait_for_function("document.querySelector('.hero-media img').complete && document.querySelector('.hero-media img').naturalWidth > 0")
    page.wait_for_timeout(1100)
    for width,height,name in [(1440,1000,'desktop'),(390,844,'mobile'),(320,740,None),(768,1024,None),(1024,768,None)]:
        page.set_viewport_size({'width':width,'height':height})
        page.evaluate("window.scrollTo({top:0,behavior:'instant'})")
        page.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager')")
        page.wait_for_function("[...document.querySelectorAll('main img')].every(i=>i.complete && i.naturalWidth>0)")
        page.wait_for_timeout(120)
        sizes=page.evaluate('''()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,heroLines:Math.round(document.querySelector('h1').getBoundingClientRect().height/parseFloat(getComputedStyle(document.querySelector('h1')).lineHeight)),ctaBottom:document.querySelector('.hero-actions').getBoundingClientRect().bottom,images:[...document.querySelectorAll('main img')].map(i=>({src:i.getAttribute('src'),loaded:i.complete&&i.naturalWidth>0}))})''')
        assert sizes['width'] == sizes['scrollWidth'], f'Horizontal overflow at {width}'
        assert sizes['heroLines'] == 2, f'Heading wraps at {width}: {sizes}'
        assert sizes['ctaBottom'] < height, f'Hero action outside viewport at {width}'
        assert all(i['loaded'] for i in sizes['images']), f'Missing image at {width}'
        assert page.locator('.inspiration-grid img').evaluate_all('(images)=>images.every(i=>i.getBoundingClientRect().height <= i.getBoundingClientRect().width*1.6)'), f'Gallery images too tall at {width}'
        results['viewports'].append(sizes)
        if name:
            page.screenshot(path=str(root / f'.impeccable/review/{name}.png'),full_page=True)
            page.screenshot(path=str(root / f'.impeccable/review/{name}-hero.png'))
            page.locator('.services').screenshot(path=str(root / f'.impeccable/review/{name}-services.png'),style='.site-header, .skip-link { visibility: hidden; }')
            page.locator('.social').screenshot(path=str(root / f'.impeccable/review/{name}-social.png'))
            page.evaluate("window.scrollTo({top:0,behavior:'instant'})")
    page.set_viewport_size({'width':390,'height':844})
    page.locator('.nav-toggle').click()
    assert page.locator('.nav-toggle').get_attribute('aria-expanded') == 'true'
    page.keyboard.press('Escape')
    assert page.locator('.nav-toggle').get_attribute('aria-expanded') == 'false'
    page.locator('.nav-toggle').click()
    page.locator('.main-nav a[href="#preise"]').click()
    assert page.locator('.nav-toggle').get_attribute('aria-expanded') == 'false'
    for category in page.locator('.price-category').all():
        category.locator('summary').click()
        assert category.evaluate('(d)=>d.open') != (category.locator('summary').inner_text().startswith('Nagelpflege'))
        category.locator('summary').click()
    page.locator('[data-menu-open]').click()
    assert page.locator('.menu-dialog').evaluate('(d)=>d.open')
    page.keyboard.press('Escape')
    assert not page.locator('.menu-dialog').evaluate('(d)=>d.open')
    assert page.locator('[data-menu-open]').evaluate('(a)=>a===document.activeElement')
    page.locator('.video-play').click()
    page.wait_for_function("document.querySelector('video').currentTime > 0")
    assert page.locator('.video-play').is_hidden()
    page.locator('video').evaluate('(v)=>v.pause()')
    assert not results['errors'],results['errors']
    missing=page.evaluate("[...document.querySelectorAll('a[href^=\"#\"]')].filter(a=>!document.querySelector(a.hash)).map(a=>a.hash)")
    assert not missing,missing
    results['interactions']='mobile menu, Escape, anchor navigation, all price disclosures, image dialog/focus return, video playback: passed'
    assert page.locator('.social-links a svg').count() == 3
    assert page.locator('.footer-socials a svg').count() == 3
    results['socialIcons']='three local Tabler brand SVGs in social section and footer'
    assert page.locator('.service-image img').count() == 6
    assert page.locator('.inspiration-grid img').count() == 4
    results['imagery']='six new AI images plus existing hero; service images and four-image inspiration collection'
    page.emulate_media(reduced_motion='reduce')
    assert page.locator('.hero-copy').evaluate('(e)=>getComputedStyle(e).animationName') == 'none'
    results['reducedMotion']=True
    context=browser.new_context(java_script_enabled=False,viewport={'width':390,'height':844})
    fallback=context.new_page()
    fallback.goto('http://127.0.0.1:8000')
    assert fallback.locator('.main-nav').is_visible()
    fallback.locator('.price-category summary').first.click()
    assert fallback.locator('.price-category').first.evaluate('(d)=>d.open')
    results['noJavaScriptFallback']=True
    browser.close()
(root/'.impeccable/review/verification.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(results,ensure_ascii=True,indent=2))
