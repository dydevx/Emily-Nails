# Mechanical detector, one run

Ran `impeccable detect --json index.html style.css script.js` once.

Remaining warnings require rendered interpretation:

- Cramped-padding: hero, about, contact are full-width section surfaces. Their content uses .container with 48px desktop or 20px mobile margins, plus 44/112/64px section vertical padding.
- Cramped-padding: studio-info child has 36px desktop or 20px mobile padding next to its 1px divider.
- Cramped-padding: video-frame is intentionally full-bleed image/video, not text.
- Cramped-padding: social has 43px block padding; footer-bottom delegates 22px block padding to .bottom-inner.
- Side-tab / border-accent-on-rounded: the play-icon pseudo-element is a CSS triangle made with three borders, inside a circular playback control. It is not a card accent border.

No second detector run is planned; verify through final rendered screenshots.
