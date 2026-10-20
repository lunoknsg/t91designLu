(function () {
  var grid = document.getElementById('pgrid');
  if (!grid) return;
  var $ = function (id) { return document.getElementById(id); };
  var eur = function (v) { return '€' + v.toFixed(2).replace('.', ','); };
  var cards = Array.prototype.slice.call(grid.children);
  var boxes = Array.prototype.slice.call(document.querySelectorAll('#filters input[type=checkbox]'));
  var cmp = [];
  var toastEl = $('toast'), toastT;
  function toast(msg) {
    toastEl.textContent = msg; toastEl.hidden = false;
    clearTimeout(toastT); toastT = setTimeout(function () { toastEl.hidden = true; }, 2800);
  }

  function active() {
    var a = {};
    boxes.forEach(function (b) { if (b.checked) { var k = b.getAttribute('data-k'); (a[k] = a[k] || []).push(b.value); } });
    return a;
  }
  function match(c, a) {
    return Object.keys(a).every(function (k) { return a[k].indexOf(c.getAttribute('data-' + k)) !== -1; });
  }
  function order() {
    var v = $('sort').value, list = cards.slice();
    list.sort(function (x, y) {
      var d = 0;
      if (v === 'new') d = y.getAttribute('data-new') - x.getAttribute('data-new');
      else if (v === 'pa') d = x.getAttribute('data-price') - y.getAttribute('data-price');
      else if (v === 'pd') d = y.getAttribute('data-price') - x.getAttribute('data-price');
      return d || (x.getAttribute('data-i') - y.getAttribute('data-i'));
    });
    list.forEach(function (c) { grid.appendChild(c); });
  }

  var DEF_T = 'Racchette da padel.';
  var DEF_D = 'Tutte le racchette T91, dal primo match al torneo. Filtra per livello e stile di gioco, o fatti consigliare dal test.';
  function heading(a) {
    var lv = a.lv && a.lv.length === 1 ? a.lv[0] : '';
    var st = a.st && a.st.length === 1 ? a.st[0] : '';
    var co = a.co && a.co.length === 1 ? a.co[0] : '';
    var only = Object.keys(a).filter(function (k) { return k === 'lv' || k === 'st' || k === 'co'; }).length === Object.keys(a).length;
    if (!only) return [DEF_T, DEF_D];
    if (co === 'Holo' && !lv && !st) return ['Holo Collection.', 'La nuova linea Master 6.0: carbonio, potenza e i colori Holo.'];
    if (co === 'Signature Pro' && !lv && !st) return ['Signature Pro.', 'Le racchette progettate insieme ai nostri atleti.'];
    var L = { Principianti: 'per principianti', Intermedi: 'per intermedi', Avanzati: 'per giocatori avanzati', Pro: 'per professionisti' }[lv] || '';
    var T = { Potenza: 'da potenza', Controllo: 'da controllo', Polivalenti: 'polivalenti' }[st] || '';
    if (!L && !T) return [DEF_T, DEF_D];
    var D = { Principianti: 'Leggere, maneggevoli e facili da gestire: per imparare e divertirsi dal primo giorno.', Intermedi: 'Per chi gioca con continuità e vuole crescere: più controllo e più precisione.', Avanzati: 'Potenza e risposta secca per chi chiude il punto.', Pro: 'Le racchette che gioca il nostro Team in torneo.' }[lv] ||
      { Potenza: 'Carbonio rigido e bilanciamento alto per smash e víbora.', Controllo: 'Bilanciamento basso e gomma morbida per piazzare la palla dove vuoi.', Polivalenti: 'Un equilibrio tra potenza e controllo, per ogni fase del gioco.' }[st];
    return ['Racchette ' + [T, L].filter(Boolean).join(' ') + '.', D];
  }

  function render() {
    var a = active(), shown = 0;
    cards.forEach(function (c) { var ok = match(c, a); c.hidden = !ok; if (ok) shown++; });
    var h = heading(a);
    $('rt').textContent = h[0]; $('rd').textContent = h[1];
    $('crumb').textContent = h[0] === DEF_T ? 'Racchette' : h[0].replace('.', '');
    $('count').textContent = shown === 1 ? '1 racchetta' : shown + ' racchette';
    $('empty').hidden = shown !== 0;
    var chips = $('chips'); chips.textContent = '';
    boxes.forEach(function (b) {
      if (!b.checked) return;
      var ch = document.createElement('button');
      ch.type = 'button'; ch.className = 'chip'; ch.textContent = b.value;
      ch.setAttribute('aria-label', 'Togli il filtro ' + b.value);
      ch.addEventListener('click', function () { b.checked = false; render(); });
      chips.appendChild(ch);
    });
    var slugs = boxes.filter(function (b) { return b.checked && b.getAttribute('data-slug'); }).map(function (b) { return b.getAttribute('data-slug'); }).join('/');
    try { if (location.hash.slice(1) !== slugs) history.replaceState(null, '', slugs ? '#' + slugs : location.pathname + location.search); } catch (e) {}
  }
  function fromHash() {
    var parts = location.hash.slice(1).split('/').filter(Boolean);
    boxes.forEach(function (b) { b.checked = false; });
    parts.forEach(function (p) { boxes.forEach(function (b) { if (b.getAttribute('data-slug') === p) b.checked = true; }); });
  }

  /* confronto */
  function byslug(s) { return cards.filter(function (c) { return c.getAttribute('data-slug') === s; })[0]; }
  function nameOf(c) { return c.querySelector('h2').textContent; }
  function renderCmp() {
    var tray = $('ctray');
    tray.hidden = cmp.length === 0;
    $('cn').textContent = cmp.length;
    var th = $('cth'); th.textContent = '';
    cmp.forEach(function (s) { var i = document.createElement('img'); i.src = byslug(s).getAttribute('data-img'); i.alt = ''; th.appendChild(i); });
    $('ctx').textContent = cmp.length + (cmp.length === 1 ? ' racchetta' : ' racchette') + ' · max 4';
    cards.forEach(function (c) {
      var on = cmp.indexOf(c.getAttribute('data-slug')) !== -1;
      c.querySelector('.cmp').setAttribute('aria-pressed', on ? 'true' : 'false');
    });
  }
  grid.addEventListener('click', function (e) {
    var b = e.target.closest('.cmp');
    if (!b) return;
    e.preventDefault();
    var s = b.closest('.pc').getAttribute('data-slug'), i = cmp.indexOf(s);
    if (i !== -1) cmp.splice(i, 1);
    else if (cmp.length < 4) cmp.push(s);
    else toast('Puoi confrontare al massimo 4 racchette.');
    renderCmp();
  });
  var dlg = $('cdlg');
  function openCmp() {
    if (cmp.length < 2) {
      toast('Scegli almeno 2 racchette con il pulsante Confronta.');
      grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
      return;
    }
    buildCmp();
    if (dlg.showModal) dlg.showModal(); else dlg.setAttribute('open', '');
  }
  function buildCmp() {
    var rows = [['Prezzo', function (c) { return eur(parseFloat(c.getAttribute('data-price'))); }],
      ['Livello', function (c) { return c.getAttribute('data-lv'); }],
      ['Stile di gioco', function (c) { return c.getAttribute('data-st'); }],
      ['Collezione', function (c) { return c.getAttribute('data-co') || '—'; }],
      ['Linea', function (c) { return c.getAttribute('data-li'); }],
      ['Carbonio', function (c) { return c.getAttribute('data-k'); }],
      ['Peso', function (c) { return c.getAttribute('data-w'); }]];
    var cs = cmp.map(byslug);
    var t = document.createElement('table'); t.className = 'ct';
    var thead = '<thead><tr><td></td>' + cs.map(function (c) {
      return '<th scope="col"><img src="' + c.getAttribute('data-img') + '" alt=""><span>' + nameOf(c) + '</span><br><button type="button" class="rm" data-s="' + c.getAttribute('data-slug') + '">Rimuovi</button></th>';
    }).join('') + '</tr></thead>';
    var tbody = '<tbody>' + rows.map(function (r) {
      return '<tr><th scope="row">' + r[0] + '</th>' + cs.map(function (c) { return '<td>' + r[1](c) + '</td>'; }).join('') + '</tr>';
    }).join('') + '</tbody>';
    t.innerHTML = thead + tbody;
    var wrap = document.createElement('div'); wrap.className = 'cmp-s'; wrap.appendChild(t);
    var body = $('cdb'); body.textContent = ''; body.appendChild(wrap);
    var n = document.createElement('p'); n.className = 'note';
    n.textContent = 'Livello e stile di gioco sono di esempio: quelli veri li indicherà T91.';
    body.appendChild(n);
  }
  $('cdb').addEventListener('click', function (e) {
    var r = e.target.closest('.rm'); if (!r) return;
    var i = cmp.indexOf(r.getAttribute('data-s')); if (i !== -1) cmp.splice(i, 1);
    renderCmp();
    if (cmp.length < 2) { if (dlg.close) dlg.close(); toast('Servono almeno 2 racchette per il confronto.'); } else buildCmp();
  });
  dlg.addEventListener('click', function (e) { if (e.target === dlg && dlg.close) dlg.close(); });
  $('cdc').addEventListener('click', function () { if (dlg.close) dlg.close(); });
  $('cbtn').addEventListener('click', openCmp);
  $('cgo').addEventListener('click', openCmp);
  $('ocmp').addEventListener('click', openCmp);
  $('cclear').addEventListener('click', function () { cmp = []; renderCmp(); });

  /* filtri e ordinamento */
  boxes.forEach(function (b) { b.addEventListener('change', render); });
  $('sort').addEventListener('change', function () { order(); render(); });
  function reset() { boxes.forEach(function (b) { b.checked = false; }); render(); }
  $('reset').addEventListener('click', reset);
  $('reset2').addEventListener('click', reset);
  $('fbtn').addEventListener('click', function () {
    var open = $('filters').classList.toggle('open');
    $('fbtn').setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  window.addEventListener('hashchange', function () { fromHash(); render(); });
  $('qf').addEventListener('submit', function (e) { e.preventDefault(); toast('Il test arriva presto (prototipo).'); });

  fromHash();
  if (boxes.some(function (b) { return b.checked; })) { $('filters').classList.add('open'); $('fbtn').setAttribute('aria-expanded', 'true'); }
  render(); renderCmp();
})();
