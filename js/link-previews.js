export function installLinkPreviews(root,popup,requestPreview){
  const doc=root.ownerDocument,win=doc.defaultView;
  const field=name=>popup.querySelector('#link-preview-'+name);
  const cache=new Map();
  let active=null,destination='',hideTimer,loadTimer,generation=0,lastTouch=0;
  function position(){
    if(!active||popup.hidden)return;
    const rect=active.getBoundingClientRect(),box=popup.getBoundingClientRect();
    popup.style.left=Math.max(12,Math.min(win.innerWidth-box.width-12,rect.left))+'px';
    popup.style.top=(rect.bottom+box.height+12<win.innerHeight?rect.bottom+8:Math.max(12,rect.top-box.height-8))+'px';
  }
  function hide(){clearTimeout(hideTimer);clearTimeout(loadTimer);generation++;popup.hidden=true;active?.removeAttribute('aria-describedby');active=null;}
  function scheduleHide(){clearTimeout(hideTimer);hideTimer=setTimeout(hide,220);}
  function render(data){
    field('site').textContent=data.site||field('site').textContent;
    field('title').textContent=data.title||'';field('title').hidden=!data.title;
    field('description').textContent=data.description||'';field('description').hidden=!data.description;
    const image=field('image');image.hidden=true;image.removeAttribute('src');
    // Only our raster image cache can supply an image, never remote HTML or scripts.
    if(/^\/assets\//.test(data.image||'')){image.src=data.image;image.hidden=false;}
    field('note').textContent=data.available?(data.internal?'On this website · Open link ↗':'Open link ↗'):'Open link ↗';
    popup.removeAttribute('aria-busy');position();
  }
  function show(link){
    if(popup.contains(link)||link.matches('.skip-link,[data-no-preview]'))return;const href=link.href;if(!/^https?:\/\//i.test(href))return;
    clearTimeout(hideTimer);
    if(active===link&&destination===href&&!popup.hidden)return;
    clearTimeout(loadTimer);active?.removeAttribute('aria-describedby');active=link;destination=href;
    const token=++generation;link.setAttribute('aria-describedby',popup.id);
    field('url').textContent=href;field('url').title=href;field('url').removeAttribute('href');
    const local=!!link.getAttribute('data-source-href');
    if(!local&&/^(https?:\/\/|mailto:|#)/i.test(href))field('url').setAttribute('href',href);
    field('title').hidden=true;field('description').hidden=true;field('image').hidden=true;field('image').removeAttribute('src');
    field('site').textContent='Link destination';popup.removeAttribute('aria-busy');
    field('note').textContent=local?'Local note link':href.startsWith('#')?'Within this draft':'Open link ↗';popup.hidden=false;
    if(!local&&/^https?:\/\//i.test(href)){
      try{field('site').textContent=new URL(href).hostname;}catch{}
      field('note').textContent='Loading preview…';popup.setAttribute('aria-busy','true');
      // Brief passes over links don't cause network requests.
      loadTimer=setTimeout(async()=>{
        let entry=cache.get(href);
        if(!entry||entry.expires<Date.now()){
          entry={expires:Date.now()+60_000,promise:requestPreview(href).catch(()=>({available:false}))};cache.set(href,entry);
          if(cache.size>64)cache.delete(cache.keys().next().value);
        }
        const data=await entry.promise;
        if(token===generation&&active===link&&!popup.hidden)render(data);
      },300);
    }
    position();
  }
  const over=e=>{if(e.pointerType==='touch'){lastTouch=Date.now();return;}if(Date.now()-lastTouch<800)return;const link=e.target.closest('a');if(link)show(link);};
  const out=e=>{const link=e.target.closest('a');if(link&&!popup.contains(link)&&!link.contains(e.relatedTarget))scheduleHide();};
  const hold=()=>clearTimeout(hideTimer);
  const escape=e=>{if(e.key==='Escape')hide();};
  const scroll=()=>{if(active===doc.activeElement){const rect=active.getBoundingClientRect();if(rect.bottom>0&&rect.top<win.innerHeight){position();return;}}hide();};
  const imageLoad=()=>position();
  const imageError=()=>{field('image').hidden=true;position();};
  root.addEventListener('pointerover',over);root.addEventListener('pointerout',out);
  root.addEventListener('focusin',over);root.addEventListener('focusout',out);
  popup.addEventListener('pointerenter',hold);popup.addEventListener('pointerleave',scheduleHide);
  popup.addEventListener('focusin',hold);popup.addEventListener('focusout',scheduleHide);
  field('image').addEventListener('load',imageLoad);field('image').addEventListener('error',imageError);
  win.addEventListener('scroll',scroll,{passive:true});win.addEventListener('resize',hide);doc.addEventListener('keydown',escape);
  return ()=>{hide();root.removeEventListener('pointerover',over);root.removeEventListener('pointerout',out);root.removeEventListener('focusin',over);root.removeEventListener('focusout',out);popup.removeEventListener('pointerenter',hold);popup.removeEventListener('pointerleave',scheduleHide);popup.removeEventListener('focusin',hold);popup.removeEventListener('focusout',scheduleHide);field('image').removeEventListener('load',imageLoad);field('image').removeEventListener('error',imageError);win.removeEventListener('scroll',scroll);win.removeEventListener('resize',hide);doc.removeEventListener('keydown',escape);};
}


export function previewKey(value,origin){
  const url=new URL(value,origin),canonicalHost='thomas.jiralerspong.com';
  if(url.origin===origin||url.hostname===canonicalHost||url.hostname==='superkaiba.github.io'){url.hostname=canonicalHost;url.port='';url.protocol='https:';}
  url.pathname=url.pathname.replace(/index\.html$/,'');return url.href;
}

// Public-site previews use only static, same-origin assets. No reader requests go to linked sites.
if(typeof document!=='undefined'&&document.querySelector('article.blog-body')){
  const card=document.createElement('div');card.id='link-preview';card.className='link-preview';card.hidden=true;card.setAttribute('role','tooltip');card.setAttribute('aria-label','Link preview');
  card.innerHTML='<img id="link-preview-image" alt="" hidden><div class="link-preview-content"><span id="link-preview-site"></span><strong id="link-preview-title" hidden></strong><p id="link-preview-description" hidden></p><a id="link-preview-url" target="_blank" rel="noopener noreferrer"></a><span id="link-preview-note"></span></div>';
  document.body.append(card);
  let index;
  installLinkPreviews(document.querySelector('article.blog-body'),card,async href=>{
    if(!index)index=fetch('/assets/link-previews/index.json',{credentials:'omit',cache:'no-cache'}).then(r=>{if(!r.ok)throw new Error('Preview index unavailable');return r.json();}).catch(error=>{index=null;throw error;});
    const entries=(await index).links,url=previewKey(href,location.origin);
    return entries[url]||entries[url.split('#')[0]]||{available:false,site:new URL(href).hostname};
  });
}
