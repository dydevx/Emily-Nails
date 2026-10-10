---
name: Emily Nails
description: Elegant salon editorial in the original logo's ivory, bronze-gold and blush palette.
colors:
  gold: "#8a613b"
  gold-deep: "#6c472b"
  background: "#fffaf5"
  cream: "#f5ebe2"
  petal: "#ead1cc"
  ink: "#403026"
  muted: "#705c4e"
  line: "#e0cfbe"
  white: "#ffffff"
typography:
  display:
    fontFamily: "Cormorant Garamond, Georgia, serif"
    fontSize: "clamp(66px, 7.2vw, 96px)"
    fontWeight: 500
    lineHeight: 1.08
    letterSpacing: "-0.035em"
  headline:
    fontFamily: "Cormorant Garamond, Georgia, serif"
    fontSize: "clamp(50px, 5.6vw, 80px)"
    fontWeight: 500
    lineHeight: 1.08
    letterSpacing: "-0.035em"
  title:
    fontFamily: "Cormorant Garamond, Georgia, serif"
    fontSize: "32px"
    fontWeight: 500
    lineHeight: 1.08
    letterSpacing: "-0.035em"
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
  content-gap: "24px"
  tablet-gap: "35px"
  price-gap: "28px"
  section-mobile: "64px"
  section-tablet: "80px"
  section-desktop: "112px"
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
    textColor: "{colors.gold}"
  price-category:
    backgroundColor: "{colors.cream}"
    textColor: "{colors.ink}"
    padding: "28px 32px"
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

Emily Nails pairs warm ivory surfaces with bronze-gold actions and soft blush accents taken from the original logo. The original logo and local social icons anchor the identity. Expressive serif headings and readable service information preserve the elegant, gentle character.

This is a native static HTML, CSS and JavaScript system with one light theme. Typography, tonal section changes and thin dividers carry the visual hierarchy. Keep the original logo and German business truth: services, prices, contact information, opening hours, social links and legal attribution remain faithful to the salon.

**Key Characteristics:**

- Warm ivory surfaces, bronze-gold accents and gentle blush details.
- Self-hosted serif display type paired with a clear sans serif body.
- Varied editorial proportions, rectangular media and generous vertical rhythm.
- Thin dividers, subtly rounded controls and native progressive disclosure.
- Purposeful cover and selection motion with a complete reduced-motion alternative.

## Colors

The palette follows the cream, bronze-gold and pink details of logo.jpg; the frontmatter is the normative color source.

### Primary

- **Bronze Gold:** primary actions, selected navigation, heading accents and focus outlines.
- **Deep Bronze:** primary hover, secondary action text and editorial text links.

### Neutral

- **Warm Paper:** the background token; the page, header, footer and dialog surface.
- **Warm Cream:** cream section backgrounds, providing tonal separation without heavy containers.
- **Petal Blush:** media placeholders, secondary hover, close controls and text selection.
- **Warm Brown Ink:** headings, prices and main copy.
- **Muted Warm Brown:** supporting descriptions, captions and practical labels.
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
- **Body:** default text; supporting service, price and contact copy uses (12?15px), with no copy below (12px). Service descriptions stay within (48ch), gallery copy within (45ch), and contact copy within (46ch).
- **Label:** action text, medium-bold and sentence case. Supporting labels use smaller sizes (12–13px).
- **Navigation:** compact desktop links; mobile links increase to (15px).

**The Two Voices Rule.** Use the serif for editorial titles and the sans serif for functional information, controls and numbers. Preserve tabular numerals for prices, telephone numbers and opening hours.

## Layout

The centered container caps at (1320px), with total horizontal inset (112px). Use open space, thin rules, varied column proportions and deliberate image baselines to create hierarchy. Standard section padding is (112px), reducing to (80px) at (980px) and (64px) at (700px). The current page's composition contract lives in `.impeccable/surfaces/index-html.md`; these measurements document its implementation rather than prescribe identical compositions for every future surface.

At (1200px), total container inset becomes (72px), navigation gaps narrow and the wordmark hides. At (980px), the header becomes (72px) high with a disclosure menu and the wordmark returns. At (700px), total inset becomes (40px), the header becomes (70px) high, and major spreads stack. At (370px), total inset becomes (32px) and the wordmark hides.

The current cover shares a twelve-column grid between a two-line headline and a photograph. The heading spans columns 1?11; the photograph occupies columns 6?12 across both grid rows. The photograph is absolutely positioned inside its grid region so intrinsic image height cannot expand the cover. Copy and appointment actions occupy the lower left. On mobile, a six-column grid places headline, inset photograph and actions in successive rows; the photograph row is (240px), becoming (205px) at (370px).

The service catalogue pairs a sticky shared preview with six selectable treatment descriptions. Desktop proportions are (.9fr / 1fr), with a responsive gap and (590px) preview image. The preview reduces to (550px) at (1200px) and (520px) at (980px). At (700px), it stays sticky above a two-column selection list: top offset (84px), photo height (240px), becoming (210px) at (370px). Without JavaScript, all six photographs and descriptions remain in a three-column grid, reducing to two columns on mobile.

The studio feature uses a centered heading, a wide image with a side caption and three prose columns. Mobile stacks these, aligns the heading left and renders the caption as a continuous phrase. Complete pricing occupies two columns of open native disclosures, reducing to one column on mobile. The inspiration gallery uses unequal placements in a twelve-column desktop grid and staggered two-column mobile images. Original studio photo and video remain a distinct media pair. Contact pairs a large invitation with practical address and hours; mobile stacks them. Social links use three columns on desktop and a vertical mobile list.

Display type reduces at (980px) to clamp(56px, 7.2vw, 76px), then at (700px) to clamp(40px, 10.6vw, 70px). Mobile headlines use clamp(43px, 10.5vw, 66px), general titles (28px). Studio and contact headings have their own larger editorial scales. Keep media rectangular with deliberate object-fit crops, explicit intrinsic dimensions and lazy loading below the fold. Seven existing local AI WebP images provide service and design inspiration; provenance remains in `assets/provenance.json`. Their German inspiration label stays visible. The original pedicure photograph and user-triggered video retain their own identity.

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

Six native buttons select a shared photographic preview and expose their state with aria-pressed. Selected labels use gold and a horizontal fine arrow; unselected arrows turn upward. Hover deepens the text color, and keyboard focus remains visible. Selecting a treatment changes its photograph and caption; every treatment description remains visible. The shared preview is sticky on desktop (110px top) and mobile (84px top), without automatic cycling. Without JavaScript, the complete static photograph grid remains available.

Captions sit beside or below square-cornered media. The inspiration gallery varies frame size and vertical placement. The original studio video keeps native controls and preload none; its overlay play affordance disappears during playback. Media plays only after an explicit action.

### Pricing Disclosures

Native details and summary elements group the complete published prices and start open. Pale cream groups use desktop padding (28px 32px) and mobile padding (23px), with square corners. Summary rows pair a serif category title (35px desktop) with a muted starting price and a gold plus/minus marker. The open rows align treatment labels left and tabular prices right; labels may wrap while price values stay intact. The native disclosure remains operable without JavaScript.

### Original Menu Dialog

A native dialog presents the original price-list image with a sticky header, a large close control and a link to the full image. It caps its width at (850px) and height at calc(100dvh - 40px). Escape, the close button and backdrop click dismiss it; dismissal restores focus to its opening link. The underlying image link remains a fallback when dialog support is absent.

### Motion and Accessibility

The cover headline enters with an upward movement (18px) and opacity change (.8 to 1), taking (.9s). The photograph reveals its lower edge with clip-path over (1.1s). Service selection fades (.5 to 1) and lifts the new image (8px) over (.45s). All use the shared cubic-bezier(.16, 1, .3, 1) easing. Control state changes remain brief (.2s); social icon states take (.25s). With prefers-reduced-motion, all animation and transitions are removed and scrolling becomes immediate. Keep the skip link, meaningful German accessible labels and visible keyboard focus.

### Social Links

Use the official local Tabler outline brand SVGs for Instagram, Facebook and TikTok, rendered with currentColor in 54px cream icon tiles. Gold icon strokes match the logo; hover and focus fill the tile bronze-gold and turn the icon white. Pair each icon with the platform name and actual profile handle. The main section uses three columns on desktop and a vertical list on mobile. Footer icons use a quieter 17px size. Keep SVGs aria-hidden because the adjacent text supplies the accessible name. The MIT license is included in assets/icons/LICENSE.txt.

## Do's and Don'ts

### Do:

- **Do** retain the elegant, gentle logo-derived palette and the original Emily Nails logo.
- **Do** use serif hierarchy, readable sans copy and tabular practical information.
- **Do** preserve responsive stacking, thin dividers and generous space around grouped content.
- **Do** retain every published German business fact and keep booking actions connected to the existing phone and SMS links.
- **Do** preserve native disclosure, dialog fallbacks, keyboard focus and reduced-motion behavior.

### Don't:

- **Don't** present decorative campaign imagery as completed salon work.
- **Don't** invent reviews, ratings, services, prices or an online booking workflow.
- **Don't** add a dark theme or replace the approved ivory, gold and blush direction with another identity.
- **Don't** put ordinary services and prices into heavily rounded, shadowed cards.
- **Don't** autoplay video or make content visibility depend on animation or JavaScript.
