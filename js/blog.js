(function () {
  var grid = document.getElementById('bgrid');
  if (!grid) return;
  var btns = Array.prototype.slice.call(document.querySelectorAll('.bc'));
  var items = Array.prototype.slice.call(grid.children);
  var count = document.getElementById('bcount');
  btns.forEach(function (b) {
    b.addEventListener('click', function () {
      var c = b.getAttribute('data-c'), n = 0;
      btns.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      items.forEach(function (li) {
        var ok = !c || li.getAttribute('data-cat') === c;
        li.hidden = !ok; if (ok) n++;
      });
      items.forEach(function (li) { li.classList.remove('big'); });
      var first = items.filter(function (li) { return !li.hidden; })[0];
      if (first && !c) first.classList.add('big');
      count.textContent = n + (n === 1 ? ' articolo' : ' articoli');
    });
  });
})();
