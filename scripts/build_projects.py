# /// script
# requires-python = ">=3.10"
# dependencies = ["markdown>=3.7,<4", "PyYAML>=6,<7"]
# ///
"""Render the editable Markdown proposals as the public project catalogue."""
from hashlib import sha256
from html import escape
from pathlib import Path
import re
import markdown
import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "projects"
DEST = ROOT / "projects"
HOME_URL = "https://thomas.jiralerspong.com/"
GROUPS = [("Not Started", "not-started"), ("In Progress", "in-progress"), ("Completed", "completed")]

CSS = """
.project-layout{grid-template-columns:230px minmax(0,1fr);gap:48px}
.project-layout>.contents{position:sticky;top:32px;max-height:calc(100dvh - 64px);overflow-y:auto;overscroll-behavior:contain;scrollbar-width:thin;padding-right:10px}
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
.project-row h3{font-size:21px;line-height:1.45;margin:0 0 18px}
.project-row h3 a{text-decoration:none}
.project-row h3 a:hover{text-decoration:underline}
.project-reading p{font-size:16px;line-height:1.8;margin:16px 0}
.project-reading ul{padding-left:24px;margin:16px 0}
.project-reading li{margin:9px 0;overflow-wrap:anywhere;line-height:1.8}
.project-reading a{overflow-wrap:anywhere}
.project-empty{font-size:15px;color:var(--muted);padding-top:8px}
.project-catalogue footer{display:block;margin-top:44px}
@media(min-width:541px) and (max-width:900px){
 .project-layout{grid-template-columns:180px minmax(0,1fr);gap:28px}
 .project-layout>.contents{top:24px;max-height:calc(100dvh - 48px)}
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
 .has-js .project-layout .contents[data-expanded="true"]{position:sticky}
 .has-js .project-layout .contents[data-expanded="true"] .sidebar-panel{display:block;max-height:calc(100dvh - 150px);overflow-y:auto;padding:16px 0 8px}
 .project-layout .contents nav{max-height:none;overflow:visible}
 .project-layout .contents .toc-subsections .toc-child>a{min-height:40px;padding-top:10px;padding-bottom:10px}
 .project-catalogue h1{font-size:28px;margin-bottom:30px}
 .project-group>h2{font-size:23px}
 .project-row h3{font-size:20px}
 .project-row,.project-group{scroll-margin-top:126px}
}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
"""

JS = """
// Keep the active entry visible within the long desktop table of contents.
const projectContents = document.querySelector('.project-layout > .contents');
const projectNav = projectContents?.querySelector('nav');
function keepCurrentProjectVisible(){
 if(!projectContents || innerWidth <= 540) return;
 const current = projectNav.querySelector('[aria-current="location"]');
 if(!current) return;
 const outer = projectContents.getBoundingClientRect();
 const entry = current.getBoundingClientRect();
 if(entry.top < outer.top + 20) projectContents.scrollTop += entry.top - outer.top - 20;
 else if(entry.bottom > outer.bottom - 20) projectContents.scrollTop += entry.bottom - outer.bottom + 20;
}
if(projectNav){
 new MutationObserver(keepCurrentProjectVisible).observe(projectNav,{subtree:true,attributes:true,attributeFilter:['aria-current']});
}
"""

def group_for(status):
    status = status.lower()
    if status.startswith(("not started", "follow-up")):
        return "not-started"
    if status.startswith("in progress"):
        return "in-progress"
    if status.startswith(("completed", "done")):
        return "completed"
    raise ValueError(f"Unsupported project status: {status!r}")

def theme_button():
    return '''<button id="theme-toggle" class="theme-toggle" type="button" aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode"><svg class="theme-moon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.8 13A9 9 0 0 1 11 3.2 9 9 0 1 0 20.8 13Z"/></svg><svg class="theme-sun" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M4.93 4.93l1.42 1.42m11.3 11.3 1.42 1.42M4.93 19.07l1.42-1.42m11.3-11.3 1.42-1.42"/></svg></button>'''

def render_page(body, toc, versions):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Research projects · Thomas Jiralerspong</title>
<link rel="canonical" href="{HOME_URL}projects/">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="base.css?v={versions['base.css']}"><link rel="stylesheet" href="catalogue.css?v={versions['catalogue.css']}">
<script>try{{document.documentElement.dataset.theme=localStorage.getItem('theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light')}}catch{{}}</script>
</head><body><a class="skip-link" href="#main">Skip to content</a>
<div class="page-layout project-layout">
<aside class="contents">
<div class="project-sidebar-heading"><a href="{HOME_URL}">Thomas Jiralerspong</a>{theme_button()}</div>
<button type="button" class="contents-toggle" aria-expanded="false" aria-controls="project-sidebar-panel">Contents <span class="current-section">Not Started</span><span class="contents-indicator" aria-hidden="true">+</span></button>
<div class="sidebar-panel" id="project-sidebar-panel"><nav aria-labelledby="contents-heading"><h2 class="sidebar-label" id="contents-heading">Projects</h2><ol>{toc}</ol></nav></div>
</aside><div class="site-wrap"><main class="project-catalogue" id="main">
<h1>Research projects</h1>{body}
<footer><a href="{HOME_URL}">Main website</a></footer>
</main></div></div><script src="navigation.js?v={versions['navigation.js']}"></script><script src="catalogue.js?v={versions['catalogue.js']}"></script>
</body></html>'''

def main():
    projects = []
    for path in sorted(CONTENT.glob("*.md")):
        _, front, body = path.read_text().split("---", 2)
        meta = yaml.safe_load(front)
        rendered = markdown.markdown(body, extensions=["sane_lists"])
        rendered = re.sub(r"<h1>.*?</h1>", "", rendered, count=1, flags=re.S)
        meta.update(slug=path.stem, rendered=rendered, body=body, group=group_for(meta["status"]))
        projects.append(meta)
    projects.sort(key=lambda p:(p.get("id", "zz"), p["title"].lower()))
    DEST.mkdir(parents=True, exist_ok=True)
    assets = {
        "base.css": (ROOT / "css/style.css").read_text(),
        "navigation.js": (ROOT / "js/script.js").read_text(),
        "catalogue.css": CSS,
        "catalogue.js": JS,
    }
    versions = {}
    for name, content in assets.items():
        (DEST / name).write_text(content)
        versions[name] = sha256(content.encode()).hexdigest()[:12]
    body, toc = "", ""
    for title, key in GROUPS:
        rows = [p for p in projects if p["group"] == key]
        body += f'<section class="project-group toc-section" id="{key}"><h2>{title}</h2>'
        toc += f'<li class="toc-parent"><a href="#{key}" data-section="{key}">{title}</a>'
        if rows:
            toc += '<ol class="toc-subsections">'
        else:
            body += '<p class="project-empty">No projects marked completed yet.</p>' if key == "completed" else '<p class="project-empty">No projects listed.</p>'
        for p in rows:
            slug, name = p["slug"], escape(p["title"])
            toc += f'<li class="toc-child"><a href="#{slug}" data-section="{slug}">{name}</a></li>'
            body += f'<article class="project-row toc-section" id="{slug}"><h3><a href="#{slug}">{name}</a></h3><div class="project-reading">{p["rendered"]}</div></article>'
            target = DEST / slug
            target.mkdir(exist_ok=True)
            (target / "index.html").write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0;url=../#{slug}"><title>{name} · Thomas Jiralerspong</title><link rel="canonical" href="{HOME_URL}projects/"></head><body><p><a href="../#{slug}">{name}</a></p></body></html>\n')
            (target / "note.md").write_text(p["body"].strip() + "\n")
        body += "</section>"
        if rows:
            toc += "</ol>"
        toc += "</li>"
    (DEST / "index.html").write_text(render_page(body, toc, versions))
    print(f"Rendered {len(projects)} projects with a scrolling table of contents at {DEST}")

if __name__ == "__main__":
    main()
