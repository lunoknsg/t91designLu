"""Pagina prodotto: Boss One K12 Pro Master 6.0.

Contenuti: scheda ufficiale dal catalogo T91 + blocchi dal mockup
https://noknok-web.github.io/T91_F/T91_mockup_pagina_prodotto.html
I dati del mockup non verificati sono segnalati nella pagina.
"""

NAME = "Boss One K12 Pro Master 6.0"
PRICE = 328.90

GALLERY = [
    ("assets/racchette/boss-one-k12-pro-master.jpg", "Boss One K12 Pro Master 6.0, vista frontale"),
    ("assets/prodotto/g2-tre-quarti.jpg", "Boss One K12 Pro Master 6.0, tre quarti"),
    ("assets/prodotto/g3-profilo.jpg", "Boss One K12 Pro Master 6.0, profilo del telaio"),
    ("assets/prodotto/g4-piatto.jpg", "Dettaglio del piatto sabbiato in carbonio 12K"),
    ("assets/prodotto/g5-gola.jpg", "Dettaglio della gola e del ponte nero"),
    ("assets/prodotto/g6-impugnatura.jpg", "Impugnatura con overgrip e laccio"),
    ("assets/prodotto/g7-azione.jpg", "Giocatore in smash con la Boss One K12"),
    ("assets/prodotto/g8-set.jpg", "Racchetta, borsone, cappellino e overgrip T91"),
]

ICON = {
    "truck": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M2 6h12v10H2zM14 9h4l3 3v4h-7"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/></svg>',
    "return": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M4 9h11a5 5 0 010 10H8M4 9l4-4M4 9l4 4"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5L16 9.5"/></svg>',
    "lock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="5" y="11" width="14" height="9"/><path d="M8 11V8a4 4 0 018 0v3"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M12 21s7-6.2 7-11a7 7 0 10-14 0c0 4.8 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M4 5h16v11H9l-5 4z"/></svg>',
    "prev": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>',
    "next": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>',
}
STAR = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.8l2.8 6 6.5.7-4.9 4.4 1.4 6.4L12 17l-5.8 3.3 1.4-6.4L2.7 9.5l6.5-.7z"/></svg>'


def eur(v):
    return "&euro;" + ("%.2f" % v).replace(".", ",")


def stars(n=5):
    return '<span class="stars" role="img" aria-label="5 stelle su 5">' + STAR * n + "</span>"


REVIEWS = [
    ("Francesco P.", "24/08/26", "Feeling dal primo momento", "Pala solida e ben fatta, il contatto con la pallina dà tanto controllo, e quando serve potenza risponde subito presente.", "Huracán 2.0"),
    ("Davide P.", "21/08/26", "Leggera e super maneggevole", "Bilanciamento ottimo, grafica stupenda. La consiglio a chi vuole il massimo del controllo.", "Huracán 2.0"),
    ("Stefano C.", "30/08/26", "Arrivata in un paio di giorni", "Mi trovo bene, devo ancora imparare a domarla. Ottima in difesa sui blocchi e sui pallonetti.", "Huracán 2.0"),
    ("Alessandro P.", "23/07/26", "Servizio clienti ai massimi", "Pala e servizio clienti ai massimi livelli.", "Huracán 2.0"),
]
DIST = [("5", 93), ("4", 5), ("3", 1), ("2", 0), ("1", 1)]

TECH = [
    ("Carbonio 12K", "Rigidità elevata: tutta l'energia va nella palla. Telaio rigido, risposta secca."),
    ("Piatto sabbiato", "Più aderenza per caricare effetto, anche nei colpi veloci."),
    ("Black EVA Hard Pro Power", "Uscita di palla esplosiva e precisione nei colpi pieni."),
    ("Bilanciamento alto", "26,3-27,2 cm: massa in testa per smash e v&iacute;bora."),
]
CHAPTERS = [
    ("0:00", "Carbonio 12K: cosa cambia nello smash"),
    ("0:38", "Bilanciamento alto: come gestirlo in difesa"),
    ("1:12", "Per chi è (e per chi no)"),
]
SPEC = [
    ("Telaio", "Fibra di carbonio 12K"),
    ("Piatto", "Sabbiato"),
    ("Gomma", "Black EVA Hard Pro"),
    ("Peso", "356-365 g, o a scelta"),
    ("Bilanciamento", "Alto, 26,3-27,2 cm"),
    ("Livello", "Avanzato / Pro"),
]
METERS = [("Potenza", 10), ("Controllo", 6), ("Maneggevolezza", 6), ("Comfort", 5)]
SET = [
    ("Boss One K12 Pro Master 6.0", "Arancione Holo", 328.90, "assets/racchette/boss-one-k12-pro-master.jpg"),
    ("Borsa isotermica XL 2.0", "Arancione e nero", 129.90, "assets/prodotto/a-borsone.jpg"),
    ("Ultra Performance Cap 2.0", "Nero", 28.90, "assets/prodotto/a-cap.jpg"),
    ("Overgrip 2.0", "Nero", 3.50, "assets/prodotto/a-overgrip.jpg"),
]
TOGETHER = [
    ("Boss One K12 6.0", 328.90, "assets/racchette/boss-one-k12-pro-master.jpg", True),
    ("Overgrip 2.0", 3.50, "assets/prodotto/a-overgrip.jpg", False),
    ("Copritesta", 7.90, "assets/prodotto/a-copritesta.jpg", False),
]
LOOK = [
    ("Halo T-shirt", 49.90, "assets/prodotto/a-tshirt.jpg"),
    ("Halo Short", 44.90, "assets/prodotto/a-short.jpg"),
    ("Calza Total Grip", 20.90, "assets/prodotto/a-calza.jpg"),
    ("Thermo Pro Backpack", 98.90, "assets/prodotto/a-zaino.jpg"),
]
COMPARE = [
    ("Boss One K12 Pro Master 6.0", "assets/racchette/boss-one-k12-pro-master.jpg", "Carbonio 12K", "EVA Hard Pro", "356-365 g", "Alto", True),
    ("Boss One K3 Pro Master", "assets/racchette/boss-one-k3-pro-master.jpg", "Carbonio 3K", "EVA Soft Power", "356-365 g", "Medio", False),
    ("Finder Pro Master K3", "assets/racchette/finder-pro-master-k3.jpg", "Carbonio 3K", "EVA Soft Power", "348-355 g", "Basso", False),
    ("Hurac&aacute;n 2.0 12K x Bubu", "assets/racchette/huracan-12k-bubu.jpg", "Carbonio 12K", "MultiEVA Hard Pro", "346-360 g", "Alto", False),
]
SIMILAR = [
    ("Boss One K3 Pro Master", "assets/racchette/boss-one-k3-pro-master.jpg", True),
    ("Finder Pro Master K3", "assets/racchette/finder-pro-master-k3.jpg", True),
    ("Hurac&aacute;n 2.0 12K x Bubu", "assets/racchette/huracan-12k-bubu.jpg", False),
    ("Hurac&aacute;n x Iriart 3.0", "assets/racchette/huracan-power-full-black-iriart.jpg", False),
    ("Boss One 18K 3.0 PWR", "assets/racchette/boss-one-18k-pwr.jpg", False),
]
SERVICES = [
    ("Ritiro usato", "T91 Care", "La tua vecchia pala, anche non T91, diventa uno sconto.", "In valutazione", "servizi.html#usato", "Valutala"),
    ("Riparazioni", "T91 Repair", "Ripariamo pale di qualsiasi marca.", "", "servizi.html#care", "Preventivo"),
    ("Ritiro in negozio", "Click &amp; Collect", "Ordini online, ritiri a Osio Sotto.", "In arrivo", "servizi.html#click-collect", "Punti di ritiro"),
    ("Personalizza", "Anche 1 pezzo", "Il tuo nome sul completo.", "", "servizi.html#personalizzazione", "Inizia"),
]
POSTS = [
    ("Guide", "6 min", "Come scegliere la racchetta per il tuo livello"),
    ("Novit&agrave;", "4 min", "Holo Collection: la nuova linea Master 6.0"),
    ("Tornei", "3 min", "Il Team T91 nel weekend: i risultati"),
]


def pcard(name, price, img, extra="", href="#", sub=""):
    s = f'<p class="pc-s">{sub}</p>' if sub else ""
    return (f'<li class="pc"><div class="pc-ph"><a class="pc-img" href="{href}" tabindex="-1" aria-hidden="true"><img src="{img}" alt="" loading="lazy"></a></div>'
            f'<a class="pc-m" href="{href}"><h3>{name}</h3>{s}<p class="pc-p">{eur(price)}{extra}</p></a></li>')


def render(head, header, footer, arrow, ver):
    A = arrow
    CURA = ' aria-current="true"'
    thumbs = "".join(
        f'<button type="button" class="th" data-i="{i}" aria-label="Immagine {i + 1} di {len(GALLERY)}"{CURA if i == 0 else ""}><img src="{src}" alt="" loading="lazy"></button>'
        for i, (src, alt) in enumerate(GALLERY)
    )
    gdata = "|".join(f"{src}~{alt}" for src, alt in GALLERY)
    rev_list = "".join(
        f'<li class="rv"><div class="rv-h"><span class="av" aria-hidden="true">{"".join(w[0] for w in n.split()[:2])}</span><div><b>{n}</b><span class="mut">Acquisto verificato</span></div>{stars()}</div>'
        f'<h3>{t}</h3><p>{b}</p><p class="rv-m">Acquistato: {p} &middot; {d}</p></li>'
        for n, d, t, b, p in REVIEWS
    )
    bars = "".join(f'<li><span>{k}&#9733;</span><span class="bar"><i style="width:{v}%"></i></span><span class="n">{v}%</span></li>' for k, v in DIST)
    tech = "".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in TECH)
    chapters = "".join(f'<li><span class="tm">{t}</span><span>{c}</span></li>' for t, c in CHAPTERS)
    spec = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in SPEC)
    meters = "".join(
        f'<li><span class="ml">{k}</span><span class="mt" role="img" aria-label="{k}: {v} su 10"><i style="width:{v * 10}%"></i></span><span class="mv">{v}</span></li>'
        for k, v in METERS
    )
    set_total = sum(x[2] for x in SET)
    set_items = "".join(
        f'<li><img src="{img}" alt="" loading="lazy"><div><b>{n}</b><span class="mut">{c}</span></div><span class="pr">{eur(p)}</span></li>'
        for n, c, p, img in SET
    )
    tog = ""
    for i, (n, p, img, on) in enumerate(TOGETHER):
        chk = "checked disabled" if on else "checked"
        tog += (f'<li class="tg"><label class="tgl" for="tg{i}"><input type="checkbox" id="tg{i}" data-p="{p}" {chk}><span class="box" aria-hidden="true"></span>'
                f'<img src="{img}" alt="" loading="lazy"><b>{n}</b><span class="pr">{eur(p)}</span></label></li>')
    tog_total = sum(x[1] for x in TOGETHER)
    look = "".join(pcard(n, p, img) for n, p, img in LOOK)
    similar = "".join(pcard(n, PRICE, img, extra='<span class="mut"> &middot; o 3 &times; &euro;109,63</span>', sub="Novit&agrave;" if nw else "") for n, img, nw in SIMILAR)
    CC = ' class="cur"'
    cmp_head = "".join(f'<th scope="col"{CC if cur else ""}><img src="{img}" alt="" loading="lazy"><span>{n}</span></th>' for n, img, *_r, cur in COMPARE)
    def row(label, idx, fmt=lambda x: x):
        return '<tr><th scope="row">' + label + "</th>" + "".join("<td" + (CC if c[-1] else "") + ">" + str(fmt(c[idx])) + "</td>" for c in COMPARE) + "</tr>"
    cmp_rows = (row("Prezzo", 0, lambda _x: eur(PRICE)) + row("Telaio", 2) + row("Gomma", 3) + row("Peso", 4) + row("Bilanciamento", 5))
    services = ""
    for t, k, d, tag, h, cta in SERVICES:
        tg = '<span class="tag">' + tag + "</span>" if tag else ""
        services += f'<li><a href="{h}"><span class="sv-k">{k}</span><h3>{t}{tg}</h3><p>{d}</p><span class="sv-go">{cta} {A}</span></a></li>'
    chapters_html = chapters
    posts = "".join(f'<li><a href="#"><span class="cap mut">{c} &middot; {m}</span><h3>{t}</h3></a></li>' for c, m, t in POSTS)

    return head("Boss One K12 Pro Master 6.0 | T91 Padel", "Boss One K12 Pro Master 6.0: carbonio 12K, bilanciamento alto, piatto sabbiato. Per chi gioca per chiudere il punto.") + header("racchette") + f"""
<div class="wrap">
<nav class="crumb" aria-label="Percorso"><a href="index.html">Home</a><span aria-hidden="true">/</span><a href="racchette.html">Racchette</a><span aria-hidden="true">/</span><span aria-current="page">{NAME}</span></nav>

<section class="pdp" aria-labelledby="pdp-h">
<div class="gal" id="gal" data-g="{gdata}">
<div class="thumbs" id="thumbs">{thumbs}</div>
<div class="stage" id="stage">
<span class="bdg"><i>Novit&agrave;</i><i class="k">Holo</i></span>
<img id="gmain" src="{GALLERY[0][0]}" alt="{GALLERY[0][1]}">
<button type="button" class="gn prev" id="gprev" aria-label="Immagine precedente">{ICON["prev"]}</button>
<button type="button" class="gn next" id="gnext" aria-label="Immagine successiva">{ICON["next"]}</button>
<span class="gcount" id="gcount" aria-live="polite">1 / {len(GALLERY)}</span>
</div>
</div>

<div class="buy" id="buy">
<a class="rate" href="#recensioni">{stars()}<span><b>4,9</b> &middot; 770 recensioni</span></a>
<h1 id="pdp-h" class="d d-l">Boss One K12<br>Pro Master 6.0</h1>
<p class="lede">Per chi gioca per chiudere il punto: carbonio 12K, bilanciamento alto, smash esplosivi.</p>
<div class="price"><span class="now" id="price" data-base="{PRICE}">{eur(PRICE)}</span><span class="klarna" id="klarna">oppure 3 rate da &euro;109,63 senza interessi con Klarna</span></div>
<p class="club">T91 Club: la pagheresti <b id="club">&euro;230,23</b></p>

<fieldset class="opt"><legend>Colore</legend>
<div class="sw"><span class="dot" aria-hidden="true"></span><b>Arancione Holo</b><a href="racchette.html">Altri modelli Holo</a></div>
</fieldset>

<fieldset class="opt"><legend>Peso</legend>
<div class="wopts">
<label class="wo"><input type="radio" name="peso" value="0" checked><span class="box" aria-hidden="true"></span><span><b>Standard</b><small>356-365 g &middot; incluso</small></span></label>
<label class="wo"><input type="radio" name="peso" value="10"><span class="box" aria-hidden="true"></span><span><b>Scelta del peso</b><small>grammo esatto &middot; +&euro;10</small></span></label>
</div>
<div class="wg" id="wg" hidden role="group" aria-label="Grammi">
<button type="button" class="chipw" aria-pressed="true">356 g</button><button type="button" class="chipw" aria-pressed="false">360 g</button><button type="button" class="chipw" aria-pressed="false">365 g</button>
</div>
</fieldset>

<div class="cta">
<button type="button" class="btn solid wide" id="add">Aggiungi al carrello {A}</button>
<a class="expert" href="#">{ICON["chat"]}Dubbi? Chiedi a un T91 Expert</a>
</div>
<p class="pickup">{ICON["pin"]}<span>Ritiro gratis a Osio Sotto <span class="tag">In arrivo</span></span></p>

<fieldset class="opt care"><legend>Proteggi la tua racchetta con T91 Care</legend>
<div class="plans2">
<label class="pl"><input type="radio" name="care" value="0" checked><span class="box" aria-hidden="true"></span><span><b>Nessuna protezione</b></span><span class="pr">&nbsp;</span></label>
<label class="pl"><input type="radio" name="care" value="39.90"><span class="box" aria-hidden="true"></span><span><b>Break</b><small>Sostituzione in caso di rottura</small></span><span class="pr">&euro;39,90</span></label>
<label class="pl"><input type="radio" name="care" value="59.90"><span class="box" aria-hidden="true"></span><span><b>Crash</b><small>Rottura accidentale, caduta, scheggiatura</small></span><span class="pr">&euro;59,90</span></label>
<label class="pl"><input type="radio" name="care" value="109"><span class="box" aria-hidden="true"></span><span><b>Total 2 anni</b><small>Protezione di 2 anni sull'acquisto</small></span><span class="pr">&euro;109</span></label>
</div>
<p class="fine"><span class="todo">Condizioni da confermare</span> <a href="garanzie.html">Come funziona</a></p>
</fieldset>

<ul class="trust">
<li>{ICON["truck"]}Spedizione gratuita</li><li>{ICON["return"]}Reso 30 giorni</li><li>{ICON["shield"]}Garanzia 2 anni</li><li>{ICON["lock"]}Pagamento sicuro</li>
</ul>
<p class="note">Bozza: valutazioni, rate Klarna, T91 Club, ritiro a Osio Sotto, spedizione e reso vengono dal mockup e vanno confermati con T91.</p>
</div>
</section>
</div>

<section class="dark n1" aria-labelledby="n1-h">
<div class="n1-img"><img src="assets/prodotto/g7-azione.jpg" alt="Giocatore in smash con la Boss One K12" loading="lazy"></div>
<div class="n1-t">
<h2 id="n1-h" class="d d-l">La pala del n.1 in Italia.</h2>
<p class="lede">Nome Cognome, n.1 del ranking italiano, gioca la Boss One K12 Pro Master 6.0 in ogni torneo.</p>
<blockquote>&laquo;Quando devo chiudere il punto voglio una pala che non perdona. Questa non perdona.&raquo;<cite>Nome Cognome &middot; Team T91 Pro</cite></blockquote>
<p class="note inv">Da inserire: nome dell'atleta, conferma del ranking e della citazione.</p>
<div class="btns"><a class="btn line" href="#">Scopri il Team {A}</a></div>
</div>
</section>

<section class="wrap rvs" id="recensioni" aria-labelledby="rv-h">
<div class="rvs-s">
<h2 id="rv-h" class="d d-m">Cosa dicono i giocatori</h2>
<div class="big4"><b>4,9</b>{stars()}<span class="mut">770 recensioni verificate</span></div>
<ul class="dist">{bars}</ul>
<p class="mut small">I clienti parlano di consegna in 24-48 ore, qualit&agrave; dei materiali e di un'assistenza personale e reattiva.</p>
<button type="button" class="btn line" disabled>Scrivi una recensione</button>
</div>
<div class="rvs-l">
<ul class="rvlist">{rev_list}</ul>
<p class="note">Recensioni di esempio dal mockup (acquistano altri modelli): sostituire con le recensioni verificate della Boss One K12.</p>
</div>
</section>

<section class="wrap tech" aria-labelledby="tech-h">
<div class="tech-i"><img src="assets/prodotto/g4-piatto.jpg" alt="Dettaglio del piatto sabbiato in carbonio 12K" loading="lazy"></div>
<div class="tech-t">
<h2 id="tech-h" class="d d-l">Dentro la Boss One.</h2>
<ul class="tl">{tech}</ul>
<div class="desc">
<p>La Boss One K12 Pro Master 6.0 &egrave; l'interpretazione pi&ugrave; aggressiva della linea Master: una racchetta costruita per chi gioca per chiudere il punto e cerca la massima potenza in ogni smash. La colorazione arancione ne esprime tutta l'energia e il carattere da attaccante puro.</p>
<p>Il peso di 356-365 g e il bilanciamento alto di 26,3-27,2 cm spostano la massa verso la testa della racchetta, per una spinta superiore in smash, v&iacute;bora e colpi di chiusura: la scelta per giocatori esperti che non accettano compromessi.</p>
</div>
</div>
</section>

<section class="wrap vid" aria-labelledby="vid-h">
<h2 id="vid-h" class="d d-m">3 cose da sapere sulla Boss One K12</h2>
<ol class="chap">{chapters}</ol>
<p class="note">Video di 1:45 in arrivo: capitoli dal mockup.</p>
</section>

<section class="wrap specs" aria-labelledby="sp-h">
<div>
<h2 id="sp-h" class="d d-m">Scheda tecnica</h2>
<dl class="spec">{spec}</dl>
<div class="acc">
<details><summary>Cura del prodotto</summary><p>Usa sempre il copritesta, non lasciarla in auto al caldo, pulisci il piatto con un panno asciutto.</p></details>
<details><summary>Spedizione e resi</summary><p>Spedizione gratuita 24/48h in Italia. Reso gratuito entro 30 giorni.</p></details>
</div>
</div>
<div>
<h2 class="d d-m">Come gioca</h2>
<ul class="meters">{meters}</ul>
<h3 class="hs">Come impugnarla</h3>
<p>Impugnatura continental. Per smash e v&iacute;bora tieni la mano in fondo al manico.</p>
<p>In difesa sali di 1-2 cm: guadagni maneggevolezza senza perdere potenza.</p>
</div>
</section>

<section class="wrap bag" aria-labelledby="bag-h">
<div class="bag-i"><img src="assets/prodotto/g8-set.jpg" alt="Racchetta, borsone, cappellino e overgrip T91 su sfondo albicocca" loading="lazy"></div>
<div class="bag-t">
<h2 id="bag-h" class="d d-l">Cosa c'&egrave; nel mio borsone</h2>
<ul class="setl">{set_items}</ul>
<div class="settot"><span class="old">{eur(set_total)}</span><b>{eur(round(set_total * 0.9, 2))}</b><span class="tag">Set -10%</span></div>
<button type="button" class="btn solid" id="addset">Acquista il set {A}</button>
</div>
</section>

<section class="wrap tgs" aria-labelledby="tg-h">
<h2 id="tg-h" class="d d-m">Spesso comprati insieme</h2>
<ul class="tgl-l">{tog}</ul>
<div class="tgbox"><span class="mut">Totale</span><b id="tgtot">{eur(tog_total)}</b><button type="button" class="btn ink" id="addtg">Aggiungi tutti {A}</button></div>
</section>

<section class="wrap look" aria-labelledby="lk-h">
<h2 id="lk-h" class="d d-m">Completa il tuo look</h2>
<ul class="pgrid">{look}</ul>
</section>

<section class="wrap cmp" aria-labelledby="cm-h">
<h2 id="cm-h" class="d d-m">Confronta le pale</h2>
<div class="cmp-s"><table class="ct"><thead><tr><td></td>{cmp_head}</tr></thead><tbody>{cmp_rows}</tbody></table></div>
<p class="cmp-q">Ancora indeciso? <a href="#">Trova la tua racchetta</a><span class="mut"> &middot; 4 domande, risultato anche su WhatsApp</span></p>
</section>

<section class="wrap look" aria-labelledby="sm-h">
<h2 id="sm-h" class="d d-m">Pale simili</h2>
<ul class="pgrid five">{similar}</ul>
</section>

<section class="wrap svc2" aria-labelledby="ns-h">
<h2 id="ns-h" class="d d-m">Non solo racchette</h2>
<ul class="s4">{services}</ul>
</section>

<section class="dark help" aria-labelledby="hp-h">
<div class="wrap helpin">
<div><h2 id="hp-h" class="d d-l">Ti risponde un giocatore. Non un bot.</h2><p class="lede mut">Consulenza prima e dopo l'acquisto.</p></div>
<div class="btns"><a class="btn solid" href="#">WhatsApp {A}</a><a class="btn line" href="#">Chiamaci {A}</a></div>
</div>
</section>

<section class="wrap guides" aria-labelledby="bl-h">
<div class="shop-h"><h2 id="bl-h" class="d d-m">Dal blog</h2><a class="btn line" href="#">Tutti gli articoli {A}</a></div>
<ul class="glist">{posts}</ul>
</section>

<div class="sbar" id="sbar" aria-hidden="true">
<div class="sbar-t"><b>{NAME}</b><span id="sprice">{eur(PRICE)}</span><span class="mut">&middot; 3 rate Klarna</span></div>
<button type="button" class="btn solid" id="sadd" tabindex="-1">Aggiungi</button>
</div>
<div class="toast" id="toast" role="status" aria-live="polite" hidden></div>
""" + footer().replace("</body>", '<script src="js/pdp.js?v=' + ver + '"></script>\n</body>')
