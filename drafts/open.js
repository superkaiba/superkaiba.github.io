const query = new URLSearchParams(location.hash.slice(1));
const access = query.get('access');
const url = new URL('https://draft-studio.superkaiba.com/');
const parameters = new URLSearchParams();
if (access && /^[A-Za-z0-9_-]{40,100}$/.test(access)) {
  parameters.set('access', access);
}
if (query.get('draft')) parameters.set('draft', query.get('draft'));
if (query.get('view') === 'drafts') parameters.set('view', 'drafts');
url.hash = parameters.toString();
document.getElementById('open-studio').href = url.href;
// Keep access in the editor's own browser context instead of relying on
// third-party cookies. A new private window still needs its private link.
location.replace(url.href);
