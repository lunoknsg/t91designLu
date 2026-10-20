"""Pagina Racchette (catalogo). Struttura dal mockup
https://noknok-web.github.io/T91_F/T91_mockup_racchette.html nello stile del sito.
Livello, stile di gioco e collezione sono dati di esempio del mockup, da confermare con T91.
"""

PRICE = 328.9

# slug, nome, handle, linea, livello, stile, collezione, badge, carbonio, peso
RACKETS = [
    ("boss-one-k12-pro-master", "Boss One K12 Pro Master 6.0", "boss-one-k12-pro-master-6-0", "Boss One", "Avanzati", "Potenza", "Holo", "Novit&agrave;", "12K", "356-365 g"),
    ("boss-one-k3-pro-master", "Boss One K3 Pro Master", "boss-one-k3-pro-master", "Boss One", "Intermedi", "Potenza", "Holo", "Novit&agrave;", "3K", "356-365 g"),
    ("finder-pro-master-k3", "Finder Pro Master K3", "finder-pro-master-k3", "Finder Pro", "Intermedi", "Controllo", "Holo", "Novit&agrave;", "3K", "348-355 g"),
    ("huracan-power-full-black-iriart", "Hurac&aacute;n Full Black x Iriart 3.0", "huracan-power-full-black-x-emiliano-iriart-3-0", "Hurac&aacute;n", "Pro", "Polivalenti", "Signature Pro", "Signature", "Carbonio", "&mdash;"),
    ("huracan-12k-bubu", "Hurac&aacute;n 2.0 12K x Bubu Salandro", "huracan-2-0-12k-x-bubu-salandro", "Hurac&aacute;n", "Pro", "Potenza", "Signature Pro", "Signature", "12K", "346-360 g"),
    ("huracan-3k-bubu", "Hurac&aacute;n 2.0 3K x Bubu Salandro", "huracan-2-0-x-bubu-salandro", "Hurac&aacute;n", "Avanzati", "Polivalenti", "Signature Pro", "Signature", "3K", "346-360 g"),
    ("huracan-2-0", "Hurac&aacute;n 2.0", "huracan-2-0", "Hurac&aacute;n", "Principianti", "Controllo", "", "Bestseller", "Carbonio", "&mdash;"),
    ("boss-one-18k-pwr", "Boss One 18K 3.0 PWR", "boss-one-18k-3-0-pwr", "Boss One", "Avanzati", "Potenza", "", "", "18K", "&mdash;"),
    ("finder-pro-k12-pwr", "Finder Pro K12 3.0 PWR", "finder-pro-k12-3-0-pwr", "Finder Pro", "Intermedi", "Polivalenti", "Signature Pro", "", "12K", "&mdash;"),
    ("finder-pro-k12-master", "Finder Pro K12 Master 5.0", "finder-pro-k12-master-5-0", "Finder Pro", "Avanzati", "Polivalenti", "", "", "12K", "&mdash;"),
    ("boss-one-12k-pwr", "Boss One 12K 3.0 PWR", "boss-one-12k-3-0-x-nick-remedi", "Boss One", "Avanzati", "Potenza", "Signature Pro", "", "12K", "&mdash;"),
]

GROUPS = [
    ("lv", "Livello", ["Principianti", "Intermedi", "Avanzati", "Pro"], 4),
    ("st", "Stile di gioco", ["Potenza", "Controllo", "Polivalenti"], 5),
    ("co", "Collezione", ["Holo", "Signature Pro"], 6),
    ("li", "Linea", ["Boss One", "Finder Pro", "Hurac&aacute;n"], 3),
    ("k", "Carbonio", ["3K", "12K", "18K"], 8),
]
SLUGS = {"Principianti": "principianti", "Intermedi": "intermedi", "Avanzati": "avanzati", "Pro": "pro",
         "Potenza": "potenza", "Controllo": "controllo", "Polivalenti": "polivalenti",
         "Holo": "holo", "Signature Pro": "signature"}

FAQ = [
    ("Che differenza c'&egrave; tra carbonio 3K, 12K e 18K?", "Pi&ugrave; &egrave; alto il numero, pi&ugrave; il telaio &egrave; rigido: la palla esce pi&ugrave; veloce ma serve pi&ugrave; tecnica. Il 3K &egrave; pi&ugrave; morbido e confortevole."),
    ("Che peso devo scegliere?", "Tra 345 e 360 g va bene per la maggior parte dei giocatori. Su molte racchette puoi scegliere il grammo esatto a +&euro;10."),
    ("Posso provarla prima di comprarla?", "S&igrave;, nei centri partner T91 e a Osio Sotto. E hai comunque 30 giorni per il reso gratuito."),
    ("Posso pagare a rate?", "S&igrave;, con Klarna in 3 rate senza interessi."),
]


def eur(v):
    return "&euro;" + ("%.2f" % v).replace(".", ",")


def attr(s):
    return s.replace("&aacute;", "a").replace("&mdash;", "-").replace("&agrave;", "a")


def render(head, header, footer, arrow, ver):
    A = arrow
    # filtri
    fg = ""
    for key, title, vals, _n in GROUPS:
        items = ""
        for v in vals:
            idx = {"lv": 4, "st": 5, "co": 6, "li": 3, "k": 8}[key]
            n = sum(1 for r in RACKETS if r[idx] == v)
            vid = f"f-{key}-" + attr(v).lower().replace(" ", "-")
            slug = SLUGS.get(v, "")
            items += (f'<label class="chk" for="{vid}"><input type="checkbox" id="{vid}" data-k="{key}" data-slug="{slug}" value="{v}">'
                      f'<span class="box" aria-hidden="true"></span><span class="lab">{v}</span><span class="n">{n}</span></label>')
        fg += f'<fieldset class="fg"><legend>{title}</legend>{items}</fieldset>'
    # schede
    cards = ""
    for i, (slug, name, handle, li, lv, st, co, badge, k, w) in enumerate(RACKETS):
        internal = slug == "boss-one-k12-pro-master"
        url = "prodotto-boss-one-k12.html" if internal else f"https://t91padel.com/products/{handle}"
        tb = "" if internal else ' target="_blank" rel="noopener"'
        bcls = "new k" if badge == "Signature" else ("new w" if badge == "Bestseller" else "new")
        bd = f'<span class="{bcls}">{badge}</span>' if badge else ""
        cards += (f'<li class="pc" data-name="{attr(name).lower()}" data-lv="{lv}" data-st="{st}" data-co="{co}" data-li="{li}" data-k="{k}" data-w="{w}" '
                  f'data-new="{1 if badge == "Novit&agrave;" else 0}" data-price="{PRICE}" data-i="{i}" data-img="assets/racchette/{slug}.jpg" data-slug="{slug}">'
                  f'<div class="pc-ph">{bd}<a class="pc-img" href="{url}"{tb} tabindex="-1" aria-hidden="true"><img src="assets/racchette/{slug}.jpg" alt="" loading="{"eager" if i < 4 else "lazy"}"></a>'
                  f'<button class="cmp" type="button" aria-pressed="false" aria-label="Confronta {attr(name)}"><i aria-hidden="true"></i>Confronta</button></div>'
                  f'<a class="pc-m" href="{url}"{tb}><p class="pc-tg"><span>{lv}</span><span>{st}</span></p><h2>{name}</h2>'
                  f'<p class="pc-p">{eur(PRICE)}<small>o 3 rate da &euro;109,63 con Klarna</small></p></a></li>')
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)

    return head("Racchette | T91 Padel", "Tutte le racchette da padel T91, dal primo match al torneo. Filtra per livello e stile di gioco, confronta fino a 4 racchette o fatti consigliare dal test.") + header("racchette") + f"""
<div class="wrap">
<nav class="crumb" aria-label="Percorso"><a href="index.html">Home</a><span aria-hidden="true">/</span><span aria-current="page" id="crumb">Racchette</span></nav>
<div class="plp-h">
<div class="plp-t"><h1 class="d d-l" id="rt">Racchette da padel.</h1><p class="lede" id="rd">Tutte le racchette T91, dal primo match al torneo. Filtra per livello e stile di gioco, o fatti consigliare dal test.</p></div>
<p class="plp-c" id="count" aria-live="polite">{len(RACKETS)} racchette</p>
</div>
<div class="plp-bar">
<button class="fbtn" type="button" id="fbtn" aria-expanded="false" aria-controls="filters">Filtri</button>
<button class="cbtn" type="button" id="cbtn">Confronta <span class="cn" id="cn">0</span></button>
<div class="chips" id="chips" aria-label="Filtri attivi"></div>
<label class="sort" for="sort"><span>Ordina</span>
<select id="sort"><option value="i">In evidenza</option><option value="new">Novit&agrave;</option><option value="pa">Prezzo crescente</option><option value="pd">Prezzo decrescente</option></select></label>
</div>
<div class="plp">
<form class="filters" id="filters" aria-label="Filtri">{fg}<button class="reset" type="button" id="reset">Rimuovi filtri</button></form>
<ul class="pgrid" id="pgrid">
{cards}
</ul>
<p class="plp-e" id="empty" hidden>Nessuna racchetta con questi filtri. <button class="reset inl" type="button" id="reset2">Rimuovi filtri</button></p>
<p class="note">Livello e stile di gioco di ogni racchetta sono di esempio: quelli veri li indicher&agrave; T91.</p>
</div>

<section class="ban" aria-label="Guide e confronto">
<a class="ban-g" href="#"><img src="assets/prodotto/g6-impugnatura.jpg" alt="" loading="lazy"><span><small>Guida &middot; 6 minuti</small><b>Come scegliere la racchetta per il tuo livello</b><u>Leggi la guida {A}</u></span></a>
<div class="ban-c"><small>Ancora indeciso?</small><b>Confronta fino a 4 racchette, fianco a fianco.</b><button type="button" class="btn ink" id="ocmp">Apri il confronto {A}</button></div>
</section>

<section class="seo" aria-labelledby="seo-h">
<h2 id="seo-h" class="d d-m">Come scegliere una racchetta da padel</h2>
<div class="acc">
<details open><summary>Livello, peso e carbonio</summary><p>Per chi inizia conta la maneggevolezza: peso contenuto, bilanciamento basso e una gomma morbida che perdona. Con l'esperienza si cerca pi&ugrave; potenza, con carbonio pi&ugrave; rigido e bilanciamento alto. Le racchette T91 sono progettate in Italia e provate dal nostro Team prima di arrivare a te.</p></details>
{faq}
</div>
</section>
</div>

<section class="dark quiz" aria-labelledby="qz-h">
<div class="wrap quizin">
<div><h2 id="qz-h" class="d d-l">Trova la tua racchetta.</h2><p class="lede mut">Fai il test in 60 secondi e ricevi il risultato su WhatsApp.</p></div>
<form class="qf" id="qf"><label for="wa" class="cap">Il tuo numero WhatsApp</label><div class="qr"><input id="wa" type="tel" inputmode="tel" autocomplete="tel" placeholder="+39 ..."><button class="btn solid" type="submit">Inizia {A}</button></div></form>
</div>
</section>

<div class="ctray" id="ctray" role="region" aria-label="Confronto" hidden>
<div class="ctray-th" id="cth"></div>
<span class="ctray-tx" id="ctx"></span>
<button type="button" class="btn solid" id="cgo">Confronta</button>
<button type="button" class="cx" id="cclear" aria-label="Svuota il confronto">&times;</button>
</div>

<dialog class="cdlg" id="cdlg" aria-labelledby="cd-h">
<div class="cdlg-h"><h2 id="cd-h" class="d d-m">Confronta le racchette</h2><button type="button" class="cx" id="cdc" aria-label="Chiudi">&times;</button></div>
<div class="cdlg-b" id="cdb"></div>
</dialog>
<div class="toast" id="toast" role="status" aria-live="polite" hidden></div>
""" + footer().replace("</body>", '<script src="js/plp.js?v=' + ver + '"></script>\n</body>')
