# Repository guide

These instructions apply to Codex and other coding agents. The legacy filename is retained for existing references.

## Architecture

This is Thomas Jiralerspong’s static personal research website, deployed at https://thomas.jiralerspong.com/ using GitHub Pages. It uses HTML, CSS, and JavaScript without a framework or build step.

- `index.html` contains About, News, My research, and Mentorship. Mentored projects, Mentees, and Testimonials are subsections of Mentorship.
- `publications.html`, `mentorship.html`, `testimonials.html`, and `top5s.html` are standalone destinations with shared navigation.
- `css/style.css` contains all page styles.
- `js/script.js` handles theme selection, the phone contents menu, active-section highlighting, and hash navigation that expands containing disclosures.
- The earlier `data/cv-data.json`, `js/about-renderer.js`, and `js/cv-renderer.js` are retained as historical structured data and renderers, but are not loaded by the current pages. Edit the rendered HTML to change current content.

## Design and behavior

Use the existing monochrome palette and Space Grotesk typography. The left sidebar contains the portrait, Contents, Links, and a sun/moon theme control. It remains sticky above 540px and becomes a compact expandable bar on smaller screens. A sidebar taller than the viewport scrolls with the page until its bottom is visible; it must never create a separate scrollbar. The expanded phone menu uses the page scroll too.

Keep section headings and contents labels consistent. Show mentorship subsections as an indented nested list. Use descriptive underlined links and equal styling for Academic CV and 1 page resume. Recent items appear first, with native `<details>` controls for additional entries. Keep Thomas’s name emphasized in author lists and equal-contribution notes above the relevant projects.

Preserve descriptive link text, semantic headings, keyboard focus indicators, reduced-motion support, and disclosure navigation. Keep repeated sidebar links and content consistent across all pages.

Short paper descriptions must first explain what we study, investigate, or develop, then state the main findings and any essential qualification. Use one or two concise sentences grounded in the paper; include both the research context and the takeaway. Keep these descriptions consistent across the homepage (including expanded older projects), research and mentorship pages, and project image captions.

## Local verification

```bash
python3 -m http.server 8000
```

Check relevant desktop and phone layouts, light/dark themes, section jumps, disclosures, and local assets. Ensure no horizontal overflow or JavaScript errors. Use focused checks appropriate to the change. Keep temporary previews, screenshots, private research provenance, and logs outside this repository.

## CV and resume

- `assets/docs/cv.pdf` is the academic CV.
- `assets/docs/resume.pdf` is the one-page AI safety resume.
- `overleaf-resume/` is the Overleaf Git submodule containing their LaTeX sources.
- Active sources: `academic.tex` and `1_page_safety.tex`.
- Other variants include `1_page_phd.tex`, `1_page_founder.tex`, `1_page_games.tex`, `1_page_secret.tex`, `2_page.tex`, and publication/award lists.

**When modifying LaTeX sources, you MUST recompile PDFs and copy them:**

```bash
cd overleaf-resume
pdflatex 1_page_safety.tex && cp 1_page_safety.pdf ../assets/docs/resume.pdf
pdflatex academic.tex && cp academic.pdf ../assets/docs/cv.pdf
```

Run enough passes to resolve references, verify the resulting documents, and push the submodule commit before committing its new reference in the website repository. Do not expose credentials.

## Publishing

The `master` branch deploys through `.github/workflows/deploy.yml` to the existing GitHub Pages site. Publishing requires the user’s authorization; an explicit instruction to push or publish provides it. Preserve the current provider and custom domain.

Bump cache versions on all affected stylesheet, script, or PDF links. Preserve canonical URLs and the homepage Person structured data. Do not publish `noindex`, blocked preview robots rules, temporary preview pages, screenshots, or private provenance. Confirm the deployment workflow succeeds and verify the live site before reporting publication complete.
