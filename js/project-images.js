// The image link remains a full-size destination when JavaScript is unavailable.
(() => {
  const links = [...document.querySelectorAll('a.project-overview')];
  if (!links.length || typeof HTMLDialogElement === 'undefined') return;
  const hoverCapable = matchMedia('(hover: hover) and (pointer: fine)');
  const preview = document.createElement('div');
  preview.className = 'project-image-preview';
  preview.hidden = true;
  preview.setAttribute('aria-hidden', 'true');
  const previewImage = document.createElement('img');
  previewImage.alt = '';
  preview.append(previewImage);
  document.body.append(preview);

  const dialog = document.createElement('dialog');
  dialog.className = 'project-image-dialog';
  dialog.setAttribute('aria-labelledby', 'project-image-title');
  dialog.innerHTML = '<div class="project-image-toolbar"><h2 id="project-image-title"></h2><button type="button" class="project-image-close" aria-label="Close project image" autofocus>Close <span aria-hidden="true">×</span></button></div><img class="project-image-full" alt=""><p class="project-image-caption"></p><div class="project-image-sources"><a class="project-image-source" target="_blank" rel="noopener">Read the research</a><a class="project-image-original" target="_blank" rel="noopener">Original paper figure</a><a class="project-image-file" target="_blank" rel="noopener">Open image</a></div>';
  document.body.append(dialog);
  const title = dialog.querySelector('h2');
  const fullImage = dialog.querySelector('.project-image-full');
  const caption = dialog.querySelector('.project-image-caption');
  const source = dialog.querySelector('.project-image-source');
  const original = dialog.querySelector('.project-image-original');
  let activeLink, openTimer, closeTimer, previousOverflow = '';

  function hidePreview() {
    clearTimeout(openTimer);
    clearTimeout(closeTimer);
    preview.hidden = true;
  }
  function showPreview(link) {
    if (!hoverCapable.matches || dialog.open) return;
    activeLink = link;
    previewImage.src = link.href;
    const thumbnail = link.querySelector('img');
    const imageWidth = Number(thumbnail.getAttribute('width')) || thumbnail.naturalWidth;
    const imageHeight = Number(thumbnail.getAttribute('height')) || thumbnail.naturalHeight;
    const ratio = imageWidth / imageHeight || 1.5;
    previewImage.width = imageWidth;
    previewImage.height = imageHeight;
    const rect = link.getBoundingClientRect();
    const width = Math.min(760, innerWidth - 32, (innerHeight - 48) * ratio);
    const height = width / ratio;
    const left = Math.max(16, Math.min(rect.left, innerWidth - width - 16));
    const top = Math.max(16, Math.min(rect.top - (height - rect.height) / 2, innerHeight - height - 16));
    preview.style.width = `${width}px`;
    preview.style.left = `${left}px`;
    preview.style.top = `${top}px`;
    preview.hidden = false;
  }
  function scheduleClose() {
    clearTimeout(openTimer);
    closeTimer = setTimeout(hidePreview, 120);
  }
  function openImage(link) {
    hidePreview();
    activeLink = link;
    title.textContent = link.dataset.title;
    fullImage.src = link.href;
    fullImage.alt = link.querySelector('img').alt;
    caption.textContent = link.dataset.caption || '';
    source.hidden = !link.dataset.source;
    if (link.dataset.source) source.href = link.dataset.source;
    original.hidden = !link.dataset.original;
    if (link.dataset.original) original.href = link.dataset.original;
    dialog.querySelector('.project-image-file').href = link.href;
    previousOverflow = document.documentElement.style.overflow;
    document.documentElement.style.overflow = 'hidden';
    dialog.showModal();
  }
  links.forEach(link => {
    link.setAttribute('aria-haspopup', 'dialog');
    link.addEventListener('pointerenter', () => {
      clearTimeout(closeTimer);
      clearTimeout(openTimer);
      openTimer = setTimeout(() => showPreview(link), 180);
    });
    link.addEventListener('pointerleave', scheduleClose);
    link.addEventListener('click', event => {
      if (event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      openImage(link);
    });
  });
  preview.addEventListener('pointerenter', () => clearTimeout(closeTimer));
  preview.addEventListener('pointerleave', scheduleClose);
  preview.addEventListener('click', () => activeLink && openImage(activeLink));
  dialog.querySelector('.project-image-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const bounds = dialog.getBoundingClientRect();
    if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
  });
  dialog.addEventListener('close', () => {
    document.documentElement.style.overflow = previousOverflow;
    hidePreview();
    activeLink?.focus({ preventScroll: true });
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape') hidePreview();
  });
  window.addEventListener('scroll', hidePreview, { passive: true });
  window.addEventListener('resize', hidePreview);
})();
