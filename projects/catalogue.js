
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
