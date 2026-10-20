(function () {
  var $ = function (id) { return document.getElementById(id); };
  var eur = function (v) { return '€' + v.toFixed(2).replace('.', ','); };
  var toastEl = $('toast'), toastT;
  function toast(msg) {
    if (!toastEl) return;
    toastEl.textContent = msg; toastEl.hidden = false;
    clearTimeout(toastT); toastT = setTimeout(function () { toastEl.hidden = true; }, 2600);
  }
  var cartN = 0;
  function addToCart(n, msg) {
    cartN += n;
    var c = document.querySelector('.hdr-r a:last-child');
    if (c) c.textContent = 'Carrello (' + cartN + ')';
    toast(msg);
  }

  /* galleria con scorrimento automatico */
  var gal = $('gal');
  if (gal) {
    var items = gal.getAttribute('data-g').split('|').map(function (s) { var p = s.split('~'); return { src: p[0], alt: p[1] }; });
    var main = $('gmain'), cnt = $('gcount'), thumbs = $('thumbs'), stage = $('stage'), play = $('gplay');
    var ths = Array.prototype.slice.call(gal.querySelectorAll('.th'));
    var cur = 0, timer = null, userPaused = false, hover = false;
    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var swapT;
    var centerThumb = function () {
      var t = ths[cur];
      var left = t.offsetLeft - (thumbs.clientWidth - t.clientWidth) / 2;
      thumbs.scrollTo({ left: left, behavior: reduce ? 'auto' : 'smooth' });
    };
    var show = function (i) {
      cur = (i + items.length) % items.length;
      clearTimeout(swapT);
      main.classList.add('swap');
      swapT = setTimeout(function () {
        main.src = items[cur].src; main.alt = items[cur].alt;
        var done = function () { main.classList.remove('swap'); };
        if (main.complete) done(); else main.onload = done;
        setTimeout(done, 600);
      }, reduce ? 0 : 180);
      cnt.textContent = (cur + 1) + ' / ' + items.length;
      ths.forEach(function (t, k) { if (k === cur) t.setAttribute('aria-current', 'true'); else t.removeAttribute('aria-current'); });
      centerThumb();
    };
    var stop = function () { clearInterval(timer); timer = null; };
    var start = function () {
      stop();
      if (reduce || userPaused || hover || document.hidden) return;
      timer = setInterval(function () { show(cur + 1); }, 4500);
    };
    var manual = function (i) { show(i); start(); };
    ths.forEach(function (t, k) { t.addEventListener('click', function () { manual(k); }); });
    $('gprev').addEventListener('click', function () { manual(cur - 1); });
    $('gnext').addEventListener('click', function () { manual(cur + 1); });
    $('tprev').addEventListener('click', function () { thumbs.scrollBy({ left: -thumbs.clientWidth * 0.8, behavior: 'smooth' }); });
    $('tnext').addEventListener('click', function () { thumbs.scrollBy({ left: thumbs.clientWidth * 0.8, behavior: 'smooth' }); });
    gal.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') manual(cur - 1);
      if (e.key === 'ArrowRight') manual(cur + 1);
    });
    var setPaused = function (v) {
      userPaused = v;
      play.setAttribute('aria-pressed', v ? 'true' : 'false');
      play.setAttribute('aria-label', v ? 'Riprendi lo scorrimento automatico' : 'Metti in pausa lo scorrimento automatico');
      start();
    };
    play.addEventListener('click', function () { setPaused(!userPaused); });
    stage.addEventListener('mouseenter', function () { hover = true; stop(); });
    stage.addEventListener('mouseleave', function () { hover = false; start(); });
    stage.addEventListener('focusin', function () { hover = true; stop(); });
    stage.addEventListener('focusout', function () { hover = false; start(); });
    document.addEventListener('visibilitychange', start);
    var sx = null;
    stage.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; stop(); }, { passive: true });
    stage.addEventListener('touchend', function (e) {
      if (sx === null) return;
      var dx = e.changedTouches[0].clientX - sx; sx = null;
      if (Math.abs(dx) > 40) manual(cur + (dx < 0 ? 1 : -1)); else start();
    });
    if (reduce) { userPaused = true; play.setAttribute('aria-pressed', 'true'); play.setAttribute('aria-label', 'Riprendi lo scorrimento automatico'); }
    start();
  }

  /* prezzo, peso e protezione */
  var priceEl = $('price');
  if (priceEl) {
    var base = parseFloat(priceEl.getAttribute('data-base'));
    var extra = 0, care = 0;
    var update = function () {
      var p = base + extra;
      priceEl.textContent = eur(p);
      $('klarna').textContent = 'oppure 3 rate da ' + eur(p / 3) + ' senza interessi con Klarna';
      $('club').textContent = eur(p * 0.7);
      $('sclub').textContent = eur(p * 0.7);
      $('sprice').textContent = eur(p + care);
    };
    Array.prototype.forEach.call(document.querySelectorAll('input[name="peso"]'), function (r) {
      r.addEventListener('change', function () {
        extra = parseFloat(r.value);
        $('wg').hidden = extra === 0;
        update();
      });
    });
    Array.prototype.forEach.call(document.querySelectorAll('input[name="care"]'), function (r) {
      r.addEventListener('change', function () { care = parseFloat(r.value); update(); });
    });
    Array.prototype.forEach.call(document.querySelectorAll('.chipw'), function (b) {
      b.addEventListener('click', function () {
        Array.prototype.forEach.call(document.querySelectorAll('.chipw'), function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      });
    });
    var addMsg = function () {
      var w = extra ? ' (peso a scelta)' : '';
      addToCart(1, 'Aggiunta al carrello' + w + ' (prototipo)');
    };
    $('add').addEventListener('click', addMsg);
    $('sadd').addEventListener('click', addMsg);
  }

  /* barra di acquisto fissa */
  var sbar = $('sbar'), add = $('add');
  if (sbar && add && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (en) {
      var out = !en[0].isIntersecting && en[0].boundingClientRect.top < 0;
      sbar.classList.toggle('on', out);
      sbar.setAttribute('aria-hidden', out ? 'false' : 'true');
      $('sadd').tabIndex = out ? 0 : -1;
    }).observe(add);
  }

  /* set e acquisti abbinati */
  var addset = $('addset');
  if (addset) addset.addEventListener('click', function () { addToCart(4, 'Set aggiunto al carrello (prototipo)'); });
  var tgs = Array.prototype.slice.call(document.querySelectorAll('.tgl input'));
  if (tgs.length) {
    var tot = function () {
      var t = 0;
      tgs.forEach(function (c) { if (c.checked) t += parseFloat(c.getAttribute('data-p')); });
      $('tgtot').textContent = eur(t);
    };
    tgs.forEach(function (c) { c.addEventListener('change', tot); });
    $('addtg').addEventListener('click', function () {
      var n = tgs.filter(function (c) { return c.checked; }).length;
      addToCart(n, n + ' prodotti aggiunti al carrello (prototipo)');
    });
  }
})();
