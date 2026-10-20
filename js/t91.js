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

/* catalogo racchette: filtri e ordinamento */
(function () {
  var grid = document.getElementById('pgrid');
  if (!grid) return;
  var cards = Array.prototype.slice.call(grid.children);
  var boxes = Array.prototype.slice.call(document.querySelectorAll('#filters input[type=checkbox]'));
  var sort = document.getElementById('sort');
  var count = document.getElementById('count');
  var chips = document.getElementById('chips');
  var empty = document.getElementById('empty');
  var fbtn = document.getElementById('fbtn');
  var filters = document.getElementById('filters');

  function active() {
    var a = {};
    boxes.forEach(function (b) {
      if (b.checked) { (a[b.getAttribute('data-k')] = a[b.getAttribute('data-k')] || []).push(b.value); }
    });
    return a;
  }
  function match(c, a) {
    return Object.keys(a).every(function (k) { return a[k].indexOf(c.getAttribute('data-' + k)) !== -1; });
  }
  function order() {
    var v = sort.value;
    var list = cards.slice();
    list.sort(function (x, y) {
      var d;
      if (v === 'new') { d = y.getAttribute('data-new') - x.getAttribute('data-new'); }
      else if (v === 'az') { d = x.getAttribute('data-name') < y.getAttribute('data-name') ? -1 : 1; }
      else if (v === 'pa') { d = x.getAttribute('data-price') - y.getAttribute('data-price'); }
      else if (v === 'pd') { d = y.getAttribute('data-price') - x.getAttribute('data-price'); }
      else { d = 0; }
      return d || (x.getAttribute('data-i') - y.getAttribute('data-i'));
    });
    list.forEach(function (c) { grid.appendChild(c); });
  }
  function render() {
    var a = active();
    var shown = 0;
    cards.forEach(function (c) {
      var ok = match(c, a);
      c.hidden = !ok;
      if (ok) shown++;
    });
    count.textContent = shown === 1 ? '1 prodotto' : shown + ' prodotti';
    empty.hidden = shown !== 0;
    chips.textContent = '';
    boxes.forEach(function (b) {
      if (!b.checked) return;
      var ch = document.createElement('button');
      ch.type = 'button';
      ch.className = 'chip';
      ch.textContent = b.value;
      ch.setAttribute('aria-label', 'Togli il filtro ' + b.value);
      ch.addEventListener('click', function () { b.checked = false; render(); });
      chips.appendChild(ch);
    });
  }
  function reset() { boxes.forEach(function (b) { b.checked = false; }); render(); }

  boxes.forEach(function (b) { b.addEventListener('change', render); });
  sort.addEventListener('change', function () { order(); render(); });
  document.getElementById('reset').addEventListener('click', reset);
  document.getElementById('reset2').addEventListener('click', reset);
  fbtn.addEventListener('click', function () {
    var open = filters.classList.toggle('open');
    fbtn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  render();
})();
