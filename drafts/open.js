const query = new URLSearchParams(location.hash.slice(1));
const access = query.get('access');
if (access && /^[A-Za-z0-9_-]{40,100}$/.test(access)) {
  const url = new URL('https://draft-studio.superkaiba.com/');
  const parameters = new URLSearchParams({access});
  if (query.get('draft')) parameters.set('draft', query.get('draft'));
  url.hash = parameters.toString();
  document.getElementById('studio').src = url.href;
  document.getElementById('studio').hidden = false;
  document.getElementById('message').hidden = true;
}
