
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
