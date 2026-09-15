# /// script
# requires-python = ">=3.10"
# dependencies = ["markdown>=3.7,<4", "PyYAML>=6,<7"]
# ///
"""Render the editable project notes into a static website directory."""
from html import escape
from pathlib import Path
import re
import shutil
import markdown
import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "projects"
DEST = ROOT / "projects"
WEBSITE = ROOT
ADVICE = "https://docs.google.com/document/d/1fU_nU4tQ_PxdVZ3fnls4tEby2015m_45Um3uQSxEDkU/edit"
PST_BOOKING = "https://calendar.app.google/zR1Yk1Z4sVsHrBob8"
NON_PST_BOOKING = "https://calendar.app.google/Rha6wPfEM5zcxNeaA"

CSS = '''
.catalogue{max-width:880px;margin:auto;padding:28px 32px 64px}
.catalogue-header{display:flex;justify-content:space-between;align-items:center;gap:24px;margin-bottom:44px}
.catalogue-header button{border:1px solid var(--line);background:var(--bg);padding:6px 12px;border-radius:4px}
.catalogue h1{font-size:32px;line-height:1.25;margin-bottom:20px}
.catalogue h2{margin:44px 0 16px;font-size:25px}
.catalogue h3{font-size:21px;line-height:1.45;margin-bottom:18px}
.catalogue h3 a{text-decoration:none}
.catalogue h3 a:hover{text-decoration:underline}
.catalogue p{margin:12px 0;max-width:76ch}
.catalogue .meta{font-size:13px;color:var(--muted)}
.catalogue .filters{display:flex;gap:20px;margin:30px 0;align-items:end}
.catalogue .filters label{display:block;font-size:14px;flex:1}
.catalogue input,.catalogue select{display:block;width:100%;margin-top:8px;padding:10px 12px;background:var(--bg);color:var(--text);border:1px solid var(--line);border-radius:4px;font:inherit}
.catalogue input:focus-visible,.catalogue select:focus-visible{outline:2px solid var(--focus);outline-offset:3px}
.project-row{padding:30px 0;border-top:1px solid var(--line);scroll-margin-top:28px}
.project-row p{font-size:16px;margin:16px 0;line-height:1.8}
.project-reading ul{padding-left:24px;margin:16px 0}
.project-reading li{margin:9px 0;overflow-wrap:anywhere;line-height:1.8}
.catalogue .onboarding{margin:24px 0 0}
.catalogue .onboarding li{margin:8px 0}
.catalogue .booking-duration{font-size:14px;color:var(--muted)}
.catalogue [hidden]{display:none!important}
.catalogue footer{display:block;margin-top:40px}
@media(max-width:540px){.catalogue{padding:22px 22px 44px}.catalogue-header{margin-bottom:30px;font-size:14px}.catalogue h1{font-size:27px}.catalogue .filters{display:block}.catalogue .filters label+label{margin-top:16px}}
'''

JS = '''
const theme=document.querySelector('#theme');
theme.textContent=document.documentElement.dataset.theme==='dark'?'Light mode':'Dark mode';
theme.addEventListener('click',()=>{
 const next=document.documentElement.dataset.theme==='dark'?'light':'dark';
 document.documentElement.dataset.theme=next;
 theme.textContent=next==='dark'?'Light mode':'Dark mode';
 try{localStorage.setItem('research-project-theme',next)}catch{}
});
const query=document.querySelector('#search'),status=document.querySelector('#status');
if(query&&status){
 const rows=[...document.querySelectorAll('.project-row')];
 function filter(){
  const value=query.value.trim().toLowerCase();
  rows.forEach(row=>row.hidden=!(row.textContent.toLowerCase().includes(value)&&(!status.value||row.dataset.status===status.value)));
  document.querySelectorAll('.project-group').forEach(group=>group.hidden=![...group.querySelectorAll('.project-row')].some(row=>!row.hidden));
  const count=rows.filter(row=>!row.hidden).length;
  document.querySelector('#count').textContent=count+' project'+(count===1?'':'s');
  document.querySelector('#empty').hidden=count!==0;
 }
 query.addEventListener('input',filter);status.addEventListener('change',filter);
 function revealHash(){
  const target=document.getElementById(decodeURIComponent(location.hash.slice(1)));
  if(target&&target.classList.contains('project-row')){
   query.value='';status.value='';filter();target.scrollIntoView();
  }
 }
 window.addEventListener('hashchange',revealHash);revealHash();
}
'''

def page(title, body, prefix=""):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)} · Thomas Jiralerspong</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}base.css"><link rel="stylesheet" href="{prefix}catalogue.css?v=2">
<script>try{{document.documentElement.dataset.theme=localStorage.getItem('research-project-theme')||'light'}}catch{{}}</script>
</head><body><a class="skip-link" href="#main">Skip to content</a><div class="catalogue">
<header class="catalogue-header"><a href="https://thomas.jiralerspong.com/">Thomas Jiralerspong</a><button id="theme" type="button">Toggle theme</button></header>
<main id="main">{body}</main><footer><a href="{ADVICE}">Advice for mentees</a> · <a href="https://thomas.jiralerspong.com/">Main website</a></footer>
</div><script src="{prefix}catalogue.js?v=2"></script></body></html>'''

def main():
    DEST.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(WEBSITE / "css/style.css", DEST / "base.css")
    (DEST / "catalogue.css").write_text(CSS)
    (DEST / "catalogue.js").write_text(JS)
    projects=[]
    for path in sorted(CONTENT.glob("*.md")):
        _, front, body=path.read_text().split("---",2)
        meta=yaml.safe_load(front)
        target=DEST/path.stem
        target.mkdir(exist_ok=True)
        rendered=markdown.markdown(body,extensions=["sane_lists"])
        heading=re.search(r"<h1>.*?</h1>",rendered,re.S).group()
        rendered=rendered.replace(heading,"",1)
        meta.update(slug=path.stem,rendered=rendered,body=body)
        projects.append(meta)
        detail=f'<p><a href="../#{path.stem}">← All projects</a></p>{heading}<div class="project-reading">{rendered}</div>'
        (target/"index.html").write_text(page(meta["title"],detail,"../"))
        (target/"note.md").write_text(body.strip()+"\n")
    projects.sort(key=lambda p:(p.get("id", "zz"), p["title"].lower()))
    groups=[("In progress","active",lambda p:p["status"].startswith("In progress")),("Follow-up projects","followup",lambda p:p["status"].startswith("Follow-up")),("New project ideas","new",lambda p:p["status"].startswith("Not started"))]
    body=f'''<h1>Research projects</h1><p>These are projects I'm working on or would be interested in mentoring. Some already have teams; others are ideas we could develop together.</p>
<div class="onboarding"><p>For SPAR, please:</p><ol>
<li>Send me your <strong>top five projects, ranked</strong>, with a sentence on what interests you in each.</li>
<li>Tell me your <strong>preferred team size</strong>, including yourself and excluding mentors, and how flexible you are.</li>
<li>Read my <a href="{ADVICE}">advice for mentees</a> before we meet.</li>
<li>Book an introductory call using the <a href="{PST_BOOKING}">PST scheduling link</a>. <strong>Please use PST whenever possible.</strong> Only use the <a href="{NON_PST_BOOKING}">non-PST scheduling link</a> if you need to because the PST times don't work for you.</li>
</ol><p class="booking-duration">Our introductory chat will take 15 minutes. The booking pages currently reserve 30-minute slots.</p></div>
<div class="filters"><label for="search">Search projects<input type="search" id="search" placeholder="Search titles and proposals"></label><label for="status">Work status<select id="status"><option value="">All projects</option><option value="active">In progress</option><option value="followup">Follow-up projects</option><option value="new">New project ideas</option></select></label></div><p id="count" class="meta" role="status">{len(projects)} projects</p><p id="empty" hidden>No projects match. Try a different search or status.</p>'''
    for title,key,predicate in groups:
        rows=[p for p in projects if predicate(p)]
        body+=f'<section class="project-group"><h2>{escape(title)}</h2>'
        for p in rows:
            body+=f'<article class="project-row" id="{p["slug"]}" data-status="{key}"><h3><a href="#{p["slug"]}">{escape(p["title"])}</a></h3><div class="project-reading">{p["rendered"]}</div></article>'
        body+='</section>'
    (DEST/"index.html").write_text(page("Research projects",body))
    print(f"Rendered all {len(projects)} full proposals inline at {DEST}")

if __name__=="__main__":
    main()
