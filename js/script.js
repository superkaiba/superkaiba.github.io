const toggle = document.getElementById('theme-toggle');
let savedTheme;
try { savedTheme = localStorage.getItem('theme'); } catch (_) {}
let isDark = savedTheme ? savedTheme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
function applyTheme() {
  document.documentElement.dataset.theme = isDark ? 'dark' : 'light';
  toggle.title = isDark ? 'Switch to light mode' : 'Switch to dark mode';
  toggle.setAttribute('aria-label', isDark ? 'Light mode' : 'Dark mode');
  toggle.setAttribute('aria-pressed', String(isDark));
}
applyTheme();
toggle.addEventListener('click', () => {
  isDark = !isDark;
  applyTheme();
  try { localStorage.setItem('theme', isDark ? 'dark' : 'light'); } catch (_) {}
});

// Reveal the containing directories before jumping to a project or list.
function revealHashTarget(hash, moveFocus = false) {
  let id;
  try { id = decodeURIComponent(hash.slice(1)); } catch (_) { return false; }
  const legacySections = { 'mentored-students': 'mentees', featured: 'research', publications: 'research' };
  const target = document.getElementById(legacySections[id] || id);
  if (!target) return false;
  for (let node = target; node; node = node.parentElement) {
    if (node.tagName === 'DETAILS') node.open = true;
  }
  selectContentsTarget(target);
  requestAnimationFrame(() => {
    target.scrollIntoView({ block: 'start' });
    if (moveFocus) {
      const focusTarget = target.tagName === 'DETAILS' ? target.querySelector('summary') : target;
      if (!focusTarget.hasAttribute('tabindex') && focusTarget.tagName !== 'SUMMARY') {
        focusTarget.setAttribute('tabindex', '-1');
      }
      focusTarget.focus({ preventScroll: true });
    }
    settleContentsSelection();
  });
  return true;
}
function normalizedPath(path) { return path.replace(/index\.html$/, ''); }
document.addEventListener('click', event => {
  if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
  const link = event.target.closest('a[href]');
  if (!link || link.hasAttribute('download') || (link.target && link.target !== '_self')) return;
  const url = new URL(link.href, location.href);
  if (url.origin !== location.origin || normalizedPath(url.pathname) !== normalizedPath(location.pathname) || !url.hash) return;
  if (revealHashTarget(url.hash, true)) {
    event.preventDefault();
    if (location.hash !== url.hash) history.pushState(null, '', url.hash);
  }
});
window.addEventListener('hashchange', () => revealHashTarget(location.hash));
window.addEventListener('load', () => {
  if (location.hash) revealHashTarget(location.hash);
});

// A compact contents menu on narrow screens and an active-section indicator everywhere.
document.documentElement.classList.add('has-js');
const contents = document.querySelector('.contents');
const contentsToggle = document.querySelector('.contents-toggle');
const contentsLinks = [...document.querySelectorAll('.contents a[data-section]')];
const currentSectionLabel = document.querySelector('.current-section');
const trackedSections = contentsLinks.map(link => ({ link, section: document.getElementById(link.dataset.section) })).filter(item => item.section);
let selectedDestination = null;
let destinationScrollY = null;
let destinationTimer;
function selectContentsTarget(target) {
  selectedDestination = trackedSections.find(item => item.section === target.closest('.toc-section')) || null;
  destinationScrollY = null;
  scheduleContentsUpdate();
}
function settleContentsSelection() {
  clearTimeout(destinationTimer);
  if (selectedDestination) destinationTimer = setTimeout(() => { destinationScrollY = scrollY; }, 160);
}
function clearContentsSelection() {
  selectedDestination = null;
  destinationScrollY = null;
  clearTimeout(destinationTimer);
  scheduleContentsUpdate();
}
let contentsReturnY = null;
function setContentsExpanded(expanded, restoreScroll = true) {
  if (!contentsToggle) return;
  const mobile = innerWidth <= 540;
  if (expanded && mobile) contentsReturnY = scrollY;
  contents.dataset.expanded = String(expanded);
  contentsToggle.setAttribute('aria-expanded', String(expanded));
  contentsToggle.querySelector('.contents-indicator').textContent = expanded ? '−' : '+';
  if (mobile && expanded) {
    // The expanded menu uses the page scroll, so bring it into view from any section.
    contents.scrollIntoView({ block: 'start', behavior: 'instant' });
  } else if (!expanded && contentsReturnY !== null) {
    if (restoreScroll && mobile) scrollTo({ top: contentsReturnY, behavior: 'instant' });
    contentsReturnY = null;
  }
}
contentsToggle?.addEventListener('click', () => setContentsExpanded(contents.dataset.expanded !== 'true'));
contents?.addEventListener('keydown', event => {
  if (event.key === 'Escape' && contents.dataset.expanded === 'true') {
    setContentsExpanded(false);
    contentsToggle.focus({ preventScroll: true });
  }
});
contentsLinks.forEach(link => link.addEventListener('click', event => {
  if (event.button === 0 && !event.metaKey && !event.ctrlKey && !event.shiftKey && !event.altKey) setContentsExpanded(false, false);
}));
let contentsFramePending = false;
function updateContents() {
  contentsFramePending = false;
  if (!trackedSections.length) return;
  // Opening the mobile menu should preserve the section the reader came from.
  if (innerWidth <= 540 && contents.dataset.expanded === 'true') return;
  const threshold = Math.min(innerHeight * 0.22, 160);
  let current = trackedSections[0];
  for (const item of trackedSections) {
    if (item.section.getBoundingClientRect().top <= threshold) current = item;
  }
  if (scrollY > 0 && scrollY + innerHeight >= document.documentElement.scrollHeight - 2) current = trackedSections.at(-1);
  // Keep the chosen destination active when a short final section cannot reach the top.
  if (selectedDestination) current = selectedDestination;
  for (const item of trackedSections) {
    if (item === current) item.link.setAttribute('aria-current', 'location');
    else item.link.removeAttribute('aria-current');
  }
  if (currentSectionLabel) currentSectionLabel.textContent = current.link.textContent;
}
function scheduleContentsUpdate() {
  if (contentsFramePending) return;
  contentsFramePending = true;
  requestAnimationFrame(updateContents);
}
window.addEventListener('scroll', () => {
  if (destinationScrollY !== null && Math.abs(scrollY - destinationScrollY) > 2) clearContentsSelection();
  settleContentsSelection();
  scheduleContentsUpdate();
}, { passive: true });
window.addEventListener('wheel', clearContentsSelection, { passive: true });
window.addEventListener('touchstart', clearContentsSelection, { passive: true });
window.addEventListener('keydown', event => {
  if (['ArrowUp', 'ArrowDown', 'PageUp', 'PageDown', 'Home', 'End', ' '].includes(event.key)) clearContentsSelection();
});
window.addEventListener('resize', scheduleContentsUpdate);
document.addEventListener('toggle', scheduleContentsUpdate, true);
window.addEventListener('load', scheduleContentsUpdate);
if ('ResizeObserver' in window) new ResizeObserver(scheduleContentsUpdate).observe(document.getElementById('main'));
scheduleContentsUpdate();

// Keep every sidebar item reachable without creating a nested scrolling area.
function updateSidebarPosition() {
  if (!contents) return;
  if (innerWidth <= 540) {
    contents.style.removeProperty('--sidebar-sticky-top');
    return;
  }
  const preferredTop = parseFloat(getComputedStyle(contents).getPropertyValue('--sidebar-offset')) || 0;
  const top = Math.min(preferredTop, innerHeight - contents.offsetHeight - 24);
  contents.style.setProperty('--sidebar-sticky-top', `${top}px`);
}
window.addEventListener('resize', updateSidebarPosition);
if ('ResizeObserver' in window) new ResizeObserver(updateSidebarPosition).observe(contents);
updateSidebarPosition();
