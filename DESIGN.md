---
name: T91 Padel
description: Sport-retail ground in white and black, one HOLO orange for action, condensed heavy caps, services as big typographic rows.
colors:
  ink: "#0b0b0b"
  ink-2: "#2a2a28"
  paper: "#ffffff"
  stone: "#f1f0ed"
  line: "#d9d8d3"
  muted: "#5f5e59"
  holo-orange: "#ff6a13"
  holo-orange-ink: "#b83e00"
  ink-line: "#2c2c2a"
  ink-muted: "#b4b3ad"
typography:
  display-xl:
    fontFamily: "Big Shoulders Display, Arial Narrow, sans-serif"
    fontSize: "clamp(3.4rem, 10.5vw, 6rem)"
    fontWeight: 900
    lineHeight: 0.88
    letterSpacing: "-0.01em"
  display-l:
    fontFamily: "Big Shoulders Display, Arial Narrow, sans-serif"
    fontSize: "clamp(2.6rem, 6.2vw, 5rem)"
    fontWeight: 900
    lineHeight: 0.88
    letterSpacing: "-0.01em"
  display-m:
    fontFamily: "Big Shoulders Display, Arial Narrow, sans-serif"
    fontSize: "clamp(1.8rem, 3.6vw, 3rem)"
    fontWeight: 900
    lineHeight: 0.88
    letterSpacing: "-0.01em"
  row-title:
    fontFamily: "Big Shoulders Display, Arial Narrow, sans-serif"
    fontSize: "clamp(1.7rem, 3vw, 2.6rem)"
    fontWeight: 900
    lineHeight: 0.95
  body:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.55
  lede:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "clamp(1rem, 1.5vw, 1.2rem)"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "11px"
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "0.12em"
  button:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "0.12em"
rounded:
  none: "0"
spacing:
  gutter: "clamp(16px, 3vw, 40px)"
  row-y: "22px"
  button-y: "17px"
  button-x: "26px"
  section-y: "clamp(56px, 9vw, 120px)"
components:
  button-solid:
    backgroundColor: "{colors.holo-orange}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "17px 26px"
    typography: "{typography.button}"
  button-solid-hover:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
  button-ink:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.none}"
    padding: "17px 26px"
  button-ink-hover:
    backgroundColor: "{colors.holo-orange}"
    textColor: "{colors.ink}"
  button-line:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "17px 26px"
  button-line-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
  announcement-strip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    typography: "{typography.label}"
  service-row:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    padding: "22px 0"
  badge-new:
    backgroundColor: "{colors.holo-orange}"
    textColor: "{colors.ink}"
    padding: "6px 8px"
---

# Design System: T91 Padel

## Overview

**Creative North Star: "The Retail Floor with the Lights Off"**

A white retail ground interrupted by black campaign fields, as in a sport-fashion store. Services get the same typographic weight as products: large condensed caps, hairline rules, full-bleed photography. Corners are square, there are no cards and no shadows; structure comes from rules, tonal fields (white, stone, black) and scale.

One orange, the HOLO racket colour, is the only chromatic voice. It marks action and status and is never decoration across a whole surface. Density is generous in section padding and tight in type (display line-height 0.88).

**Key Characteristics:**
- White ground, black campaign fields, stone as the quiet third tone.
- Big Shoulders Display 900 uppercase against Archivo; tiny tracked uppercase for navigation and buttons.
- Square corners, 1px hairlines, no shadows.
- Full-bleed photography with a bottom black gradient for headline legibility.
- Motion is slow reveal on a single expo-out ease.

## Colors

Monochrome ink and paper with one saturated orange.

### Primary
- **HOLO Orange** (#ff6a13): fill for the primary action, "new" badge, large numerals on dark fields, focus outline, selection, row hover underline.
- **HOLO Orange Ink** (#b83e00): the orange when it must be read as text or numerals on white or stone (contrast-safe), and guide-title hover.

### Neutral
- **Ink** (#0b0b0b): body text, black fields (hero, centres, footer, strip), solid ink buttons.
- **Ink 2** (#2a2a28): declared, held in reserve.
- **Paper** (#ffffff): page ground.
- **Stone** (#f1f0ed): community text panel, scrollbar track.
- **Line** (#d9d8d3): hairlines on white.
- **Muted** (#5f5e59): secondary copy on white.
- **Ink Line** (#2c2c2a): hairlines on black fields.
- **Ink Muted** (#b4b3ad): secondary copy on black fields.

### Named Rules
**The One Orange Rule.** Orange fills mark action or status only. On white, orange as text uses HOLO Orange Ink, never the bright orange.
**The Two Grounds Rule.** Every section is either white/stone or black (`dark`); mixed-tone sections do not exist. Hairlines switch from Line to Ink Line with the ground.

## Typography

**Display Font:** Big Shoulders Display (with Arial Narrow, sans-serif), weights 700 and 900, loaded from Google Fonts.
**Body Font:** Archivo (with system-ui), weights 400 to 700.

**Character:** a sport-poster condensed voice for everything that is a headline, name, price or number; a neutral grotesk for reading and for the small tracked labels.

### Hierarchy
- **Display XL** (900, clamp 3.4rem to 6rem, 0.88): hero headline, max 12ch.
- **Display L** (900, clamp 2.6rem to 5rem, 0.88): section statements.
- **Display M** (900, clamp 1.8rem to 3rem, 0.88): section titles.
- **Row title** (900, clamp 1.7rem to 2.6rem, 0.95): service rows; also plan names, FAQ summaries and guide titles at smaller fixed sizes (1.5rem to 1.9rem).
- **Numerals** (900, up to 17rem, 0.8, orange): centre count and service numbers; tabular figures for prices.
- **Body** (400, 15px, 1.55): copy; ledes capped at 52ch, row copy 40ch, FAQ answers 62ch.
- **Label** (500, 11px, 0.12em, uppercase): nav, announcement strip, form labels, table headers, footer headings. Minimum 11px.

### Named Rules
**The Caps Rule.** All display type is uppercase Big Shoulders at 900; mixed-case display never appears. Body and labels are never set in the display face except the centre-name input and list names.

## Layout

A `wrap` container capped at 1680px with a fluid gutter (16px to 40px). Sections use two-column splits (5fr/7fr for services and centres, 1fr/1fr for community and service detail) that collapse to one column at 900px (800px for splits and footer). The sticky 58px header sits on a Line hairline; the section head in the services list is sticky at 90px on desktop. Vertical rhythm is fluid: 56px to 120px for major sections. Product tiles sit in a 3-up grid with a 4px gap, one column under 700px.

## Elevation & Depth

Flat. No box-shadows exist. Depth comes from tonal fields (white, stone, black), full-bleed imagery under a black gradient, and the sticky header's hairline. The only response to state is colour change, an underline sweep or a small image scale.

### Named Rules
**The No-Shadow Rule.** Surfaces never lift. Hover is expressed by a sweep line, colour inversion or a 3.5% image zoom.

## Shapes

Square everywhere (0 radius). Hairline 1px borders define buttons, tags, list buttons and table rows; 2px orange sweep line on row hover; ink 1px rule on top of lists. Photographs fill their frames edge to edge (4:5 product tiles, cover-fit hero and split).

## Components

### Buttons
- **Shape:** square, 1px currentColor border, 12px/600 uppercase tracked label, padding 17px 26px, optional 16px arrow icon that slides 5px on hover.
- **Solid:** orange fill, ink text; hover turns white. Primary action on dark fields and campaign.
- **Ink:** ink fill, white text; hover turns orange.
- **Line:** transparent, currentColor border; hover inverts to ink (white on dark fields).
- **Focus:** 2px orange outline, 3px offset, on all elements.

### Navigation
Sticky white header, 58px, italic 900 wordmark with orange "91" accent, 11px uppercase tracked links, 1px underline that sweeps in from the left on hover and for current page. Under 900px the main nav and all but the last right-hand link are hidden. Preceded by a black announcement strip.

### Service rows (signature)
Large typographic rows replace cards: row title in display type, one-line copy in Muted, an arrow icon on the right; 1px Line rule between rows, Ink rule on top, an orange 2px underline sweeps across on hover or focus and the arrow moves 6px.

### Product tile
4:5 image, 4px gutter, a one-line uppercase meta row (name left, price right, no wrap), orange "new" badge top-left on the image.

### Centre finder
On black: underlined display-type input (no box), orange bottom border on focus, list of centres with a bordered action link that fills orange on hover.

### Warranty table and FAQ
Hairline table with 11px muted headers, display-face plan names and large tabular prices; collapses to stacked blocks under 800px. FAQ uses native details with display-face summaries and a plus that rotates 45 degrees.

## Do's and Don'ts

### Do:
- **Do** alternate white and black grounds section by section, with orange reserved for the action or status in each.
- **Do** set every headline, price and number in uppercase Big Shoulders 900 with line-height around 0.88 to 0.95.
- **Do** build lists as rows divided by 1px hairlines rather than as boxed items.
- **Do** keep corners square and depth flat.
- **Do** use HOLO Orange Ink for orange text on white or stone.
- **Do** keep a 2px orange focus outline with 3px offset.
- **Do** keep minimum text at 11px, with prefers-reduced-motion disabling the hero reveal and smooth scroll.

### Don't:
- **Don't** use border-radius, box-shadows or boxed cards.
- **Don't** introduce a second accent colour or tint a whole section orange.
- **Don't** use bright orange (#ff6a13) as small text on white.
- **Don't** set display type in mixed case or in the body face.
- **Don't** use ease curves other than the expo-out (cubic-bezier(.16,1,.3,1)) for reveal and sweep motion.
