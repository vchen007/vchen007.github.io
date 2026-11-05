/* Small site-wide helpers. Wide tables and code blocks scroll sideways; make
   the ones that actually overflow reachable with the keyboard. */
(function () {
  var nodes = document.querySelectorAll('.page__content table, .page__content pre');
  Array.prototype.forEach.call(nodes, function (node) {
    if (node.scrollWidth > node.clientWidth + 1 && !node.hasAttribute('tabindex')) {
      node.setAttribute('tabindex', '0');
      node.setAttribute('role', 'region');
      node.setAttribute('aria-label', node.tagName === 'PRE' ? 'Code (scrolls sideways)' : 'Table (scrolls sideways)');
    }
  });
})();
