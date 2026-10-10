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
    fontSize: "clamp(48px, 5.1vw, 76px)"
    fontWeight: 500
    lineHeight: 1.08
    letterSpacing: "-0.025em"
  headline:
    fontFamily: "Cormorant Garamond, Georgia, serif"
    fontSize: "clamp(42px, 4.15vw, 62px)"
    fontWeight: 500
    lineHeight: 1.08
    letterSpacing: "-0.025em"
  title:
    fontFamily: "Cormorant Garamond, Georgia, serif"
    fontSize: "29px"
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
    fontSize: "14px"
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
  mobile-gap: "30px"
  stacked-gap: "35px"
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
  price-category:
    textColor: "{colors.ink}"
    padding: "23px 2px"
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

Emily Nails pairs warm ivory surfaces with bronze-gold actions and soft blush accents taken from the original logo. The user requested this logo palette, more AI beauty imagery and custom social icons. Expressive serif headings and readable service information preserve the elegant, gentle character.

This is a native static HTML, CSS and JavaScript system with one light theme. Typography, tonal section changes and thin dividers carry the visual hierarchy. Keep the original logo and German business truth: services, prices, contact information, opening hours, social links and legal attribution remain faithful to the salon.

**Key Characteristics:**

- Warm ivory surfaces, bronze-gold accents and gentle blush details.
- Self-hosted serif display type paired with a clear sans serif body.
- Open editorial grids, rectangular media and generous vertical rhythm.
- Thin dividers, subtly rounded controls and native progressive disclosure.
- Gentle entrance motion with a complete reduced-motion alternative.

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
- **Title:** services, gallery captions and contact subheadings. Pricing summaries use the same serif size with a slightly looser line height (1.15).
- **Body:** default text; detailed service, price and contact copy is commonly smaller (14px). Descriptions remain constrained: service copy (36ch), about copy (55ch), gallery copy (50ch).
- **Label:** action text, medium-bold and sentence case. Supporting labels use smaller sizes (12–13px).
- **Navigation:** compact desktop links; mobile links increase to (15px).

**The Two Voices Rule.** Use the serif for editorial titles and the sans serif for functional information, controls and numbers. Preserve tabular numerals for prices, telephone numbers and opening hours.

## Layout

The desktop container is centered, capped at (1240px), with total horizontal inset (96px). Standard sections use the documented desktop rhythm. The services heading leads a three-column image grid. Pricing keeps its heading beside native disclosures; studio media uses asymmetric two-column grids. Dividers and open space provide grouping instead of a repeated card shell.

At (1200px), total container inset reduces to (64px), navigation gaps narrow and the brand wordmark temporarily hides. At (980px), the header becomes (72px) high with a disclosure menu, sections use the tablet rhythm and media/grid gaps compress. At (700px), total inset becomes (40px), major sections stack, the header becomes (70px), and sections use the mobile rhythm. The gallery has zero top padding on mobile so the gap after pricing remains deliberate. Services change from three to two columns below 700px. The design inspiration grid changes from four to two columns; social links change from three columns to a vertical list. At (370px), total inset becomes (32px), the wordmark hides and the hero media height reduces to (290px).

Desktop display type changes at (1200px) to clamp(48px, 5.8vw, 68px), then (49px) at (980px). At (700px), display type uses clamp(42px, 10.3vw, 62px), headlines use clamp(39px, 9vw, 52px), and general titles use (27px). Above (1600px), only the hero's vertical padding increases from (44px) to (54px).

Media stays in the document flow. Static images use deliberate object-fit crops; the video plays only when requested. Keep images rectangular, provide actual intrinsic dimensions, and retain lazy loading for below-the-fold images. Seven unique AI images illustrate the hero, six services, the studio introduction and a four-image inspiration collection. All generated assets are local WebP files with provenance in assets/provenance.json. A concise German label identifies the inspiration collection. The original pedicure photograph and video remain in a separate media pair.

## Elevation & Depth

Depth comes mainly from alternating paper and cream surfaces with thin dividers. Services and price lists remain flat. Shadows are limited to the mobile navigation, video play control and modal dialog; their exact values live in the sidecar. The dialog uses a dark translucent backdrop to separate the original printed menu from the page.

**The Flat Content Rule.** Keep ordinary content flat; reserve elevation for interactive overlays and the video play affordance.

## Shapes

Images and open content regions have square corners. Social icon tiles use 16px corners, the link focus boundary uses 12px, and other controls use the small shared 6px radius; the dialog is softly rounded, and the video play control is circular. Borders are thin (1px) and generally use the divider token. Native pricing disclosures use a small plus/minus marker rather than a large icon badge. Directional arrows remain fine strokes.

## Components

### Buttons

Primary and secondary actions share compact padding and medium-bold sans typography. The shared base uses a minimum height (50px); header and mobile variants adapt to available space. Primary actions pair gold with white; secondary actions have a gold outline and transparent surface. Primary hover deepens the gold; secondary hover adds soft petal. Press scales the control to (.98). Color and transform changes take (.2s).

Every interactive element retains the global visible focus outline (2px), offset by (5px). Text links use a minimum target height (44px), a fine arrow and hover underline.

### Navigation

The header is sticky and separated by a thin bottom divider. Desktop navigation uses a fine animated underline for hover and the observed section marked by aria-current. Below the navigation breakpoint, a bordered menu toggle opens a full-width paper menu. Escape restores focus to the toggle; section selection, outside click and focus leaving the header close the menu. Without JavaScript, mobile navigation remains visible as wrapping links.

### Services and Media

Services are open image-led groups: rectangular campaign photograph, serif title and constrained description, without a card shell. The image grid uses three columns on desktop and two on mobile. Image hover scales gently to 1.035. Captions sit below rectangular media. The gallery video keeps native controls and preload none; its overlay play affordance disappears during playback. Avoid autoplay or media backgrounds that compete with the treatment information.

### Pricing Disclosures

Native details and summary elements group the complete published prices. Summary rows pair a serif category title with a muted starting price and a gold plus/minus marker. The open rows align treatment labels left and tabular prices right; labels may wrap while price values stay intact. The native disclosure remains operable without JavaScript.

### Original Menu Dialog

A native dialog presents the original price-list image with a sticky header, a large close control and a link to the full image. It caps its width at (850px) and height at calc(100dvh - 40px). Escape, the close button and backdrop click dismiss it; dismissal restores focus to its opening link. The underlying image link remains a fallback when dialog support is absent.

### Motion and Accessibility

Only the opening copy and campaign media enter with a short upward movement (12px) and opacity change, taking (.85s) with the shared easing; media begins (.1s) later. State changes are brief and quiet. With prefers-reduced-motion, all animation and transitions are removed and scrolling becomes immediate. Keep the skip link, meaningful German accessible labels and visible keyboard focus.

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
