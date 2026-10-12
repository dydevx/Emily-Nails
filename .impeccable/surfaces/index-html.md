---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: ["style.css","script.js"]
---

# Magazine redesign

Mode: Persuade. User confirmed a whole-page redesign in a beauty-magazine direction. Retain the existing logo palette, German content, local imagery, business facts, navigation and phone/SMS booking.

## Direction contract

THESIS: A beauty magazine with clear grouping and a common alignment system. User rejected the earlier overlapping headline, scattered gallery and sticky mobile preview as cluttered; order takes priority over arbitrary variation.

OWN-WORLD: Existing ivory, cream, bronze and blush. Self-hosted Cormorant and DM Sans preserve the brand. Left-aligned headings, square photographic frames, thin rules, restrained rectangular controls. Shared 1200px content width, 32px content gaps and restrained heading hierarchy.

STORY: See the nail-care invitation, explore six services, meet the studio, compare the complete prices, browse design inspiration, then call or text.

FIRST VIEWPORT: Two-line title up to 80px above a wide photograph on the left and a serif introduction/action group on the right, spanning the title and media rows. Nothing overlaps. Mobile reads title, copy and actions, photograph, then practical contact information.

FORM: User-selected beauty magazine, code-led, corrected to be orderly after direct user feedback. Original seed 5fcc18e4 remains historical, not a reason to preserve rejected details. Desktop services use a shared preview; mobile opens the selected photograph within a single-column service list, without sticky overlays. About is a wide photo/story, prices an aligned two-column open menu, gallery one dominant frame beside three aligned companions, contact a practical closing spread.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

GALLERY CROP: French retains the dominant two-row frame with wider 2fr / 1fr / 1fr columns. Babyboomer and Goldakzente have square close-ups; Shellac uses a taller 3:2 frame that preserves all nail tips. Each photograph has its own focal point. Mobile keeps two columns and uses four square photographs. See `review/gallery-crop/finish-review.md` and `review/gallery-crop/verification.json`.

## Refinement

Blush cover with a responsive 3:2 desktop photograph cropped at 50% 82%, and a square mobile photograph cropped at 50% 100%. Both sets of nail tips remain visible. Retain 104px section spacing, cream selected-service rows, category-header price menus and adjacent address/hours columns on wide screens. See `.impeccable/review/hero-crop/finish-review.md` for the crop refinement and `review/hero-crop/verification.json` for responsive checks. Earlier interaction checks remain in `review/upgrade/verification.json`.
