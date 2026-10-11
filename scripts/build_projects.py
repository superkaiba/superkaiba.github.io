# /// script
# requires-python = ">=3.10"
# dependencies = ["markdown>=3.7,<4", "PyYAML>=6,<7", "python-markdown-math==0.9", "latex2mathml==3.81.1"]
# ///
"""Render the editable Markdown proposals as the public project catalogue."""
from hashlib import sha256
from html import escape
from pathlib import Path
import re
import markdown
import yaml
from latex2mathml.converter import convert as latex_to_mathml

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "projects"
DEST = ROOT / "projects"
HOME_URL = "https://thomas.jiralerspong.com/"
GROUPS = [
    ("Not Started", "not-started"),
    ("In Progress", "in-progress"),
    ("Completed", "completed"),
]
STATUSES = {"Not started": 0, "In progress": 1, "Completed": 2}

CSS = """
.project-layout{grid-template-columns:230px minmax(0,1fr);gap:48px}
.project-layout>.contents{--sidebar-offset:32px;position:sticky;top:var(--sidebar-sticky-top,32px);max-height:none;overflow:visible;padding-right:10px}
.project-sidebar-heading{display:flex;gap:10px;align-items:center;justify-content:space-between;margin-bottom:28px}
.project-sidebar-heading>a{font-size:13px;text-decoration:none}
.project-layout .contents #theme-toggle{margin:0;flex-shrink:0}
.project-layout .sidebar-panel{display:block}
.project-layout .contents .sidebar-label{margin:0 0 12px}
.project-layout .contents .toc-subsections{margin:4px 0 16px 12px}
.project-layout .contents .toc-subsections .toc-child>a{font-size:12px;line-height:1.5;font-weight:400;padding:6px 0 6px 12px}
.project-layout .contents .toc-subsections a[aria-current="location"]{font-weight:600}
.project-layout .contents .toc-parent>a{font-size:14px;padding:8px 0 8px 14px}
.project-catalogue{min-width:0}
.project-catalogue h1{font-size:32px;margin:0 0 36px;line-height:1.25}
.project-group{margin-top:44px;scroll-margin-top:28px}
.project-group:first-of-type{margin-top:0}
.project-group>h2{font-size:25px;margin:0 0 18px}
.project-row{padding:28px 0;border-top:1px solid var(--line);scroll-margin-top:28px}
.project-row h3{font-size:21px;line-height:1.45;margin:0 0 6px}
.project-status{font-size:13px;color:var(--muted);margin:0 0 18px}
.project-alias{display:block;height:0;scroll-margin-top:28px}
.project-row h3 a{text-decoration:none}
.project-row h3 a:hover{text-decoration:underline}
.project-reading p{font-size:16px;line-height:1.8;margin:16px 0}
.project-reading ul{padding-left:24px;margin:16px 0}
.project-reading li{margin:9px 0;overflow-wrap:anywhere;line-height:1.8}
.project-reading a{overflow-wrap:anywhere}
.project-reading math{font-size:1.05em}
.project-equation{display:block;max-width:100%;overflow-x:auto;padding:8px 2px}
.project-equation math{width:max-content;min-width:100%}
.project-empty{font-size:15px;color:var(--muted);padding-top:8px}
.project-catalogue footer{display:block;margin-top:44px}
.project-detail-layout .project-catalogue h1{margin-bottom:12px;overflow-wrap:anywhere}
.project-back{font-size:14px;margin:0 0 24px}
@media(min-width:541px) and (max-width:900px){
 .project-layout{grid-template-columns:180px minmax(0,1fr);gap:28px}
 .project-layout>.contents{--sidebar-offset:24px}
 .project-sidebar-heading{display:block}
 .project-sidebar-heading>a{display:block;margin-bottom:10px}
}
@media(max-width:540px){
 .project-layout{display:block;padding:24px 22px 44px}
 .project-layout>.contents{display:block;top:0;margin:-24px -22px 28px;padding:12px 22px;max-height:none;overflow:visible;background:var(--bg)}
 .project-sidebar-heading{display:flex;margin:0 0 6px}
 .project-layout .contents-toggle{grid-column:auto;grid-row:auto}
 .project-layout .current-section{max-width:45%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
 .project-layout .sidebar-panel{display:block}
 .has-js .project-layout .sidebar-panel{display:none}
 .has-js .project-layout .contents[data-expanded="true"]{position:relative}
 .has-js .project-layout .contents[data-expanded="true"] .sidebar-panel{display:block;max-height:none;overflow:visible;padding:16px 0 8px}
 .project-layout .contents nav{max-height:none;overflow:visible}
 .project-layout .contents .toc-subsections .toc-child>a{min-height:40px;padding-top:10px;padding-bottom:10px}
 .project-catalogue h1{font-size:28px;margin-bottom:30px}
 .project-group>h2{font-size:23px}
 .project-row h3{font-size:20px}
 .project-row,.project-group,.project-alias{scroll-margin-top:126px}
}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
"""

def theme_button():
    return '''<button id="theme-toggle" class="theme-toggle" type="button" aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode"><svg class="theme-moon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.8 13A9 9 0 0 1 11 3.2 9 9 0 1 0 20.8 13Z"/></svg><svg class="theme-sun" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M4.93 4.93l1.42 1.42m11.3 11.3 1.42 1.42M4.93 19.07l1.42-1.42m11.3-11.3 1.42-1.42"/></svg></button>'''

def render_page(body, toc, versions, project=None):
    title = escape(project["title"]) if project else "Research projects"
    canonical = f'{HOME_URL}projects/{project["slug"]}/' if project else f'{HOME_URL}projects/'
    prefix = "../" if project else ""
    layout = " project-detail-layout" if project else ""
    current_section = "Overview" if project else "Not Started"
    heading = '<p class="project-back"><a href="../">← All projects</a></p>' if project else '<h1>Research projects</h1>'
    footer = f'<a href="../">All projects</a> · <a href="../#{project["slug"]}">View in catalogue</a>' if project else f'<a href="{HOME_URL}">Main website</a>'
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · Thomas Jiralerspong</title>
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title} · Thomas Jiralerspong"><meta property="og:url" content="{canonical}"><meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}base.css?v={versions['base.css']}"><link rel="stylesheet" href="{prefix}catalogue.css?v={versions['catalogue.css']}">
<script>try{{document.documentElement.dataset.theme=localStorage.getItem('theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light')}}catch{{}}</script>
</head><body><a class="skip-link" href="#main">Skip to content</a>
<div class="page-layout project-layout{layout}">
<aside class="contents">
<div class="project-sidebar-heading"><a href="{HOME_URL}">Thomas Jiralerspong</a>{theme_button()}</div>
<button type="button" class="contents-toggle" aria-expanded="false" aria-controls="project-sidebar-panel">Contents <span class="current-section">{current_section}</span><span class="contents-indicator" aria-hidden="true">+</span></button>
<div class="sidebar-panel" id="project-sidebar-panel"><nav aria-labelledby="contents-heading"><h2 class="sidebar-label" id="contents-heading">Projects</h2><ol>{toc}</ol></nav></div>
</aside><div class="site-wrap"><main class="project-catalogue" id="main">
{heading}{body}
<footer>{footer}</footer>
</main></div></div><script src="{prefix}navigation.js?v={versions['navigation.js']}"></script>
</body></html>'''


def standalone_links(rendered, project_targets, current_slug):
    """Keep local anchors local, and send related-project links to their pages."""
    def replace(match):
        target = project_targets.get(match.group(1))
        if target is None or target == current_slug:
            return match.group(0)
        return f'href="../{target}/"'

    return re.sub(r'href="#([^"]+)"', replace, rendered)


def render_project_page(project, versions, project_targets):
    slug, title = project["slug"], escape(project["title"])
    aliases = ''.join(f'<span class="project-alias" id="{alias}" aria-hidden="true"></span>' for alias in project.get("aliases", []))
    content = standalone_links(project["rendered"], project_targets, slug)
    body = f'<article class="project-detail toc-section" id="{slug}">{aliases}<h1>{title}</h1><p class="project-status">{escape(project["status"])}</p><div class="project-reading">{content}</div></article>'
    toc = f'<li><a href="../">All projects</a></li><li><a href="#{slug}" data-section="{slug}">Overview</a></li>'
    return render_page(body, toc, versions, project=project)


def render_project_redirect(project):
    slug, title = project["slug"], escape(project["title"])
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0;url=../{slug}/"><title>{title} · Thomas Jiralerspong</title><link rel="canonical" href="{HOME_URL}projects/{slug}/"></head><body><p><a href="../{slug}/">{title}</a></p></body></html>\n'


def render_markdown(body, math_enabled=False):
    extensions = ["sane_lists"]
    if math_enabled:
        extensions.append("mdx_math")
    rendered = markdown.markdown(
        body, extensions=extensions,
        extension_configs={"mdx_math": {"enable_dollar_delimiter": True}},
    )
    if math_enabled:
        def render_equation(match):
            display = bool(match.group("display"))
            mathml = latex_to_mathml(
                match.group("tex").strip(), display="block" if display else "inline"
            )
            return f'<span class="project-equation">{mathml}</span>' if display else mathml

        rendered = re.sub(
            r'<script type="math/tex(?P<display>; mode=display)?">(?P<tex>.*?)</script>',
            render_equation, rendered, flags=re.S,
        )
    return rendered


def main():
    projects = []
    for path in sorted(CONTENT.glob("*.md")):
        _, front, body = path.read_text().split("---", 2)
        meta = yaml.safe_load(front)
        if not isinstance(meta.get("math", False), bool):
            raise ValueError(f"The math field in {path.name} must be true or false")
        rendered = render_markdown(body, math_enabled=meta.get("math", False))
        rendered = re.sub(r"<h1>.*?</h1>", "", rendered, count=1, flags=re.S)
        if meta["status"] not in STATUSES:
            raise ValueError(f"Unsupported status in {path.name}: {meta['status']!r}")
        if not isinstance(meta.get("published", True), bool):
            raise ValueError(f"The published field in {path.name} must be true or false")
        meta.update(slug=path.stem, rendered=rendered, body=body)
        projects.append(meta)
    projects.sort(key=lambda p:(STATUSES[p["status"]], p.get("order", 999), p["title"].lower()))
    # Validate all public anchors before writing files, including historical names.
    anchors = {key for _, key in GROUPS} | {"main"}
    for p in projects:
        for slug in [p["slug"], *p.get("aliases", [])]:
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug) or slug in anchors:
                raise ValueError(f"Invalid or duplicate project anchor: {slug!r}")
            anchors.add(slug)
    unpublished = [p for p in projects if not p.get("published", True)]
    projects = [p for p in projects if p.get("published", True)]
    project_targets = {slug: p["slug"] for p in projects for slug in [p["slug"], *p.get("aliases", [])]}
    # Keep unpublished proposals editable, but remove their generated pages.
    for p in unpublished:
        for slug in [p["slug"], *p.get("aliases", [])]:
            for name in ("index.html", "note.md"):
                (DEST / slug / name).unlink(missing_ok=True)
    DEST.mkdir(parents=True, exist_ok=True)
    assets = {
        "base.css": (ROOT / "css/style.css").read_text(),
        "navigation.js": (ROOT / "js/script.js").read_text(),
        "catalogue.css": CSS,
    }
    versions = {}
    for name, content in assets.items():
        (DEST / name).write_text(content)
        versions[name] = sha256(content.encode()).hexdigest()[:12]
    # Navigation now uses the same page-scrolling sidebar as the main website.
    (DEST / "catalogue.js").unlink(missing_ok=True)
    body, toc = "", ""
    for title, key in GROUPS:
        rows = [p for p in projects if p["status"].lower().replace(" ", "-") == key]
        body += f'<section class="project-group toc-section" id="{key}"><h2>{title}</h2>'
        toc += f'<li class="toc-parent"><a href="#{key}" data-section="{key}">{title}</a>'
        if rows:
            toc += '<ol class="toc-subsections">'
        else:
            body += '<p class="project-empty">No projects marked completed yet.</p>' if key == "completed" else '<p class="project-empty">No projects listed.</p>'
        for p in rows:
            slug, name = p["slug"], escape(p["title"])
            toc += f'<li class="toc-child"><a href="#{slug}" data-section="{slug}">{name}</a></li>'
            aliases = list(p.get("aliases", []))
            alias_html = ''.join(f'<span class="project-alias" id="{alias}" aria-hidden="true"></span>' for alias in aliases)
            body += f'<article class="project-row toc-section" id="{slug}">{alias_html}<h3><a href="{slug}/">{name}</a></h3><p class="project-status">{escape(p["status"])}</p><div class="project-reading">{p["rendered"]}</div></article>'
            for path_slug in [slug, *p.get("aliases", [])]:
                target = DEST / path_slug
                target.mkdir(exist_ok=True)
                page = render_project_page(p, versions, project_targets) if path_slug == slug else render_project_redirect(p)
                (target / "index.html").write_text(page)
                (target / "note.md").write_text(p["body"].strip() + "\n")
        body += "</section>"
        if rows:
            toc += "</ol>"
        toc += "</li>"
    (DEST / "index.html").write_text(render_page(body, toc, versions))
    print(f"Rendered {len(projects)} projects at {DEST}; retained {len(unpublished)} unpublished proposals in {CONTENT}")

if __name__ == "__main__":
    main()
