# Thomas Jiralerspong’s website

Personal research website at https://thomas.jiralerspong.com/, hosted on GitHub Pages.

## Editing

The deployed pages are static HTML. The project catalogue is generated from Markdown; the other pages can be edited directly.

- `index.html`: introduction, news, research, mentored projects, mentees, and testimonials. Recent entries are visible; native `<details>` elements expand the rest.
- `publications.html`, `mentorship.html`, `testimonials.html`, and `top5s.html`: standalone pages with the same sidebar.
- `css/style.css`: responsive layout and light/dark styles.
- `js/script.js`: theme preference, mobile contents menu, active-section tracking, and links that reveal collapsed content.
- `assets/images/`: portrait, project figures, and film/TV covers.
- `assets/docs/cv.pdf` and `assets/docs/resume.pdf`: academic CV and one-page resume.
- `content/projects/*.md`: editable project proposals, compatible with Obsidian.
- `scripts/build_projects.py`: generates the catalogue at `projects/`. GitHub Actions runs this automatically before every deployment.

Edit the HTML directly and keep sidebar labels, shared profile links, and repeated content consistent across pages. The retained `data/cv-data.json`, `js/about-renderer.js`, and `js/cv-renderer.js` belong to the earlier dynamic layout; the current pages do not load them.

Use descriptive, visibly underlined links. Sidebar headings are stronger than navigation items, and mentorship subsections are indented under Mentorship. Keep CV and resume links identically styled.

## Local preview and checks

### Project catalogue

The permanent URL is https://thomas.jiralerspong.com/projects/. All proposals appear directly on that page. Individual projects have stable links based on their filenames, such as https://thomas.jiralerspong.com/projects/#self-reflection.

Edit the Markdown files in `content/projects/` to change proposals or statuses. Keep filenames stable to preserve shared links. Add a new Markdown file with `title` and `status` in its YAML frontmatter; the existing `id` field only controls ordering and is not displayed. Current status groups recognize `In progress`, `Follow-up`, and `Not started` prefixes.

Rebuild locally with:

```bash
uv run scripts/build_projects.py
```

Or install the pinned dependencies from `scripts/projects-requirements.txt` and run the script with Python. Pushing to `master` rebuilds the catalogue and deploys the same URL automatically. Obsidian can edit these files directly; syncing another device's vault remains a separate setup step.

The source of truth is `content/projects/`; avoid editing the generated HTML in `projects/`. Private mentee records, source-document snapshots, and message drafts stay in the separate research workspace.

### Preview the website

```bash
python3 -m http.server 8000
```

Open http://localhost:8000/. Check desktop and phone widths, section jumps, disclosure controls, the mobile menu, both color themes, and the two PDFs. Keep temporary screenshots and preview snapshots outside this repository.

When changing CSS, JavaScript, or PDFs, update their URL version parameters on all pages so returning visitors receive the new files.

## CV and resume sources

The `overleaf-resume/` submodule contains the LaTeX sources. The active documents are `academic.tex` and `1_page_safety.tex`. After changing either source, recompile it and copy its PDF into `assets/docs/`. Push the submodule commit before publishing its updated reference in this repository.

## Deployment

Pushing `master` triggers `.github/workflows/deploy.yml`, which deploys this repository to the existing GitHub Pages site. Confirm that the workflow succeeds and verify https://thomas.jiralerspong.com/ after publishing. Production pages must not include preview URLs or `noindex` directives.
