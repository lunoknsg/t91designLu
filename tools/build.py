#!/usr/bin/env python3
"""Genera index.html, servizi.html, garanzie.html (prototipo statico T91 Padel)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VER = __import__("time").strftime("%Y%m%d%H%M")
CDN = "https://t91padel.com/cdn/shop/files/"
IMG_HOLO = "assets/ext/Racchetta_HOLO_arancione_in_carbonio_pc.webp"
IMG_HOLO_M = CDN + "Racchetta_HOLO_arancione_in_carbonio_cell.webp"
IMG_IRIART = CDN + "IRIART_3_COVER_PC_a5cd421b-ba5d-4364-9af6-ef683e77ac0d.webp"
IMG_BOSS = CDN + "BOSS_ONE_K12_5.0_COVER_PC_640x.webp"
LOGO = "assets/ext/Logo_T91_Nero.svg"
CAMP = "assets/campaign/"
IMG_DONNA = "assets/ext/Abbigliamento_Donna_Computer.webp"

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M3 12h17M14 6l6 6-6 6"/></svg>'

SERVICES = [
    ("personalizzazione", "Personalizzazione", "Il tuo nome, i tuoi colori sul prodotto. Anche per un solo pezzo: nessun minimo d'ordine.", ""),
    ("care", "T91 Care / Repair", "Riparazione delle racchette, anche di altri marchi.", ""),
    ("usato", "Ritiro usato", "Una racchetta che non usi più può tornare utile.", "In valutazione"),
    ("experience", "T91 Experience", "Eventi, test ed esperienze per incontrare il brand dal vivo.", ""),
    ("customer-care", "Customer care", "L'assistenza T91, resa visibile.", ""),
    ("click-collect", "Click &amp; Collect", "Compri online, ritiri in un centro T91.", "In arrivo"),
    ("garanzie", "Garanzie e protezione", "Le tre formule di protezione.", ""),
]


def head(title, desc):
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Big+Shoulders+Display:wght@700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/t91.css?v={VER}">
</head>
<body>
<a class="skip" href="#main">Vai ai contenuti</a>
<div class="strip"><span>Spedizione in tutto il mondo</span><span>From Players to players</span></div>
"""


def header(cur):
    def a(href, label, key):
        c = ' aria-current="page"' if cur == key else ""
        return f'<a href="{href}"{c}>{label}</a>'
    return f"""<header class="top"><div class="wrap">
<a class="logo" href="index.html" aria-label="T91 Padel, home"><img src="{LOGO}" alt="T91" width="64" height="51"></a>
<nav class="main" aria-label="Principale">
{a("racchette.html","Racchette","racchette")}
{a("index.html#shop","Abbigliamento","app")}
{a("servizi.html","Servizi","servizi")}
{a("garanzie.html","Garanzie","garanzie")}
{a("index.html#centri","Trova T91","centri")}
</nav>
<details class="mnav"><summary aria-label="Menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M3 7h18M3 12h18M3 17h18"/></svg></summary><div class="mpanel">{a("racchette.html","Racchette","racchette")}{a("index.html#shop","Abbigliamento","app")}{a("servizi.html","Servizi","servizi")}{a("garanzie.html","Garanzie","garanzie")}{a("index.html#centri","Trova T91","centri")}</div></details>
<div class="hdr-r"><a href="#">Accesso</a><a href="#">Cerca</a><a href="#">Carrello (0)</a></div>
</div></header>
<main id="main">
"""


def footer():
    return f"""</main>
<footer>
<div class="cols">
<div><a class="logo" href="index.html" aria-label="T91 Padel, home"><img class="inv" src="{LOGO}" alt="T91" width="96" height="76"></a><p style="margin-top:14px;max-width:30ch;color:#b4b3ad">From Players to players.</p></div>
<div><h3>Shop</h3><ul><li><a href="racchette.html">Racchette</a></li><li><a href="index.html#shop">Abbigliamento</a></li><li><a href="#">Buoni regalo</a></li></ul></div>
<div><h3>Servizi</h3><ul><li><a href="servizi.html#care">Care / Repair</a></li><li><a href="servizi.html#personalizzazione">Personalizzazione</a></li><li><a href="garanzie.html">Garanzie</a></li><li><a href="servizi.html#experience">Experience</a></li></ul></div>
<div><h3>Rete</h3><ul><li><a href="index.html#centri">Trova T91</a></li><li><a href="#">Programma centri</a></li><li><a href="#">Programma maestri</a></li><li><a href="#">Ambassador</a></li></ul></div>
</div>
<div class="base"><span>Prototipo di design. Foto di campagna generate con IA per il prototipo, da sostituire con uno shooting reale; altre immagini dal sito attuale t91padel.com. Testi dei servizi in bozza da validare.</span><span>&copy; T91 Padel</span></div>
</footer>
<script src="js/t91.js?v={VER}"></script>
</body>
</html>
"""


GO = ARROW.replace('<svg', '<svg class="go"')


def rows():
    out = []
    for sid, name, desc, tag in SERVICES:
        href = "garanzie.html" if sid == "garanzie" else f"servizi.html#{sid}"
        t = f'<span class="tag">{tag}</span>' if tag else ""
        out.append(f'<a class="row" href="{href}"><h3>{name}{t}</h3><p>{desc}</p>{GO}</a>')
    return "\n".join(out)


CENTRES = [
    ("Gpadel Borgaro", "Borgaro Torinese (TO)"),
    ("City Padel Golden Goose Arena", "Milano, CityLife"),
    ("Padel Indoor Baveno", "Baveno (VB)"),
    ("Padel Albaro", "Genova"),
    ("Country Padel", "Paderno Dugnano (MI)"),
    ("The Padel Resort Como", "Como"),
    ("Yep Padel", "Albano Sant'Alessandro (BG)"),
    ("Contra Padel", "Roma"),
    ("Colognola Racquet Club", "Bergamo"),
    ("Padel Prime", "Osio Sotto (BG)"),
    ("Tarta Padel", "Noto (SR), Sicilia"),
    ("Padel Poreč", "Poreč, Croazia"),
    ("The Padel Lab", "Biasca, Svizzera"),
    ("Padel Seasons", "Monaco di Baviera, Germania"),
]

RACKETS = [
    # slug, nome, handle, linea, carbonio, gioco, edizione, novita
    ("finder-pro-master-k3", "Finder Pro Master K3", "finder-pro-master-k3", "Finder Pro", "3K", "Controllo", "Master", True),
    ("boss-one-k3-pro-master", "Boss One K3 Pro Master", "boss-one-k3-pro-master", "Boss One", "3K", "Potenza", "Master", True),
    ("boss-one-k12-pro-master", "Boss One K12 Pro Master 6.0", "boss-one-k12-pro-master-6-0", "Boss One", "12K", "Potenza", "Master", True),
    ("huracan-power-full-black-iriart", "Hurac&aacute;n Power Full Black x Emiliano Iriart 3.0", "huracan-power-full-black-x-emiliano-iriart-3-0", "Hurac&aacute;n", "", "Potenza", "Con atleta", False),
    ("huracan-12k-bubu", "Hurac&aacute;n 2.0 12K x Bubu Salandro", "huracan-2-0-12k-x-bubu-salandro", "Hurac&aacute;n", "12K", "Potenza", "Con atleta", False),
    ("huracan-3k-bubu", "Hurac&aacute;n 2.0 3K x Bubu Salandro", "huracan-2-0-x-bubu-salandro", "Hurac&aacute;n", "3K", "Potenza", "Con atleta", False),
    ("finder-pro-k12-master", "Finder Pro K12 Master 5.0", "finder-pro-k12-master-5-0", "Finder Pro", "12K", "", "Master", False),
    ("huracan-2-0", "Hurac&aacute;n 2.0", "huracan-2-0", "Hurac&aacute;n", "", "Potenza", "Standard", False),
    ("boss-one-18k-pwr", "Boss One 18K 3.0 PWR", "boss-one-18k-3-0-pwr", "Boss One", "18K", "Potenza", "Standard", False),
    ("boss-one-12k-pwr", "Boss One 12K 3.0 PWR", "boss-one-12k-3-0-x-nick-remedi", "Boss One", "12K", "Potenza", "Con atleta", False),
    ("finder-pro-k12-pwr", "Finder Pro K12 3.0 PWR", "finder-pro-k12-3-0-pwr", "Finder Pro", "12K", "Potenza", "Standard", False),
]
PRICE = 328.9


def fmt_price(v):
    return ("%.2f" % v).replace(".", ",")


def fgroup(key, title, values):
    items = []
    for v in values:
        n = sum(1 for r in RACKETS if {"linea": r[3], "carbonio": r[4], "gioco": r[5], "edizione": r[6]}[key] == v)
        vid = f"f-{key}-{v.lower().replace(' ', '-').replace('&aacute;', 'a').replace('k', 'k')}"
        items.append(f'<label class="chk" for="{vid}"><input type="checkbox" id="{vid}" data-k="{key}" value="{v}"><span class="box" aria-hidden="true"></span><span class="lab">{v}</span><span class="n">{n}</span></label>')
    return f'<fieldset class="fg"><legend>{title}</legend>{"".join(items)}</fieldset>'


def racchette():
    cards = []
    for i, (slug, name, handle, linea, carb, gioco, ed, new) in enumerate(RACKETS):
        sub = " &middot; ".join(x for x in (linea, carb) if x)
        badge = '<span class="new">Novit&agrave;</span>' if new else ""
        tb = "" if slug == "boss-one-k12-pro-master" else ' target="_blank" rel="noopener"'
        url = "prodotto-boss-one-k12.html" if slug == "boss-one-k12-pro-master" else f"https://t91padel.com/products/{handle}"
        cards.append(f'''<li class="pc" data-name="{name.lower()}" data-linea="{linea}" data-carbonio="{carb}" data-gioco="{gioco}" data-edizione="{ed}" data-new="{1 if new else 0}" data-price="{PRICE}" data-i="{i}">
<div class="pc-ph">{badge}<a class="pc-img" href="{url}" {tb} tabindex="-1" aria-hidden="true"><img src="assets/racchette/{slug}.jpg" alt="" loading="{'eager' if i < 4 else 'lazy'}"></a><button class="pc-add" type="button" aria-label="Scegli il peso per {name}">Scegli il peso</button></div>
<a class="pc-m" href="{url}"{tb}><h2>{name}</h2><p class="pc-s">{sub}</p><p class="pc-p">Da &euro;{fmt_price(PRICE)}</p></a>
</li>''')
    filters = (fgroup("linea", "Linea", ["Boss One", "Finder Pro", "Hurac&aacute;n"])
               + fgroup("carbonio", "Carbonio", ["3K", "12K", "18K"])
               + fgroup("gioco", "Gioco", ["Potenza", "Controllo"])
               + fgroup("edizione", "Edizione", ["Master", "Con atleta", "Standard"]))
    return head("Racchette | T91 Padel", "Tutte le racchette da padel T91: Boss One, Finder Pro, Hurac&aacute;n. Filtra per linea, carbonio e gioco.") + header("racchette") + f"""
<div class="wrap">
<nav class="crumb" aria-label="Percorso"><a href="index.html">Home</a><span aria-hidden="true">/</span><span aria-current="page">Racchette</span></nav>
<div class="plp-h">
<h1 class="d d-l">Racchette</h1>
<p class="plp-c" id="count" aria-live="polite">{len(RACKETS)} prodotti</p>
</div>
<div class="plp-bar">
<button class="fbtn" type="button" id="fbtn" aria-expanded="false" aria-controls="filters">Filtri</button>
<div class="chips" id="chips" aria-label="Filtri attivi"></div>
<label class="sort" for="sort"><span>Ordina per</span>
<select id="sort"><option value="i">In evidenza</option><option value="new">Novit&agrave;</option><option value="az">Nome A-Z</option><option value="pa">Prezzo crescente</option><option value="pd">Prezzo decrescente</option></select></label>
</div>
<div class="plp">
<form class="filters" id="filters" aria-label="Filtri">{filters}<button class="reset" type="button" id="reset">Azzera filtri</button></form>
<div class="plp-r">
<ul class="pgrid" id="pgrid">
{"".join(cards)}
</ul>
<p class="plp-e" id="empty" hidden>Nessuna racchetta con questi filtri. <button class="reset inl" type="button" id="reset2">Azzera i filtri</button></p>
</div>
</div>
</div>

<section class="assure wrap" aria-label="Servizi">
<a href="servizi.html#personalizzazione"><b>Personalizzazione</b><span>Anche per un solo pezzo.</span></a>
<a href="garanzie.html"><b>Garanzie</b><span>Tre formule di protezione.</span></a>
<a href="servizi.html#care"><b>T91 Care</b><span>Riparazione, anche di altri marchi.</span></a>
<a href="index.html#centri"><b>70 centri</b><span>Provale dove giochi.</span></a>
</section>
""" + footer()


def home():
    centres = "\n".join(
        f'<li data-s="{n.lower()} {c.lower()}"><div><b>{n}</b><br><span>{c}</span></div><a href="#" aria-label="Indicazioni per {n}">Indicazioni</a></li>'
        for n, c in CENTRES
    )
    return head("T91 Padel | Racchette, servizi e centri", "Racchette e abbigliamento T91, più riparazione, personalizzazione, garanzie e 70 centri partner in Italia e in Europa.") + header("") + f"""
<section class="hero dark" aria-labelledby="h1">
<img class="bg" src="{CAMP}hero.jpg" alt="Giocatore in volo in uno smash di padel con la racchetta Holo, di sera sotto i riflettori">
<div class="in">
<h1 id="h1" class="d d-l">Holo.<br>Poi tutto il resto.</h1>
<p class="sub">La racchetta &egrave; l'inizio. Dopo ci sono la riparazione, la personalizzazione, le garanzie e 70 centri dove provarla.</p>
<div class="btns"><a class="btn solid" href="#shop">Acquista Holo {ARROW}</a><a class="btn line" href="#servizi">Scopri i servizi {ARROW}</a></div>
</div>
<span class="synth">Immagine generata con IA &middot; prototipo</span>
</section>

<section class="lb" aria-label="Campagna">
<a href="#shop" class="lb-i"><img src="{CAMP}v2-g1.jpg" alt="Giocatrice in top e leggings verde salvia T91 cammina tra i campi da padel, racchetta Holo in mano" loading="lazy"><span class="lb-c"><b>Donna. In movimento.</b><i class="pill">Donna</i></span></a>
<a href="#shop" class="lb-i"><img src="{CAMP}v2-g2.jpg" alt="Giocatrice con abito lilla T91 appoggiata a una panca, borsone arancione T91 e racchetta Holo accanto" loading="lazy"><span class="lb-c"><b>Donna. Dopo il campo.</b><i class="pill">Donna</i></span></a>
<a href="#shop" class="lb-i"><img src="{CAMP}v2-g3.jpg" alt="Giocatore con felpa e pantaloncini oliva T91 disteso su una panca nera lancia una pallina" loading="lazy"><span class="lb-c"><b>Uomo. Prima del punto.</b><i class="pill">Uomo</i></span></a>
<a href="#shop" class="lb-i"><img src="{CAMP}lookbook-g4.jpg" alt="Giocatore in t-shirt T91 in uno smash su sfondo di luce blu, racchetta Holo" loading="lazy"><span class="lb-c"><b>Uomo. Smash.</b><i class="pill">Racchette</i></span></a>
</section>

<div class="wrap">
<section class="svc" id="servizi" aria-labelledby="sv-h">
<div class="head">
<h2 id="sv-h" class="d d-l">Dopo l'acquisto siamo ancora qui.</h2>
<p class="lede mut">Sette servizi che di solito si scoprono troppo tardi. Qui stanno in prima fila.</p>
<div><a class="btn ink" href="servizi.html">Tutti i servizi {ARROW}</a></div>
</div>
<div class="rows">
{rows()}
</div>
</section>
</div>

<section class="feat" aria-labelledby="ft-h">
<div class="feat-img"><img src="{CAMP}dettaglio.jpg" alt="Mani che avvolgono l'impugnatura di una racchetta T91" loading="lazy"></div>
<div class="feat-txt"><h2 id="ft-h" class="d d-l">Una racchetta si cura.</h2><p class="lede">T91 Care ripara le racchette, anche di altri marchi. Non buttare quella che ami.</p><div class="btns"><a class="btn ink" href="servizi.html#care">T91 Care / Repair {ARROW}</a></div></div>
</section>

<section class="shop wrap" id="shop" aria-labelledby="sh-h">
<div class="shop-h"><h2 id="sh-h" class="d d-m">Racchette</h2><a class="btn line" href="racchette.html">Vedi tutte {ARROW}</a></div>
<div class="prods">
<a class="prod" href="#"><span class="new">Novit&agrave;</span><div class="ph"><img src="{IMG_HOLO}" alt="Racchetta HOLO" loading="lazy"></div><div class="meta"><span>Holo Collection</span><span>Da &euro;328,90</span></div></a>
<a class="prod" href="racchette.html"><div class="ph"><img src="assets/racchette/huracan-power-full-black-iriart.jpg" alt="Hurac&aacute;n Power Full Black x Emiliano Iriart 3.0" loading="lazy"></div><div class="meta"><span>Hurac&aacute;n Power Full Black x Iriart 3.0</span><span>Da &euro;328,90</span></div></a>
<a class="prod" href="prodotto-boss-one-k12.html"><div class="ph"><img src="assets/racchette/boss-one-k12-pro-master.jpg" alt="Boss One K12 Pro Master 6.0" loading="lazy"></div><div class="meta"><span>Boss One K12 Pro Master</span><span>Da &euro;328,90</span></div></a>
</div>
</section>

<section class="dark" id="centri" aria-labelledby="c-h">
<div class="wrap"><div class="centres">
<div style="display:grid;gap:22px;align-content:start">
<div class="big" aria-hidden="true">70</div>
<h2 id="c-h" class="d d-m">Centri partner in Italia e in Europa.</h2>
<p class="lede mut">Trovi, provi e compri T91 dove giochi. Presto anche Click &amp; Collect: ordini online, ritiri nel centro.</p>
</div>
<div class="find">
<label for="q">Cerca per citt&agrave; o centro</label>
<p class="cap mut" style="margin:-6px 0 0">14 centri su 70 in questo prototipo</p>
<input id="q" type="search" placeholder="Es. Bergamo" autocomplete="off">
<ul class="clist" id="clist" tabindex="0" aria-label="Elenco dei centri partner (14 di 70)">
{centres}
</ul>
<p class="empty" id="none" hidden>Nessun centro trovato. Scrivici: ne stiamo aggiungendo.</p>
</div>
</div></div>
</section>

<section class="split">
<div class="img"><img src="{IMG_DONNA}" alt="Abbigliamento donna T91 SS26" loading="lazy"></div>
<div class="txt">
<h2 class="d d-l">From Players to players.</h2>
<p class="lede">Ambassador, maestri e centri: la community che prova il prodotto prima di te e ti dice come va.</p>
<div class="btns"><a class="btn ink" href="#">Ambassador {ARROW}</a><a class="btn line" href="#">Programma maestri {ARROW}</a></div>
</div>
</section>

<section class="guides wrap" aria-labelledby="g-h">
<h2 id="g-h" class="d d-m">Guide</h2>
<div class="glist">
<a href="#"><h3>Quale racchetta fa per te</h3><span class="mut">Il quiz per scegliere la racchetta.</span></a>
<a href="#"><h3>Quando far riparare una racchetta</h3><span class="mut">Segnali da non ignorare.</span></a>
<a href="#"><h3>Quale garanzia scegliere</h3><span class="mut">Le formule di protezione.</span></a>
</div>
</section>
""" + footer()


SV_IMG = {"personalizzazione": ("uomo.jpg", "Uomo in t-shirt T91"), "care": ("dettaglio.jpg", "Impugnatura di una racchetta T91"), "experience": ("donna-campo.jpg", "Giocatrice che esce dal campo")}


def sv_block(i, sid, name, lead, steps, dark, tag="", note=""):
    cls = "sv dark" if dark else "sv"
    t = f'<span class="tag">{tag}</span>' if tag else ""
    cta = f'<a class="btn line" href="#contatti">Segnala interesse {ARROW}</a>' if tag else f'<a class="btn solid" href="#contatti">Contattaci {ARROW}</a>'
    li = "\n".join(f"<li><div><strong>{h}</strong>{p}</div></li>" for h, p in steps)
    n = f'<p class="note">{note}</p>' if note else ""
    im = f'<img class="svimg" src="{CAMP}{SV_IMG[sid][0]}" alt="{SV_IMG[sid][1]}" loading="lazy">' if sid in SV_IMG else ""
    return f"""<section class="{cls}" id="{sid}" aria-labelledby="{sid}-h">
<div class="a"><div style="display:grid;gap:20px"><h2 id="{sid}-h" class="d d-l">{name}{t}</h2><p class="lede">{lead}</p><div class="btns">{cta}</div></div></div>
<div class="b">{im}<ol class="steps">{li}</ol>{n}</div>
</section>"""


def servizi():
    S = [
        ("personalizzazione", "Personalizzazione", "Personalizza il prodotto T91 anche se ne vuoi uno solo. Nessun minimo d'ordine.",
         [("Scegli il prodotto", "Racchetta o abbigliamento."), ("Indica cosa vuoi", "Nome, colori, dettagli.")], False, "", "Bozza: tempi, costi e limiti da validare con T91."),
        ("care", "T91 Care / Repair", "Riparazione delle racchette, anche di altri marchi. Non buttare quella che ami.",
         [("Racchette T91 e di altri marchi", "La riparazione vale anche per i marchi concorrenti."), ("Modalit&agrave; da definire", "Dove si porta, tempi e costi.")], True, "", "Bozza: modalit&agrave;, tempi e costi da validare con T91."),
        ("usato", "Ritiro usato", "Valutiamo un servizio dedicato per le racchette che non usi pi&ugrave;.",
         [("Servizio in valutazione", "Condizioni e modalit&agrave; non ancora definite.")], False, "In valutazione", ""),
        ("experience", "T91 Experience", "Eventi, test ed esperienze speciali: il brand dal vivo, nei centri.",
         [("Provi", "Le racchette in campo, con chi le conosce."), ("Incontri", "Ambassador, maestri e altri giocatori.")], True, "", "Bozza: calendario eventi da fornire."),
        ("customer-care", "Customer care", "L'assistenza &egrave; parte del prodotto. Deve vedersi.",
         [("Assistenza in evidenza", "Canali e orari da definire con T91.")], False, "", "Bozza: canali e orari da confermare."),
        ("click-collect", "Click &amp; Collect", "Acquisti online e ritiri nel centro partner pi&ugrave; vicino.",
         [("Ordini online", "Scegli il centro al checkout."), ("Ritiri e provi", "Direttamente dove giochi.")], True, "In arrivo", "Dipende dalla scelta dello stack e dai centri aderenti."),
    ]
    blocks = "\n".join(sv_block(i + 1, *s) for i, s in enumerate(S))
    return head("Servizi | T91 Padel", "Personalizzazione, riparazione, ritiro usato, esperienze, assistenza, Click & Collect e garanzie T91.") + header("servizi") + f"""
<div class="wrap page-h">
<h1 class="d d-xl">Servizi.</h1>
<p class="lede">Una racchetta non finisce quando esce dal negozio. Ecco tutto quello che facciamo per te, prima e dopo.</p>
<div class="btns"><a class="btn ink" href="garanzie.html">Garanzie e protezione {ARROW}</a></div>
</div>
{blocks}
<section id="contatti" style="border-top:1px solid var(--ink)"><div class="wrap" style="padding-block:clamp(56px,8vw,100px);display:grid;gap:22px">
<h2 class="d d-l">Parliamone.</h2>
<p class="lede mut">Scrivici cosa ti serve. Rispondiamo con una proposta chiara.</p>
<div class="btns"><a class="btn ink" href="#">WhatsApp {ARROW}</a><a class="btn line" href="#">Scrivi una email {ARROW}</a></div>
<p class="note mut">Contatti reali da inserire (numero, email).</p>
</div></section>
""" + footer()


def garanzie():
    P = [
        ("109", "", "Protezione 2 anni", "Protezione di 2 anni sull'acquisto.", "Per chi vuole stare tranquillo a lungo."),
        ("39,90", "", "Sostituzione", "Sostituzione in caso di rottura.", "Se si rompe, la cambiamo."),
        ("59,90", "", "Rottura accidentale", "Rottura accidentale, caduta o scheggiatura.", "Per i colpi, le cadute, le scheggiature."),
    ]
    rows_ = "\n".join(
        f'<tr><th scope="row"><span class="pn">{n}</span></th><td><span class="pr">&euro;{p}</span></td><td>{c}<br><span class="mut">{d}</span></td><td><span class="todo">Condizioni da confermare</span></td></tr>'
        for p, _, n, c, d in P
    )
    return head("Garanzie e protezione | T91 Padel", "Le tre formule di protezione T91: 2 anni, sostituzione, rottura accidentale.") + header("garanzie") + f"""
<div class="wrap page-h">
<h1 class="d d-xl">Garanzie.</h1>
<p class="lede">Tre formule, ognuna con un prezzo e una cosa precisa che copre. Le condizioni complete vanno ancora confermate: finch&eacute; non lo sono, lo diciamo qui.</p>
</div>
<section class="wrap" aria-labelledby="pl-h" style="padding-bottom:clamp(40px,6vw,80px)">
<h2 id="pl-h" class="d d-m">Le tre formule</h2>
<table class="plans">
<thead><tr><th>Formula</th><th>Prezzo</th><th>Cosa copre</th><th>Stato</th></tr></thead>
<tbody>
{rows_}
</tbody>
</table>
<p class="note">Bozza: copertura, esclusioni, durata, procedura di richiesta e terminologia vanno verificate con T91 prima di pubblicare. I prezzi sono quelli indicati dal cliente.</p>
</section>
<section class="dark"><div class="wrap" style="padding-block:clamp(48px,7vw,96px)">
<h2 class="d d-l">Cosa succede se&hellip;</h2>
<div class="scn">
<div><b>Si rompe</b><span class="mut">Sostituzione, &euro;39,90.</span></div>
<div><b>Cade e si scheggia</b><span class="mut">Rottura accidentale, &euro;59,90.</span></div>
<div><b>Voglio stare tranquillo</b><span class="mut">Protezione 2 anni, &euro;109.</span></div>
</div>
<p class="note mut" style="border-color:#555">Le corrispondenze sono dedotte dalle descrizioni del cliente e le condizioni sono da confermare.</p>
</div></section>
<section class="wrap" style="padding-block:clamp(48px,7vw,96px)" aria-labelledby="f-h">
<h2 id="f-h" class="d d-m">Domande frequenti</h2>
<div class="faq">
<details><summary>Come attivo la protezione?</summary><p>Testo da definire con T91: quando si acquista, entro quanti giorni, come si registra.</p></details>
<details><summary>Come richiedo una sostituzione?</summary><p>Testo da definire con T91: documenti, tempi, centro di riferimento.</p></details>
<details><summary>Cosa non &egrave; coperto?</summary><p>Testo da definire con T91: esclusioni e usura normale.</p></details>
</div>
<div class="btns" style="margin-top:32px"><a class="btn ink" href="servizi.html">Tutti i servizi {ARROW}</a></div>
</section>
""" + footer()


(ROOT / "index.html").write_text(home(), encoding="utf-8")
(ROOT / "servizi.html").write_text(servizi(), encoding="utf-8")
(ROOT / "garanzie.html").write_text(garanzie(), encoding="utf-8")
(ROOT / "racchette.html").write_text(racchette(), encoding="utf-8")
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import pdp
(ROOT / "prodotto-boss-one-k12.html").write_text(pdp.render(head, header, footer, ARROW, VER), encoding="utf-8")
print("ok")
