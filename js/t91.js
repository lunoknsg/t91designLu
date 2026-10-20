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
