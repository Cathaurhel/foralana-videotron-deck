---
name: Luminous Milestone (Chapter 20)
colors:
  # Core Chapter 20 palette (as specified by the palette reference)
  elegant-black: '#1A1A1A'
  silver-chrome: '#E0E0E0'
  white-glow: '#FFFFFF'
  soft-gray: '#888888'
  deep-dark: '#1A1730'
  # Neon glow accents (used for borders, text glow, stars, lens flare)
  neon-pink: '#FF3EC9'
  neon-cyan: '#22E5FF'
  neon-purple: '#7B2FFF'
  neon-lime: '#D4FF00'
  # Material-role tokens (drive the Tailwind config in every slide's code.html)
  surface: '#1a1730'
  surface-dim: '#1a1730'
  surface-bright: '#2a2645'
  surface-container-lowest: '#100e1c'
  surface-container-low: '#1c1930'
  surface-container: '#201c38'
  surface-container-high: '#2a2548'
  surface-container-highest: '#342e58'
  on-surface: '#ffffff'
  on-surface-variant: '#e0e0e0'
  inverse-surface: '#ffffff'
  inverse-on-surface: '#1a1a1a'
  outline: '#888888'
  outline-variant: '#3a3560'
  surface-tint: '#22e5ff'
  primary: '#22e5ff'
  on-primary: '#0a1a1f'
  primary-container: '#100e1c'
  on-primary-container: '#22e5ff'
  inverse-primary: '#7b2fff'
  secondary: '#ff3ec9'
  on-secondary: '#2e0a24'
  secondary-container: '#4a1240'
  on-secondary-container: '#ff9fe3'
  tertiary: '#d4ff00'
  on-tertiary: '#1a1f00'
  tertiary-container: '#1a1a1a'
  on-tertiary-container: '#d4ff00'
  error: '#ff6b6b'
  on-error: '#2a0000'
  error-container: '#7a0010'
  on-error-container: '#ffd6d6'
  primary-fixed: '#b8f5ff'
  primary-fixed-dim: '#22e5ff'
  on-primary-fixed: '#071a1d'
  on-primary-fixed-variant: '#0f3a40'
  secondary-fixed: '#ffd6f3'
  secondary-fixed-dim: '#ff3ec9'
  on-secondary-fixed: '#3a0a30'
  on-secondary-fixed-variant: '#7a1f66'
  tertiary-fixed: '#f1ffa8'
  tertiary-fixed-dim: '#d4ff00'
  on-tertiary-fixed: '#1f2400'
  on-tertiary-fixed-variant: '#3a4200'
  background: '#1a1730'
  on-background: '#ffffff'
  surface-variant: '#342e58'
typography:
  display-lg:
    fontFamily: Montserrat
    fontSize: 80px
    fontWeight: '900'
    lineHeight: 96px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '900'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
  headline-lg:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  accent-serif:
    fontFamily: EB Garamond
    fontSize: 24px
    fontWeight: '400'
    lineHeight: 32px
  body-lg:
    fontFamily: Montserrat
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Montserrat
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: Montserrat
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 20px
  margin-desktop: 64px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 64px
---

## Brand & Style

The design system is a high-end, cinematic **Chapter 20** framework designed for a celebratory digital experience. It bridges the gap between early-2000s cyber-glam and high-production motion graphics. The personality is **sophisticated, atmospheric, and celebratory**, evoking the feeling of a premium night-time event or a high-profile "videotron" showcase — filtered through a chrome-and-neon Chapter 20 lens.

The visual style is **Elegant Dark Mode with Chapter 20 Neon Glow**. It utilizes deep black-navy space to create infinite depth, punctuated by vibrant neon pink, cyan, lime, and purple light leaks, soft lens flares, and glossy chrome frames. It leans into a **Modern-Corporate** structure but breaks formality with **Glassmorphic** layers, glowing star/sparkle motifs, and high-fashion typography.

**Key Aesthetic Principles:**
- **Cinematic Depth:** Use of deep shadows and light overlays to create a 3D sense of space.
- **Radiant Neon Accents:** Interactive elements should feel like they are emitting light — pink, cyan, lime, or purple — not just colored.
- **Chrome & Glossy Surfaces:** Borders and frames pick up a metallic, glass-like highlight, referencing Chapter 20 chrome/bubble aesthetics.
- **Editorial Precision:** Large-scale headings paired with delicate serif accents for a "milestone" look.

## Colors

The palette is rooted in the "Deep Dark" navy-black base to ensure maximum contrast for the neon glow effects.

- **Elegant Black (#1A1A1A):** Card and container fills, floating above the Deep Dark canvas.
- **Silver Chrome (#E0E0E0):** Secondary text, metadata, chrome/glossy surface highlights.
- **White Glow (#FFFFFF):** Reserved for primary text and high-impact highlights.
- **Soft Gray (#888888):** Used for outlines, inactive states, and tertiary metadata.
- **Deep Dark (#1A1730):** The primary canvas / page background — a near-black with a hint of navy-violet.
- **Neon Pink (#FF3EC9):** Primary interactive/glow accent — "secondary" role. Used the most: active nav states, glow text, lens flares.
- **Neon Cyan (#22E5FF):** Primary accent — "primary" role. Used for chips, badges, primary glow borders, dark-mode/UI accents.
- **Neon Lime (#D4FF00):** Tertiary accent. Used for stars/sparkles, highlight glows, and "glow stars" decorative elements.
- **Neon Purple (#7B2FFF):** Inverse/atmospheric accent. Used for background glow gradients and serif/editorial highlights.

Color application should favor high-contrast text (White Glow / Silver Chrome) against the Deep Dark canvas, using the four neon accents as "backlights" — glowing borders, drop-shadows, and dot/star indicators — rather than large solid fills.

## Typography

The typography strategy focuses on scale and contrast between a bold, geometric sans-serif and a delicate, historical serif.

- **Headlines (Montserrat):** Should be treated with high weight (Bold/Black). For display levels, apply a subtle "Chrome" gradient (White to Soft Gray) or an outer glow (0 0 10px Primary Secondary).
- **Accents (EB Garamond):** Used for "Elegant Details" such as quotes, section sub-headers, or dates. This font should always be used sparingly to maintain its premium impact.
- **Body (Montserrat):** Kept clean and legible. Use wider line-heights to compensate for light-on-dark reading fatigue.
- **Labels:** Use uppercase with increased letter spacing for a technical, "data-display" feel.

## Layout & Spacing

This design system uses a **Fluid Grid** model with generous margins to mimic the wide-screen cinematic experience.

- **Breakpoints:** Mobile (<768px), Tablet (768px - 1024px), Desktop (>1024px).
- **Grid:** A 12-column grid for desktop with 24px gutters. On mobile, transition to a 4-column grid.
- **Vertical Rhythm:** Spacing is defined in multiples of 8px. Large sections (Milestones) should be separated by `stack-lg` to create a sense of breathing room and focus.
- **Safe Areas:** Elements like lens flares and glow effects should bleed into the margins to create an immersive, uncontained feel, while core text stays strictly within the grid.

## Elevation & Depth

Elevation is achieved through **light and translucency** rather than traditional drop shadows.

- **Background Layers:** The base is #1A1730 (Deep Dark). Use "Atmospheric Glows" (Radial gradients of #7B2FFF Neon Purple at 20% opacity) to suggest light sources behind the content.
- **Glassmorphism:** Foreground containers use a semi-transparent background (White at 5% opacity) with a `backdrop-filter: blur(20px)`.
- **Glossy Frames:** Components use a 1px solid border with a linear gradient (White 30%, Transparent 70%) to create a "chrome rim" effect.
- **Interactive Depth:** When an element is hovered or active, increase the `box-shadow` using a vibrant neon glow matched to that element's accent — Neon Pink `0 0 20px rgba(255,62,201,0.5)`, Neon Cyan `rgba(34,229,255,0.5)`, Neon Lime `rgba(212,255,0,0.5)`, or Neon Purple `rgba(123,47,255,0.5)`.
- **Star / Sparkle Motifs:** Small `auto_awesome`-style sparkle glyphs in Neon Lime or White Glow, often with a subtle pulse animation, reinforce the Chapter 20 "glow stars" motif near titles and section badges.

## Shapes

The shape language is **Soft yet Structured**. 

- **Base Radius:** 4px (Soft) for most components to maintain a professional, architectural feel. 
- **Milestone Cards:** Use `rounded-lg` (8px) to distinguish them as focal points.
- **Interactive Elements:** Buttons can use `rounded-xl` (12px) or Pill-shaped settings to feel more approachable and modern.
- **Framing:** Use thin, high-contrast strokes (1px) for borders to mimic the look of a premium screen or glass frame.

## Components

### Buttons
- **Primary:** Solid White Glow text on a Dark background with a persistent "Chrome" border. On hover, a Neon Pink or Neon Cyan outer glow activates.
- **Ghost:** Transparent background with a 1px Soft Gray border.

### Milestone Cards (Frame Glossy)
- These are the centerpiece. Use the Glassmorphism effect with a 1px top-left highlight border.
- Include a subtle "Lens Flare" SVG element positioned in the corner of the card to break the geometric frame.

### Chapter 20 Glow Cards
- Cards use a 2px border in one of the four neon accents (rotate pink → cyan → lime → purple across a grid) with a matching soft outer glow (`box-shadow`) and inner glow.
- Card titles are set in the matching accent color with a short text drop-shadow glow; a small solid-color dot (same accent) sits to the left of the title as a bullet/indicator.

### Chips & Tags
- Use the Secondary-container color (#4A1240, deep magenta) as a low-opacity background fill with White Glow text for labels; badge/pill chips use a thin Neon Cyan border with a small glowing dot.

### Input Fields
- Dark backgrounds (#000) with a Soft Gray bottom-border only. On focus, the border transitions to a Neon Purple glow.

### Lists
- Milestone lists should feature large numbers (Montserrat Black) in the Secondary (Neon Pink) color, acting as a background element for the list item text.

### Interactive "Glow" Points
- Small circular elements that pulse with Neon Pink/Cyan/Lime/Purple to indicate "hotspots," milestones in a timeline, or moodboard palette bullets.