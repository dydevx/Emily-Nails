---
name: Emily Nails
description: Elegant salon editorial in the original logo's ivory, bronze-gold and blush palette.
colors:
  gold: "#8a613b"
  gold-deep: "#6c472b"
  background: "#fffaf5"
  cream: "#f5ebe2"
  petal: "#ead1cc"
  cover: "#f8eee8"
  ink: "#2d211b"
  muted: "#514137"
  line: "#e0cfbe"
  white: "#ffffff"
typography:
  display:
    fontFamily: "Cormorant Garamond, Georgia, serif"
    fontSize: "clamp(60px, 6vw, 80px)"
    fontWeight: 500
    lineHeight: 1.08
    letterSpacing: "-0.025em"
  headline:
    fontFamily: "Cormorant Garamond, Georgia, serif"
    fontSize: "clamp(44px, 4.5vw, 60px)"
    fontWeight: 500
    lineHeight: 1.08
    letterSpacing: "-0.025em"
  title:
    fontFamily: "Cormorant Garamond, Georgia, serif"
    fontSize: "30px"
    fontWeight: 500
    lineHeight: 1.08
    letterSpacing: "-0.025em"
  body:
    fontFamily: "DM Sans, Arial, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.7
  label:
    fontFamily: "DM Sans, Arial, sans-serif"
    fontSize: "13px"
    fontWeight: 600
    lineHeight: 1.7
  navigation:
    fontFamily: "DM Sans, Arial, sans-serif"
    fontSize: "13px"
    fontWeight: 500
    lineHeight: 1.7
rounded:
  control: "6px"
  dialog: "12px"
  play: "50%"
spacing:
  control-gap: "12px"
  content-gap: "32px"
  content-gap-mobile: "24px"
  tablet-gap: "35px"
  price-gap: "24px"
  section-mobile: "56px"
  section-tablet: "72px"
  section-desktop: "104px"
components:
  button-primary:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.white}"
    typography: "{typography.label}"
    rounded: "{rounded.control}"
    padding: "12px 25px"
  button-primary-hover:
    backgroundColor: "{colors.gold-deep}"
    textColor: "{colors.white}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.gold-deep}"
    typography: "{typography.label}"
    rounded: "{rounded.control}"
    padding: "12px 25px"
  button-secondary-hover:
    backgroundColor: "{colors.petal}"
  text-link:
    textColor: "{colors.gold-deep}"
  navigation-link:
    textColor: "{colors.ink}"
    typography: "{typography.navigation}"
    padding: "12px 0"
  service-select:
    textColor: "{colors.ink}"
    padding: "0"
  service-select-active:
    textColor: "{colors.gold-deep}"
  price-category:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    padding: "0"
  dialog-close:
    backgroundColor: "{colors.petal}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    height: "44px"
    width: "44px"
---

# Design System: Emily Nails

## Overview

**Creative North Star: "Gentle Salon Editorial"**

Emily Nails pairs warm ivory surfaces with bronze-gold actions and soft blush accents taken from the original logo. The original logo and local social icons anchor the identity. Restrained serif headings, shared alignments and readable service information preserve the elegant, gentle character.

This is a native static HTML, CSS and JavaScript system with one light theme. Typography, tonal section changes and thin dividers carry the visual hierarchy. Keep the original logo and German business truth: services, prices, contact information, opening hours, social links and legal attribution remain faithful to the salon.

**Key Characteristics:**

- Warm ivory surfaces, bronze-gold accents and gentle blush details.
- Self-hosted serif display type paired with a clear sans serif body.
- Clear content grouping, aligned rectangular media and consistent vertical rhythm.
- Thin dividers, subtly rounded controls and native progressive disclosure.
- Purposeful cover and selection motion with a complete reduced-motion alternative.

## Colors

The palette follows the cream, bronze-gold and pink details of logo.jpg; the frontmatter is the normative color source.

### Primary

- **Bronze Gold:** primary action backgrounds, icons and focus outlines.
- **Deep Bronze:** emphasized headings, selected service labels, navigation, primary hover and text links.

### Neutral

- **Warm Paper:** the background token; the page, header, footer and dialog surface.
- **Warm Cream:** cream section backgrounds, providing tonal separation without heavy containers.
- **Petal Blush:** media placeholders, secondary hover, close controls and text selection.
- **Warm Brown Ink:** deep brown for headings, prices and main copy.
- **Muted Warm Brown:** darker supporting descriptions, captions and practical labels for clear contrast against the pale backgrounds.
- **Cream Divider:** thin borders between services, prices, hours and navigation areas.
- **White:** primary button text and the circular video play control.

**The Quiet Accent Rule.** Use gold to make actions and selected content clear; retain pale surfaces as the dominant material.

## Typography

**Display Font:** Cormorant Garamond, with Georgia and serif fallbacks.
**Body Font:** DM Sans, with Arial and sans-serif fallbacks.

Both families are self-hosted as WOFF2 files in assets, use font-display swap, and support weights 400–700. The serif supplies elegance; the sans keeps German treatment names, prices and opening hours easy to scan. Headings balance their wrapping and use the frontmatter's close tracking.

### Hierarchy

- **Display:** the main invitation; a gold-colored phrase may share the same scale.
- **Headline:** section introductions and the contact invitation.
- **Title:** services, gallery captions and contact subheadings. Pricing summaries use a larger serif size (35px) with a slightly looser line height (1.15).
- **Body:** default text; supporting service, price and contact copy uses (12 to 15px), with no copy below (12px). Service descriptions stay within (48ch), gallery copy within (45ch), and contact copy within (46ch).
- **Label:** action text, medium-bold and sentence case. Supporting labels use smaller sizes (12–13px).
- **Navigation:** compact desktop links; mobile links increase to (15px).

**The Two Voices Rule.** Use the serif for editorial titles and the sans serif for functional information, controls and numbers. Preserve tabular numerals for prices, telephone numbers and opening hours.

## Layout

The centered container caps at (1200px), with total horizontal inset (96px). Shared left edges, clear grouping and restrained heading hierarchy keep content orderly. Section spacing uses the shared (104px) token, becoming (72px) at (980px) and (56px) at (700px). The content gap is (32px) on desktop and (24px) on mobile. The current page's composition contract lives in `.impeccable/surfaces/index-html.md`; measurements here record the current implementation.

At (1200px), total container inset becomes (64px) while retaining the maximum-width cap. At (980px), the header becomes (72px) high with a disclosure menu and the wordmark returns. At (700px), total inset becomes (40px), the header becomes (70px) high, and major spreads stack. At (370px), total inset becomes (32px) and the wordmark hides.

The blush cover places its two-line heading above a twelve-column media row. The heading and photograph use grid lines 1 / 9. The photograph has a responsive (3 / 2) frame, approximately (526px high) at the maximum container width. Object-position (50% 82%) centers both manicures and keeps the lower fingertips visible. The copy/actions use 9 / -1 and span both rows, with 24px inner inset. The introduction uses 30px serif type. At (980px), the introduction becomes 25px and its inset is removed. The image remains absolutely fitted inside its assigned region. Mobile reading order is headline, description and actions, then a full-width square photograph with object-position (50% 100%). Frame height follows its width rather than a fixed pixel height.

Desktop services pair a shared photograph with six treatment descriptions, using (.9fr / 1fr) columns and a (72px) gap. The preview participates in normal flow. Its image is (560px) high, reducing to (540px) at (1200px) and (520px) at (980px). At (700px), the shared stage hides and the list uses one column; only the selected article opens its inline photograph (240px high). All descriptions and the German inspiration note remain available. Without JavaScript, all six photographs and descriptions form a three-column desktop grid and two-column mobile grid.

The studio story uses a standard left-aligned section heading, full-width image (3 / 1), caption underneath and three prose columns. Mobile changes the photo to (5 / 4) and stacks the story. Pricing uses left-aligned headings and equal two-column rows with aligned group edges; mobile uses one column. The inspiration collection uses (2fr / 1fr / 1fr) columns: French spans two rows with a wider portrait frame; Babyboomer and Goldakzente use square frames above a (3 / 2) Shellac photograph. Individual object-position values are French (50% 65%), Babyboomer (50% 60%), Goldakzente (50% 55%) and Shellac (50% 65%), preserving nail tips. Mobile uses an equal two-column grid with square images and Shellac shifts to (50% 80%). The original studio photograph and video occupy equal desktop columns, both (380px) high, reducing to (300px) at (980px). Mobile stacks these media. Contact uses a (1fr / 1.15fr) spread: the invitation sits beside address and hours in two columns. Below 1200px, the practical columns stack; mobile stacks the whole spread. Social links retain three desktop columns and a vertical mobile list.

Display type reduces at (980px) to clamp(54px, 7vw, 68px), then at (700px) to clamp(40px, 10.6vw, 70px). Mobile headlines use clamp(38px, 9.5vw, 52px), general titles (28px). Studio and contact share the standard heading scale. Keep rectangular media, deliberate object-fit crops, intrinsic dimensions and lazy loading below the fold. Seven existing local AI WebP images provide service and design inspiration; provenance remains in `assets/provenance.json`. Their German inspiration label stays visible. The original pedicure photograph and user-triggered video retain their own identity.

## Elevation & Depth

Depth comes mainly from alternating paper and cream surfaces with thin dividers. Services and price lists remain flat. Shadows are limited to the mobile navigation, video play control and modal dialog; their exact values live in the sidecar. The dialog uses a dark translucent backdrop to separate the original printed menu from the page.

**The Flat Content Rule.** Keep ordinary content flat; reserve elevation for interactive overlays and the video play affordance.

## Shapes

Images and open content regions have square corners. Social icon tiles use 16px corners, the link focus boundary uses 12px, and other controls use the small shared 6px radius; the dialog is softly rounded, and the video play control is circular. Borders are thin (1px) and generally use the divider token. Native pricing disclosures use a small plus/minus marker rather than a large icon badge. Directional arrows remain fine strokes.

## Components

### Buttons

Primary and secondary actions share compact padding and medium-bold sans typography (13px). The shared base uses a minimum height (52px); header and mobile variants adapt to available space. Primary actions pair gold with white; secondary actions have a gold outline and transparent surface. Primary hover deepens the gold; secondary hover adds soft petal. Press scales the control to (.98). Color and transform changes take (.2s).

Every interactive element retains the global visible focus outline (2px), offset by (5px). Text links use a minimum target height (44px), a fine arrow and hover underline.

### Navigation

The header is sticky and separated by a thin bottom divider. Desktop navigation uses a fine animated underline for hover and the observed section marked by aria-current. Below the navigation breakpoint, a bordered menu toggle opens a full-width paper menu. Escape restores focus to the toggle; section selection, outside click and focus leaving the header close the menu. Without JavaScript, mobile navigation remains visible as wrapping links.

### Services and Media

Six native buttons select a treatment with aria-pressed and aria-controls linking the shared preview and its inline image. Selected rows use a cream surface with a 20px inset (14px on mobile). Selected labels use deep bronze and a horizontal fine arrow; unselected arrows turn upward. Desktop labels use clamp(28px, 2.8vw, 36px), tablet (31px) and mobile (29px). Every description remains visible. Desktop selection changes the shared photograph and caption. Mobile selection opens only that article's inline photograph; the shared stage is hidden. The catalogue stays in normal flow and does not cycle automatically. Without JavaScript, the complete static photograph grid remains available.

Captions sit below square-cornered media; the studio caption uses (38px) serif type, reducing to (32px) on mobile. The inspiration collection groups one dominant frame with three aligned companions. The original video retains native controls and preload none; its overlay play affordance disappears during playback. Media plays only after an explicit action.

### Pricing Disclosures

Native details and summary elements group the complete published prices and start open. Category headers use pale cream with desktop padding (24px 28px) and mobile padding (20px). The open menu body uses the page surface, padding (20px 28px 24px), and 14px rows with medium-bold tabular prices. Categories remain square and end with a thin divider. Summary rows pair a serif category title (35px desktop) with a muted starting price and a gold plus/minus marker. The open rows align treatment labels left and tabular prices right; labels may wrap while price values stay intact. The native disclosure remains operable without JavaScript.

### Original Menu Dialog

A native dialog presents the original price-list image with a sticky header, a large close control and a link to the full image. It caps its width at (850px) and height at calc(100dvh - 40px). Escape, the close button and backdrop click dismiss it; dismissal restores focus to its opening link. The underlying image link remains a fallback when dialog support is absent.

### Motion and Accessibility

The cover headline enters with an upward movement (18px) and opacity change (.8 to 1), taking (.9s). The photograph reveals its lower edge with clip-path over (1.1s). The desktop shared preview fades (.5 to 1) and lifts the new image (8px) over (.45s). All use the shared cubic-bezier(.16, 1, .3, 1) easing. Control state changes remain brief (.2s); social icon states take (.25s). With prefers-reduced-motion, all animation and transitions are removed and scrolling becomes immediate. Keep the skip link, meaningful German accessible labels and visible keyboard focus.

### Social Links

Use the official local Tabler outline brand SVGs for Instagram, Facebook and TikTok, rendered with currentColor in 54px cream icon tiles. Gold icon strokes match the logo; hover and focus fill the tile bronze-gold and turn the icon white. Pair each icon with the platform name and actual profile handle. The main section uses three columns on desktop and a vertical list on mobile. Footer icons use a quieter 17px size. Keep SVGs aria-hidden because the adjacent text supplies the accessible name. The MIT license is included in assets/icons/LICENSE.txt.

## Do's and Don'ts

### Do:

- **Do** retain the elegant, gentle logo-derived palette and the original Emily Nails logo.
- **Do** use serif hierarchy, readable sans copy and tabular practical information.
- **Do** preserve shared alignment, responsive stacking, thin dividers and consistent space around grouped content.
- **Do** retain every published German business fact and keep booking actions connected to the existing phone and SMS links.
- **Do** preserve native disclosure, dialog fallbacks, keyboard focus and reduced-motion behavior.

### Don't:

- **Don't** present decorative campaign imagery as completed salon work.
- **Don't** invent reviews, ratings, services, prices or an online booking workflow.
- **Don't** add a dark theme or replace the approved ivory, gold and blush direction with another identity.
- **Don't** put ordinary services and prices into heavily rounded, shadowed cards.
- **Don't** autoplay video or make content visibility depend on animation or JavaScript.
