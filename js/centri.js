(function () {
  var mapEl = document.getElementById('cmap');
  if (!mapEl) return;
  var $ = function (id) { return document.getElementById(id); };
  var list = $('clist'), q = $('q'), note = $('cmn');
  var centres = [], markers = {}, map, shown = [], userPos = null;

  function load(src, cb, isCss) {
    var el = document.createElement(isCss ? 'link' : 'script');
    if (isCss) { el.rel = 'stylesheet'; el.href = src; } else { el.src = src; el.onload = cb; }
    document.head.appendChild(el);
    if (isCss && cb) cb();
  }
  var esc = function (s) { return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var digits = function (p) { return p.replace(/[^\d]/g, ''); };
  var km = function (a, b) {
    var R = 6371, rad = Math.PI / 180, dLat = (b.lat - a.lat) * rad, dLng = (b.lng - a.lng) * rad;
    var x = Math.sin(dLat / 2) * Math.sin(dLat / 2) + Math.cos(a.lat * rad) * Math.cos(b.lat * rad) * Math.sin(dLng / 2) * Math.sin(dLng / 2);
    return 2 * R * Math.asin(Math.sqrt(x));
  };

  function itemHtml(c) {
    var d = c.dist != null ? '<span class="cm-d">' + Math.round(c.dist) + ' km</span>' : '';
    return '<li data-id="' + c.id + '"><div class="cm-t"><b>' + esc(c.name) + '</b>' + d + '</div><span class="cm-a">' + esc(c.loc) + '</span><span class="cm-ph">' + esc(c.phone) + '</span>' +
      '<div class="cm-b"><a class="cm-call" href="tel:' + c.phone.replace(/\s/g, '') + '">Chiama</a>' +
      '<a href="https://wa.me/' + digits(c.phone) + '" target="_blank" rel="noopener">WhatsApp</a>' +
      '<a href="https://www.google.com/maps/dir/?api=1&destination=' + c.lat + ',' + c.lng + '" target="_blank" rel="noopener">Indicazioni</a></div></li>';
  }

  function render() {
    var v = q.value.trim().toLowerCase();
    shown = centres.filter(function (c) { return !v || (c.name + ' ' + c.loc).toLowerCase().indexOf(v) !== -1; });
    if (userPos) shown.sort(function (a, b) { return a.dist - b.dist; });
    list.innerHTML = shown.length ? shown.map(itemHtml).join('') : '<li class="cm-e">Nessun centro trovato. Ne stiamo aggiungendo.</li>';
    note.textContent = shown.length === centres.length ? centres.length + ' centri partner in Italia e in Europa' : shown.length + (shown.length === 1 ? ' centro trovato' : ' centri trovati');
    Object.keys(markers).forEach(function (id) {
      var on = shown.some(function (c) { return String(c.id) === id; });
      markers[id].setOpacity(on ? 1 : 0.18);
      markers[id].setZIndexOffset(on ? 200 : 0);
    });
    if (map && v && shown.length) fit(shown);
    if (map && !v && !userPos) map.setView([44.2, 11], window.innerWidth < 800 ? 4 : 5);
  }
  function fit(arr) {
    if (arr.length === 1) { map.setView([arr[0].lat, arr[0].lng], 7); return; }
    map.fitBounds(L.latLngBounds(arr.map(function (c) { return [c.lat, c.lng]; })), { padding: [40, 40], maxZoom: 7 });
  }

  function init() {
    map = L.map(mapEl, { zoomControl: true, scrollWheelZoom: false, worldCopyJump: false, minZoom: 3, maxZoom: 9, attributionControl: false }).setView([44.2, 11], window.innerWidth < 800 ? 4 : 5);
    map.getContainer().style.background = '#0a1c3d';
    fetch('assets/mondo.geo.json').then(function (r) { return r.json(); }).then(function (g) {
      L.geoJSON(g, { interactive: false, style: { color: '#ffffff', weight: 0.7, opacity: 0.9, fillColor: '#0d0d0d', fillOpacity: 1 } }).addTo(map);
    });
    var icon = L.divIcon({ className: 'cm-pin', html: '<i></i>', iconSize: [22, 22], iconAnchor: [11, 11] });
    centres.forEach(function (c) {
      var m = L.marker([c.lat, c.lng], { icon: icon, title: c.name, keyboard: true }).addTo(map);
      m.on('click', function () { select(c.id, true); });
      markers[c.id] = m;
    });
    map.on('click', function () { map.scrollWheelZoom.enable(); });
    map.on('mouseout', function () { map.scrollWheelZoom.disable(); });
    render();
  }
  function select(id, fromMap) {
    var li = list.querySelector('li[data-id="' + id + '"]');
    Array.prototype.forEach.call(list.children, function (x) { x.classList.remove('on'); });
    Object.keys(markers).forEach(function (k) { var e = markers[k].getElement(); if (e) e.classList.remove('on'); });
    if (li) { li.classList.add('on'); if (fromMap) list.scrollTo({ top: li.offsetTop - list.offsetTop - 8, behavior: 'smooth' }); }
    var mk = markers[id]; if (mk && mk.getElement()) mk.getElement().classList.add('on');
  }
  list.addEventListener('click', function (e) {
    if (e.target.closest('a')) return;
    var li = e.target.closest('li[data-id]'); if (!li) return;
    var id = li.getAttribute('data-id'), c = centres.filter(function (x) { return String(x.id) === id; })[0];
    select(id, false);
    if (map) { map.flyTo([c.lat, c.lng], Math.max(map.getZoom(), 7), { duration: 0.8 }); }
    if (window.innerWidth < 900) mapEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
  });
  q.addEventListener('input', render);
  $('near').addEventListener('click', function () {
    var b = $('near');
    if (!navigator.geolocation) { note.textContent = 'Posizione non disponibile su questo dispositivo.'; return; }
    b.disabled = true; b.textContent = 'Cerco...';
    navigator.geolocation.getCurrentPosition(function (p) {
      userPos = { lat: p.coords.latitude, lng: p.coords.longitude };
      centres.forEach(function (c) { c.dist = km(userPos, c); });
      q.value = ''; render();
      fit(shown.slice(0, 3));
      note.textContent = 'Il centro più vicino: ' + shown[0].name + ', a ' + Math.round(shown[0].dist) + ' km';
      b.disabled = false; b.textContent = 'Vicino a me';
    }, function () {
      note.textContent = 'Non riesco a leggere la tua posizione. Cerca per città.';
      b.disabled = false; b.textContent = 'Vicino a me';
    }, { timeout: 8000 });
  });

  fetch('assets/centri.json').then(function (r) { return r.json(); }).then(function (d) {
    centres = d;
    list.innerHTML = centres.map(itemHtml).join('');
    var go = function () { init(); };
    load('assets/vendor/leaflet.css', null, true);
    if (window.L) go(); else load('assets/vendor/leaflet.js', go);
  });
})();
