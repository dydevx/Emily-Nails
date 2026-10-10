from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
path = root / 'index.html'
html = path.read_text(encoding='utf-8')
hero = '''      <section class="hero" aria-labelledby="hero-title">
        <div class="container hero-grid">
          <div class="hero-copy">
            <h1 id="hero-title">Schöne Nägel.<br /><span>Schöne Momente.</span></h1>
            <div class="hero-bottom">
              <p>Professionelle Nagelpflege, modernes Nageldesign und entspannende Pediküre im Herzen von Goch.</p>
              <div class="hero-actions"><a class="btn btn-primary" href="#kontakt">Termin anfragen <span class="link-arrow" aria-hidden="true"></span></a><a class="text-link" href="#preise">Preisliste ansehen <span class="link-arrow" aria-hidden="true"></span></a></div>
            </div>
          </div>
          <div class="hero-media">
            <img src="assets/hero-manicure.webp" alt="" width="1024" height="1280" fetchpriority="high" />
          </div>
        </div>
      </section>'''
html = re.sub(r'      <section class="hero".*?</section>', lambda _: hero, html, count=1, flags=re.S)

services = [
    ('Maniküre', 'Professionelle Pflege für schöne und gepflegte Hände.', 'hero-manicure'),
    ('Pediküre', 'Entspannende Fußpflege für ein gepflegtes und frisches Gefühl.', 'pedicure-care'),
    ('Acryl-System', 'Stabile und elegante Nagelmodellage für individuelle Looks.', 'french-manicure'),
    ('UV-Gel-System', 'Natürlich wirkende, langlebige und individuell gestaltete Nägel.', 'babyboomer-nails'),
    ('Nageldesign', 'French, Babyboomer, Glitzer, Farbverlauf und viele weitere Designs.', 'gold-nail-art'),
    ('Shellac', 'Langanhaltender Glanz und intensive Farben für Hände und Füße.', 'shellac-rose')
]
items = '\n'.join(f'''              <article class="service-item" data-service="{i}">
                <h3><button class="service-select" type="button" aria-controls="service-preview" aria-pressed="{'true' if i == 0 else 'false'}" data-service-select="{i}"><span>{name}</span><span class="link-arrow" aria-hidden="true"></span></button></h3>
                <p>{description}</p>
                <div class="service-image"><img src="assets/{image}.webp" alt="" width="1024" height="1280" loading="lazy" /></div>
              </article>''' for i, (name, description, image) in enumerate(services))
previews = '\n'.join(f'''              <figure class="service-preview-panel" data-service-panel="{i}" {'hidden' if i else ''}><img src="assets/{image}.webp" alt="" width="1024" height="1280" loading="lazy" /><figcaption>{name}</figcaption></figure>''' for i, (name, _, image) in enumerate(services))
section = f'''      <section class="services section" id="leistungen" aria-labelledby="services-title">
        <div class="container">
          <div class="section-intro"><h2 id="services-title">Unsere Leistungen</h2><p>Schönheit, die zu Ihnen passt.</p></div>
          <div class="services-layout">
            <div class="service-preview" id="service-preview">{previews}
              <p class="service-preview-note">Design-Inspirationen, mit KI gestaltet.</p>
            </div>
            <div class="service-grid">
{items}
              <a class="text-link service-price-link" href="#preise">Preisliste ansehen <span class="link-arrow" aria-hidden="true"></span></a>
            </div>
          </div>
        </div>
      </section>'''
html = re.sub(r'      <section class="services section".*?</section>', lambda _: section, html, count=1, flags=re.S)

about = '''      <section class="about section" id="ueber-uns" aria-labelledby="about-title">
        <div class="container about-grid">
          <h2 id="about-title">Willkommen bei<br /><span>Emily Nails</span></h2>
          <figure class="about-media"><img src="assets/beauty-ritual.webp" alt="Beauty-Inspiration mit Nagellack und Pflegeaccessoires, mit KI gestaltet" width="1280" height="1024" loading="lazy" /><figcaption>Ein Moment <br />nur für Sie.</figcaption></figure>
          <div class="about-copy">
            <p class="about-lead">Bei Emily Nails stehen Schönheit, Qualität und Wohlbefinden im Mittelpunkt.</p>
            <p>Wir bieten professionelle Nagelpflege, moderne Nageldesigns sowie entspannende Pediküre in einer angenehmen und stilvollen Atmosphäre.</p>
            <p>Unser Ziel ist es, dass Sie sich bei jedem Besuch rundum wohlfühlen und unser Studio mit wunderschönen Nägeln verlassen.</p>
          </div>
          <div class="studio-values" id="why-us" aria-label="Warum Emily Nails?"><span>Professionelle Pflege</span><span>Hochwertige Produkte</span><span>Moderne Nageldesigns</span><span>Entspannte Atmosphäre</span></div>
        </div>
      </section>'''
html = re.sub(r'      <section class="about section".*?</section>', lambda _: about, html, count=1, flags=re.S)
html = html.replace('<h2 id="pricing-title">Unsere <br />Preisliste</h2>', '<h2 id="pricing-title">Unsere Preisliste</h2>')
html = re.sub(r'<details class="price-category"\s*(?:open)?\s*>', '<details class="price-category" open>', html)
html = html.replace('<h2 id="gallery-title">Schönheit bis ins<br />kleinste Detail</h2>', '<h2 id="gallery-title">Schönheit bis ins<br /><span>kleinste Detail</span></h2>')
html = html.replace('<div class="container">\n          <div class="contact-heading">', '<div class="container contact-layout">\n          <div class="contact-heading">')
path.write_text(html, encoding='utf-8')
