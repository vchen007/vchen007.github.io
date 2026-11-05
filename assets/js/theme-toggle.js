/* Light/dark theme toggle. The saved choice is applied before first paint by
   the inline snippet in _includes/head/custom.html; this file wires up the
   button and keeps its label in sync. Without a saved choice the site follows
   the visitor's system setting. */
(function () {
  var root = document.documentElement;
  var button = document.getElementById('theme-toggle');
  if (!button) return;
  var systemDark = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;

  function current() {
    var chosen = root.getAttribute('data-theme');
    if (chosen === 'dark' || chosen === 'light') return chosen;
    return systemDark && systemDark.matches ? 'dark' : 'light';
  }

  function syncLabel() {
    var dark = current() === 'dark';
    button.setAttribute('aria-pressed', dark ? 'true' : 'false');
    button.setAttribute('aria-label', dark ? 'Switch to light theme' : 'Switch to dark theme');
  }

  button.addEventListener('click', function () {
    var next = current() === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('theme', next); } catch (e) { /* private mode: still switches for this page */ }
    syncLabel();
  });

  if (systemDark && systemDark.addEventListener) systemDark.addEventListener('change', syncLabel);
  syncLabel();
})();
