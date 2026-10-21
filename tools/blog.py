"""Blog: pagina elenco e articoli.

Gli articoli sono sintesi scritte con parole nostre di tre pubblicazioni esterne, a solo scopo
illustrativo per la presentazione al cliente. Foto e fonti sono dei rispettivi autori.
"""

POSTS = [
    {
        "slug": "warm-up-nel-padel",
        "file": "articolo-warm-up-nel-padel.html",
        "cat": "Guide",
        "min": 5,
        "title": "Il warm-up nel padel: come prepararsi prima di scendere in campo",
        "short": "Il warm-up nel padel",
        "dek": "Dieci o quindici minuti di riscaldamento bastano a rendere il corpo più pronto e a ridurre il rischio di infortuni. Ecco come organizzarli.",
        "img": "assets/blog/warm-up.jpg",
        "alt": "Giocatore in ginocchio sul campo da padel mentre si allunga prima della partita",
        "src_name": "Padel Island",
        "src_url": "https://www.padelisland.it/warm-up-nel-padel/",
        "photo": "Padel Island",
        "body": [
            ("p", "Il padel chiede scatti brevi, frenate improvvise, rotazioni del busto e colpi esplosivi. Muscoli e articolazioni lavorano da subito al massimo, e le più esposte sono ginocchia e spalle. Entrare in campo a freddo vuol dire rischiare stiramenti e contratture, ma anche partire con reazioni più lente."),
            ("h", "Quanto deve durare"),
            ("p", "La finestra giusta è tra i 10 e i 15 minuti. Meno non basta per alzare la temperatura del corpo e attivare i muscoli, di più rischia di consumare energie che servono nel match. Chi ha appena iniziato può dedicare qualche minuto in più alla mobilità, mentre un giocatore esperto può concentrarsi sulla velocità."),
            ("h", "Tre fasi, in quest'ordine"),
            ("ol", [
                ("Mobilità articolare", "Circonduzioni delle spalle, rotazioni del busto, piegamenti delle ginocchia. Servono a sciogliere la rigidità prima dei cambi di direzione."),
                ("Attivazione muscolare", "Affondi in avanti e squat dinamici per le gambe, un plank breve per il core. Venti o trenta secondi per esercizio, a ritmo costante."),
                ("Cardio leggero", "Corsa sul posto, skip basso e salti laterali, a intensità moderata. Il cuore deve salire di giri senza stancarti."),
            ]),
            ("h", "Adattalo al tuo livello"),
            ("p", "Chi inizia può fermarsi a mobilità e un po' di corsa leggera. Un intermedio aggiunge affondi, squat e salti laterali e lavora di più sul core, che dà equilibrio e precisione ai colpi. Un avanzato inserisce cambi di direzione rapidi e spostamenti laterali per accendere i riflessi."),
            ("quote", "Qualunque sia il livello, la regola è ascoltare il corpo e non saltare mai il riscaldamento."),
        ],
        "cta": ("Prima di giocare, anche l'attrezzatura conta", "Una racchetta adatta al tuo livello aiuta a muoverti meglio fin dai primi scambi.", "Scopri le racchette", "racchette.html"),
    },
    {
        "slug": "gdb-padel-tour-master",
        "file": "articolo-gdb-padel-tour-master.html",
        "cat": "Tornei",
        "min": 4,
        "title": "Un Master da applausi: si chiude il GdB Padel Tour",
        "short": "Il Master del GdB Padel Tour",
        "dek": "A Castenedolo nove categorie hanno chiuso tre mesi di gare con match combattuti e tanta voglia di stare insieme.",
        "img": "assets/blog/gdb-padel-tour.jpg",
        "alt": "Una giocatrice festeggia sollevando il trofeo alla finale del Master",
        "src_name": "Giornale di Brescia",
        "src_url": "https://www.giornaledibrescia.it/sport/altri-sport/match-spettacolari-festa-master-gdb-padel-tour-da-applausi-foto-bakrte7f",
        "photo": "Giornale di Brescia, foto Newreporter Papetti",
        "body": [
            ("p", "Doveva essere una grande festa, ed è stata una grande festa. Dopo oltre tre mesi di tappe, il GdB Padel Tour, organizzato insieme ad Awt, ha chiuso la stagione nella nuova struttura del Ten Padel di Castenedolo, inaugurata proprio per il Master finale."),
            ("h", "I numeri della giornata"),
            ("ul", [
                "104 giocatori sui cinque campi del centro",
                "9 categorie in gara, dal mattino fino a sera",
                "8mila euro di montepremi in prodotti tecnici",
                "Un pubblico numeroso, arrivato fin dalle prime partite",
            ]),
            ("h", "Storie dal torneo"),
            ("p", "Nella quinta categoria maschile hanno vinto ancora Lancini e Cominelli, già primi in tre tappe su quattro: dopo un esordio sofferto, chiuso solo al tie break, hanno preso il controllo e vinto la finale con un doppio 6-2. Al femminile, Menni e Nolli si sono messe in coppia solo per il Master e hanno trovato subito l'intesa."),
            ("p", "Eugenia Alessia Todaro, ex tennista, ha fatto la doppietta: titolo nel misto di quarta e finale vinta in terza categoria femminile insieme a Lazzaroni. Tra i momenti più spettacolari, la finale di terza maschile, decisa da un tie break infinito chiuso 21-19."),
            ("p", "L'ultimo trofeo, quello della seconda categoria maschile, il livello più alto del Master, è andato a Barbi e Tonelli, con una finale senza sbavature."),
            ("quote", "Partite combattute che hanno regalato i trofei, ma anche la voglia di stare insieme e di divertirsi."),
        ],
        "cta": ("Gioca come i protagonisti del Master", "Dal controllo alla potenza, trova la racchetta adatta al tuo gioco.", "Trova la tua racchetta", "racchette.html"),
    },
    {
        "slug": "bnl-italy-major-premier-padel",
        "file": "articolo-bnl-italy-major-premier-padel.html",
        "cat": "Tornei",
        "min": 3,
        "title": "Premier Padel a Roma: nove giorni di padel al Foro Italico",
        "short": "Premier Padel al Foro Italico",
        "dek": "134 incontri, due tabelloni che avanzano insieme e le stelle del circuito: il programma del BNL Italy Major.",
        "img": "assets/blog/foro-italico.jpg",
        "alt": "Il campo centrale del Foro Italico pieno di pubblico durante il torneo di padel",
        "src_name": "MrPadel Paddle",
        "src_url": "https://www.mrpadelpaddle.com/padel-italia/bnl-italy-major-premier-padel-9-giorni-intensi-di-padel/",
        "photo": "MrPadel Paddle, foto A. Fioriti",
        "body": [
            ("p", "Al Foro Italico il Major diventa un appuntamento di nove giorni, con una qualità di gioco e di intrattenimento che cresce di anno in anno. In programma 134 incontri complessivi, 79 maschili e 55 femminili, con due tabelloni che procedono di pari passo fino al gran finale di domenica sera."),
            ("h", "Come funziona il torneo"),
            ("ul", [
                "Si parte il sabato con le qualificazioni maschili: 32 coppie si giocano gli otto posti ancora liberi nel tabellone principale da 56",
                "Il femminile comincia il lunedì con il turno unico di qualificazione: 16 coppie per 8 posti",
                "Dal martedì il tabellone femminile conta 48 coppie, e tutte le sedici teste di serie saltano il primo turno",
                "Nel maschile le prime otto teste di serie entrano dal secondo turno",
            ]),
            ("h", "Il calendario in breve"),
            ("p", "La giornata più intensa è il mercoledì: debuttano a Roma tutti i nomi più attesi e si giocano 32 partite, 16 maschili e 16 femminili, su più campi. Giovedì gli ottavi, venerdì i quarti, sabato le semifinali in due sessioni, pomeridiana e serale. Domenica sera le finali decidono le due coppie vincitrici."),
            ("h", "Dal vivo o in TV"),
            ("p", "I biglietti si acquistano online. Per i tesserati FITP è prevista una scontistica sui tagliandi e sugli abbonamenti, mentre orari e programmazione TV sono pubblicati dagli organizzatori."),
            ("quote", "Nove giorni di padel, con due tabelloni che avanzano insieme fino alla domenica."),
        ],
        "cta": ("Il padel dei campioni, a casa tua", "Scopri le racchette T91 progettate insieme ai nostri atleti.", "Vai alle racchette", "racchette.html#signature"),
    },
]
BY_SLUG = {p["slug"]: p for p in POSTS}
CATS = ["Guide", "Tornei"]


def card(p, big=False, tag="h3"):
    cls = "bp big" if big else "bp"
    return (f'<li class="{cls}" data-cat="{p["cat"]}"><a href="{p["file"]}"><div class="bp-i"><img src="{p["img"]}" alt="{p["alt"]}" loading="lazy"></div>'
            f'<div class="bp-t"><span class="cap mut">{p["cat"]} &middot; {p["min"]} min</span><{tag}>{p["title"]}</{tag}><p>{p["dek"]}</p></div></a></li>')


def render_list(head, header, footer, arrow, ver):
    chips = '<button type="button" class="bc" aria-pressed="true" data-c="">Tutti</button>' + "".join(
        f'<button type="button" class="bc" aria-pressed="false" data-c="{c}">{c}</button>' for c in CATS)
    cards = "".join(card(p, i == 0, "h2") for i, p in enumerate(POSTS))
    return head("Blog | T91 Padel", "Guide, tornei e novit&agrave; dal mondo del padel.") + header("blog") + f"""
<div class="wrap">
<nav class="crumb" aria-label="Percorso"><a href="index.html">Home</a><span aria-hidden="true">/</span><span aria-current="page">Blog</span></nav>
<div class="plp-h"><div class="plp-t"><h1 class="d d-l">Dal blog.</h1><p class="lede">Guide per giocare meglio, tornei e storie dal mondo del padel.</p></div><p class="plp-c" id="bcount">{len(POSTS)} articoli</p></div>
<div class="plp-bar bbar" role="group" aria-label="Categorie">{chips}</div>
<ul class="bgrid" id="bgrid">{cards}</ul>
<p class="note">Articoli a solo scopo illustrativo: sintesi di testi pubblicati da altre testate, con foto e fonti dei rispettivi autori. Da sostituire con i contenuti T91.</p>
</div>
<section class="dark quiz" aria-labelledby="bq-h"><div class="wrap quizin">
<div><h2 id="bq-h" class="d d-l">Trova la tua racchetta.</h2><p class="lede mut">Fai il test in 60 secondi e ricevi il risultato su WhatsApp.</p></div>
<a class="btn solid" href="racchette.html">Vai alle racchette {arrow}</a></div></section>
""" + footer().replace("</body>", '<script src="js/blog.js?v=' + ver + '"></script>\n</body>')


def render_article(p, head, header, footer, arrow, ver):
    body = ""
    for kind, val in p["body"]:
        if kind == "p":
            body += f"<p>{val}</p>"
        elif kind == "h":
            body += f"<h2>{val}</h2>"
        elif kind == "ul":
            body += "<ul>" + "".join(f"<li>{x}</li>" for x in val) + "</ul>"
        elif kind == "ol":
            body += '<ol class="ar-steps">' + "".join(f"<li><b>{t}</b><span>{d}</span></li>" for t, d in val) + "</ol>"
        elif kind == "quote":
            body += f"<blockquote>{val}</blockquote>"
    others = [x for x in POSTS if x["slug"] != p["slug"]]
    rel = "".join(card(x, False, "h3") for x in others)
    c = p["cta"]
    return head(f'{p["short"]} | Blog T91 Padel', p["dek"]) + header("blog") + f"""
<div class="wrap">
<nav class="crumb" aria-label="Percorso"><a href="index.html">Home</a><span aria-hidden="true">/</span><a href="blog.html">Blog</a><span aria-hidden="true">/</span><span aria-current="page">{p["short"]}</span></nav>
<article class="art">
<header class="art-h"><span class="cap mut">{p["cat"]} &middot; {p["min"]} min di lettura</span><h1 class="d d-l">{p["title"]}</h1><p class="lede">{p["dek"]}</p></header>
<figure class="art-f"><img src="{p["img"]}" alt="{p["alt"]}"><figcaption>Foto: {p["photo"]}</figcaption></figure>
<div class="art-b">{body}
<p class="art-src">Sintesi a solo scopo illustrativo. Fonte originale: <a href="{p["src_url"]}" target="_blank" rel="noopener">{p["src_name"]}</a>.</p>
</div>
</article>
</div>
<section class="dark help" aria-labelledby="ac-h"><div class="wrap helpin">
<div><h2 id="ac-h" class="d d-l">{c[0]}</h2><p class="lede mut">{c[1]}</p></div>
<div class="btns"><a class="btn solid" href="{c[3]}">{c[2]} {arrow}</a></div></div></section>
<section class="wrap guides" aria-labelledby="ar-h"><div class="shop-h"><h2 id="ar-h" class="d d-m">Altri articoli</h2><a class="btn line" href="blog.html">Tutto il blog {arrow}</a></div>
<ul class="bgrid two">{rel}</ul></section>
""" + footer()
