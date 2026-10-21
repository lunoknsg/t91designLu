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
    map.createPane('lab'); map.getPane('lab').style.zIndex = 450; map.getPane('lab').style.pointerEvents = 'none';
    fetch('assets/mondo.geo.json').then(function (r) { return r.json(); }).then(function (g) {
      L.geoJSON(g, { interactive: false, style: { color: '#ffffff', weight: 0.7, opacity: 0.9, fillColor: '#0d0d0d', fillOpacity: 1 } }).addTo(map);
    });
    var prov = L.geoJSON(null, { interactive: false, style: { color: '#ffffff', weight: 0.5, opacity: 0.28, fill: false } });
    var reg = L.geoJSON(null, { interactive: false, style: { color: '#ffffff', weight: 0.9, opacity: 0.55, fill: false } });
    fetch('assets/it-province.geo.json').then(function (r) { return r.json(); }).then(function (g) { prov.addData(g); sync(); });
    fetch('assets/it-regioni.geo.json').then(function (r) { return r.json(); }).then(function (g) {
      reg.addData(g);
      g.features.forEach(function (f) {
        var c = L.geoJSON(f).getBounds().getCenter(), n = f.properties.n.replace(/\/.*$/, '').replace("Valle d'Aosta", "Valle d'Aosta");
        labels.push(mk(n, c.lat, c.lng, 6, 'rg'));
      });
      sync();
    });
    var labels = [];
    function mk(text, lat, lng, min, cls, max) {
      var m = L.marker([lat, lng], { pane: 'lab', interactive: false, keyboard: false, icon: L.divIcon({ className: 'mlb ' + cls, html: '<span>' + text + '</span>', iconSize: null }) });
      m._min = min; m._max = max || 99; return m;
    }
    function sync() {
      var z = map.getZoom();
      if (z >= 7) { if (!map.hasLayer(prov)) prov.addTo(map); } else if (map.hasLayer(prov)) map.removeLayer(prov);
      if (z >= 5) { if (!map.hasLayer(reg)) reg.addTo(map); } else if (map.hasLayer(reg)) map.removeLayer(reg);
      labels.forEach(function (m) {
        var on = z >= m._min && z <= m._max;
        if (on && !map.hasLayer(m)) m.addTo(map); else if (!on && map.hasLayer(m)) map.removeLayer(m);
      });
    }
    var C = [['Italia', 42.9, 12.6, 3, 7], ['Francia', 46.6, 2.6, 3], ['Spagna', 40.2, -3.7, 3], ['Portogallo', 39.5, -8, 4], ['Germania', 51.2, 10.4, 3], ['Svizzera', 46.85, 8.2, 5], ['Austria', 47.6, 14.4, 5], ['Slovenia', 46.1, 14.8, 6], ['Croazia', 45.3, 16, 5], ['Bosnia ed Erzegovina', 44.2, 17.8, 6], ['Serbia', 44, 20.8, 5], ['Ungheria', 47.2, 19.4, 5], ['Repubblica Ceca', 49.8, 15.5, 5], ['Slovacchia', 48.7, 19.6, 6], ['Polonia', 52, 19.4, 4], ['Romania', 45.9, 25, 4], ['Bulgaria', 42.8, 25.3, 5], ['Grecia', 39.3, 22, 5], ['Albania', 41.1, 20.1, 6], ['Montenegro', 42.75, 19.3, 7], ['Macedonia del Nord', 41.6, 21.7, 7], ['Kosovo', 42.6, 20.9, 8], ['Regno Unito', 54, -2.5, 4], ['Irlanda', 53.2, -8, 4], ['Belgio', 50.6, 4.7, 6], ['Paesi Bassi', 52.2, 5.6, 6], ['Danimarca', 56, 9.5, 4], ['Svezia', 62, 15, 3], ['Norvegia', 61, 9, 3], ['Ucraina', 49, 31.4, 4], ['Turchia', 39, 35, 4], ['Tunisia', 34, 9.5, 4], ['Algeria', 28.5, 2, 3], ['Marocco', 31.8, -6.5, 4], ['Libia', 28, 17, 3], ['Egitto', 26.5, 30, 3], ['Malta', 35.6, 14.4, 8], ['Singapore', 3.2, 103.8, 3, 4]];
    C.forEach(function (c) { labels.push(mk(c[0], c[1], c[2], c[3], 'co', c[4])); });
    var SEA = [['Oceano Atlantico', 41, -16, 3], ['Mar Mediterraneo', 36.6, 17.5, 3], ['Mar Tirreno', 39.9, 12, 6], ['Mare Adriatico', 43.1, 15.4, 6], ['Mar Ionio', 38.3, 18.4, 6], ['Mar Ligure', 43.7, 8.6, 7], ['Mar Egeo', 38.9, 25.1, 6], ['Mar Nero', 43.4, 34, 4], ['Mare del Nord', 56, 3, 4], ['Golfo del Leone', 42.9, 4.4, 6]];
    SEA.forEach(function (c) { labels.push(mk(c[0], c[1], c[2], c[3], 'sea')); });
    var CT = [['Roma', 41.9, 12.5, 4], ['Milano', 45.46, 9.19, 4], ['Torino', 45.07, 7.69, 5], ['Napoli', 40.85, 14.27, 5], ['Firenze', 43.77, 11.25, 5], ['Bologna', 44.49, 11.34, 5], ['Venezia', 45.44, 12.32, 5], ['Genova', 44.41, 8.93, 5], ['Palermo', 38.12, 13.36, 5], ['Cagliari', 39.22, 9.12, 5], ['Bari', 41.12, 16.87, 5], ['Verona', 45.44, 10.99, 6], ['Parigi', 48.86, 2.35, 4], ['Madrid', 40.42, -3.7, 4], ['Barcellona', 41.39, 2.17, 4], ['Berlino', 52.52, 13.4, 4], ['Monaco di Baviera', 48.14, 11.58, 5], ['Vienna', 48.21, 16.37, 4], ['Zurigo', 47.38, 8.54, 5], ['Lione', 45.76, 4.84, 5], ['Marsiglia', 43.3, 5.37, 5], ['Lubiana', 46.06, 14.51, 6], ['Zagabria', 45.81, 15.98, 5], ['Budapest', 47.5, 19.04, 5], ['Praga', 50.08, 14.44, 5], ['Belgrado', 44.79, 20.45, 5], ['Tirana', 41.33, 19.82, 6], ['Atene', 37.98, 23.73, 5], ['Sofia', 42.7, 23.32, 5], ['Bucarest', 44.43, 26.1, 5], ['Londra', 51.51, -0.13, 4], ['Bruxelles', 50.85, 4.35, 5], ['Amsterdam', 52.37, 4.9, 5], ['Lisbona', 38.72, -9.14, 4], ['Singapore', 1.35, 103.82, 4],
      ['Trieste', 45.65, 13.78, 6], ['Udine', 46.06, 13.24, 7], ['Trento', 46.07, 11.12, 7], ['Bolzano', 46.5, 11.35, 7], ['Brescia', 45.54, 10.22, 7], ['Bergamo', 45.7, 9.67, 7], ['Como', 45.81, 9.09, 7], ['Parma', 44.8, 10.33, 7], ['Modena', 44.65, 10.93, 7], ['Ravenna', 44.42, 12.2, 7], ['Ancona', 43.62, 13.52, 6], ['Perugia', 43.11, 12.39, 6], ['Pescara', 42.46, 14.21, 6], ['Catania', 37.5, 15.09, 6], ['Messina', 38.19, 15.55, 7], ['Reggio Calabria', 38.11, 15.65, 7], ['Cosenza', 39.3, 16.25, 7], ['Taranto', 40.47, 17.24, 7], ['Pisa', 43.72, 10.4, 7], ['Livorno', 43.55, 10.31, 7], ['Cuneo', 44.38, 7.54, 7], ['Sassari', 40.73, 8.56, 7], ['Olbia', 40.92, 9.5, 7], ['Rimini', 44.06, 12.57, 7], ['Padova', 45.41, 11.88, 7], ['Vicenza', 45.55, 11.55, 8], ['Aosta', 45.74, 7.32, 7], ['Savona', 44.31, 8.48, 8], ['Latina', 41.47, 12.9, 7], ['Salerno', 40.68, 14.77, 7], ['Potenza', 40.64, 15.8, 7], ['Campobasso', 41.56, 14.66, 7], ["L'Aquila", 42.35, 13.4, 7], ['Terni', 42.56, 12.64, 8], ['Siracusa', 37.08, 15.29, 7]];
    CT.forEach(function (c) { labels.push(mk(c[0], c[1], c[2], c[3], 'ct')); });
    map.on('zoomend', sync); sync();
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
