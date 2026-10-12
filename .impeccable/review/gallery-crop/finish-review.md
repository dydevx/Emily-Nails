# Gallery crop refinement

User requested crops for the four inspiration photographs in their screenshot. This is a refinement of the existing salon editorial layout, retaining its palette, captions, square corners, image assets and asymmetrical composition. The design and motion dials remain unchanged.

French now has a wider dominant portrait frame, using 2fr / 1fr / 1fr columns. Babyboomer and Goldakzente use square crops centered around the manicure. Shellac changes from a shallow 2.6:1 crop to a taller 3:2 frame with its focal point shifted downward, preserving all five nail tips. Mobile uses four square frames in the existing two-column grid. The gallery image dimensions now match the actual 1122 by 1402 pixel assets. Existing raster files and provenance are unchanged.

Desktop and mobile screenshots were inspected together. All nail tips remain visible, the French and Shellac lower edges align, and captions remain outside the photos. Checks passed at widths 320, 390, 700, 768, 1024, 1440 and 1920: loaded images, nonzero frames, no horizontal overflow and no JavaScript errors. Source diff check passed.

Mechanical detector results are retained in detector.json. Reported incumbent padding, radius, palette and typography findings are outside this crop refinement; the scoped image styles retain the established geometry and visible container spacing. No behavior or factual copy changed. Verdict: complete.
