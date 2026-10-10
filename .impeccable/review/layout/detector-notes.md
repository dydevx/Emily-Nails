# Layout verification

The pre-edit source/screenshot assessment identified hero overlap, inconsistent heading alignment and scale, scattered gallery offsets and an obstructive sticky mobile service preview. The correction addresses all four with a shared 1200px container, left-aligned 60px maximum section hierarchy, 32px content gaps, no negative gallery offsets and inline mobile service photography.

The before and after layout detectors each returned five non-advisory warnings. All are static-parser limitations: about/contact/social section gutters and vertical padding are inherited through .container and .section and are visible in the captures; video-frame is full-bleed media with no text needing inset; footer-bottom receives its vertical spacing from .bottom-inner. These do not require padding inside media or additional outer section boxes.

Responsive browser verification passes at 320, 390, 700, 768, 1024, 1280 and 1440px, without horizontal overflow, with two heading lines and a visible appointment CTA. Complete published prices, navigation and footer remain preserved. Desktop shared preview and six mobile inline-photo selections, keyboard Enter/Space, disclosures, menu/Escape, dialog/focus restoration, playback, reduced motion and the no-JS fallback pass.

No new raster imagery; existing assets/provenance.json remains the source record.
