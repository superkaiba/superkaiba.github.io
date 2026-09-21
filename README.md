# Thomas Jiralerspong’s website

Personal research website at https://thomas.jiralerspong.com/, hosted on GitHub Pages.

## Editing

The deployed pages are static HTML. The project catalogue is generated from Markdown; the other pages can be edited directly.

- `index.html`: introduction, news, research, mentored projects, mentees, and testimonials. Recent entries are visible; native `<details>` elements expand the rest.
- `publications.html`, `mentorship.html`, `testimonials.html`, and `top5s.html`: standalone pages with the same sidebar.
- `css/style.css`: responsive layout and light/dark styles.
- `js/script.js`: theme preference, mobile contents menu, active-section tracking, and links that reveal collapsed content.
- `js/link-previews.js` and `css/link-previews.css`: hover and keyboard-focus cards for links inside blog post bodies only.
- `scripts/build_link_previews.py`: builds public link metadata and thumbnails in `assets/link-previews/`. It reads rendered public HTML, never local drafts or notes.
- `assets/images/`: portrait, project figures, and film/TV covers.
- `assets/docs/cv.pdf` and `assets/docs/resume.pdf`: academic CV and one-page resume.
- `content/projects/*.md`: editable project proposals, compatible with Obsidian.
- `scripts/build_projects.py`: generates the catalogue at `projects/`. GitHub Actions runs this automatically before every deployment.

Edit the HTML directly and keep sidebar labels, shared profile links, and repeated content consistent across pages. The retained `data/cv-data.json`, `js/about-renderer.js`, and `js/cv-renderer.js` belong to the earlier dynamic layout; the current pages do not load them.

Use descriptive, visibly underlined links. Sidebar headings are stronger than navigation items, and mentorship subsections are indented under Mentorship. Keep CV and resume links identically styled.

## Local preview and checks

### Project catalogue

The permanent URL is https://thomas.jiralerspong.com/projects/. All proposals appear directly on that page, with a scrolling table of contents matching the main site's navigation. The three sections are Not Started, In Progress, and Completed, in that order. Individual projects have stable links based on their filenames, such as https://thomas.jiralerspong.com/projects/#self-reflection.

Edit the Markdown files in `content/projects/` to change proposals or statuses. Keep filenames stable to preserve shared links. New files need `title`, `status`, and `order` in their YAML frontmatter. Supported statuses are exactly `Not started`, `In progress`, and `Completed`. The numeric `order` controls ordering within a status section. Unknown statuses fail the build rather than silently hiding a project.

Set `published: false` to retain a project in this source list while removing it from the website catalogue and its generated project pages. Omit the field or set `published: true` to publish it again.

Proposals should briefly explain relevant prior work with inline links, explain what would be useful to investigate, and list initial directions as bullets. Describe Thomas's existing findings in the first person, using “I have some results showing…” and preserving the supported scope of the result. An optional `aliases` list preserves older project names as both hash anchors and redirect pages when proposals are combined. Completed papers can use a retrospective summary and link to their follow-ups.

When referring to Affine Anticipation in proposal prose, link it as “My recent paper on linear context-answer relationships” and state the concrete finding: a learned linear map from the final context token's activation predicts the mean activation across answer tokens before generation. The completed project's title remains Affine Anticipation.

Rebuild locally with:

```bash
uv run scripts/build_projects.py
```

Or install the pinned dependencies from `scripts/projects-requirements.txt` and run the script with Python. Pushing to `master` rebuilds the catalogue and deploys the same URL automatically. Obsidian can edit these files directly; syncing another device's vault remains a separate setup step.

The source of truth is `content/projects/`; avoid editing the generated HTML in `projects/`. Private mentee records, source-document snapshots, and message drafts stay in the separate research workspace.

### Blog link previews

Hover over a link inside a blog post, or focus it with the keyboard, to see its destination title, description, and image when available. Previews are disabled on the homepage, blog archive, research pages, project catalogue, sidebars, and navigation. Blog links to internal sections preview the destination’s specific content. Escape dismisses a card. Moving onto the card keeps it open, and normal clicks and touch navigation are unchanged. Cards inherit the current light/dark theme.

Readers fetch only this site's static preview index and images. They do not contact an external preview service or the linked websites on hover. The build fetches public metadata without cookies or credentials, with bounded responses, validated public IP addresses, and raster-only thumbnails. Destinations that block previews fall back to their link label and address.

GitHub Actions rebuilds the preview index after the project catalogue, reusing cached external metadata. New external links are fetched automatically. To refresh existing external previews locally:

```bash
python3 -m pip install -r scripts/link-preview-requirements.txt
PYTHONDONTWRITEBYTECODE=1 python3 scripts/build_link_previews.py --refresh
```

Use `--offline` to update internal cards without network requests. Keep the preview script and stylesheet only on individual blog post templates, including the blog generator in the private publishing workspace. The script also restricts its listeners to `article.blog-body`. `data-no-preview` opts a link out.

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
