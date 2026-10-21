(function () {
  document.querySelectorAll('a[href="#"]').forEach(function (a) {
    a.classList.add('todo-link');
    a.setAttribute('title', 'Link da collegare (prototipo)');
    a.addEventListener('click', function (e) { e.preventDefault(); });
  });
})();
(function () {
  var q = document.getElementById('q');
  if (!q) return;
  var items = Array.prototype.slice.call(document.querySelectorAll('#clist li'));
  var none = document.getElementById('none');
  q.addEventListener('input', function () {
    var v = q.value.trim().toLowerCase();
    var shown = 0;
    items.forEach(function (li) {
      var ok = !v || li.getAttribute('data-s').indexOf(v) !== -1;
      li.hidden = !ok;
      if (ok) shown++;
    });
    none.hidden = shown !== 0;
  });
})();

/* Le più acquistate: la base dell'invito coincide con la base delle foto */
(function () {
  var t = document.querySelector('.best-t'), ph = document.querySelector('.best-l .pc-ph');
  if (!t || !ph) return;
  var set = function () {
    if (window.innerWidth <= 1000) { t.style.height = ''; return; }
    t.style.height = ph.getBoundingClientRect().height + 'px';
  };
  set();
  if ('ResizeObserver' in window) new ResizeObserver(set).observe(ph); else window.addEventListener('resize', set);
  window.addEventListener('load', set);
})();
