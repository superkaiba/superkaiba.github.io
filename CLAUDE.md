# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a static personal website (GitHub Pages site) for an academic/research profile. It's a single-page design with a fixed sidebar and minimal, monochrome styling. The site is built with pure HTML/CSS/JS—no build process, frameworks, or dependencies.

## Architecture

**Single-Page Layout:**
- `index.html`: Single HTML file containing all content in one page
- Fixed sidebar navigation (`.sidebar`) on the left with name and external links
- Main content area (`.content`) on the right with profile, research, publications, and experience
- Fully responsive: sidebar becomes horizontal on mobile (<768px)

**Styling Philosophy:**
- Monochrome/grayscale aesthetic with Inter font family
- Profile image has `grayscale(100%)` filter applied
- Minimal borders and subtle hover effects
- All styling defined in a single `css/style.css` file organized by sections

**Key Layout Measurements:**
- Sidebar: Fixed 240px width, becomes full-width on mobile
- Content: Left margin of 240px (to account for sidebar), max-width 800px
- Profile image: 140px circular (120px on tablet, 100px on phone)

## Development Commands

**Local Testing:**
```bash
# Open in browser
open index.html

# Or run local server
python3 -m http.server 8000
# Then visit http://localhost:8000
```

**Git Operations:**
This is a `username.github.io` repository that deploys automatically to GitHub Pages from the master branch.

## Content Update Locations

When updating personal content in `index.html`:
- Line 6: Page title
- Line 7: Meta description
- Line 17: Site title (name in sidebar)
- Lines 20-24: External links (Resume, CV, Scholar, LinkedIn, GitHub)
- Line 34: Profile image path (stored in `assets/images/`)
- Lines 36-63: Main content (bio, research, publications, experience, contact)

**Asset Directories:**
- `assets/docs/`: PDF files (resume.pdf, cv.pdf)
- `assets/images/`: Profile picture (profile.jpg)

## Design System

**Color Palette:**
- `#000`: Primary text (headings, emphasis)
- `#333`: Body text
- `#555`: Secondary text
- `#666`: Link items
- `#888`: Section headings
- `#f0f0f0`: Borders
- `#ddd` / `#e0e0e0`: Underlines

**Typography:**
- Font: Inter (Google Fonts) with system fallbacks
- Weights: 300 (body), 400 (headings), 500 (strong/subheadings)
- Section headings: Uppercase with letter-spacing

**Responsive Breakpoints:**
- 768px: Sidebar becomes horizontal, profile stacks vertically
- 480px: Further padding reduction

## JavaScript

`js/script.js` is minimal—only updates footer year if a `#year` element exists (currently not in the HTML). The site has no interactive features or navigation logic since it's a single-page layout.
