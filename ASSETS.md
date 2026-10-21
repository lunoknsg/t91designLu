# Provenance degli asset (prototipo)

Tutte le immagini sono caricate al volo dal sito attuale del cliente (t91padel.com, CDN Shopify), non sono nel progetto. Da sostituire con file forniti dal cliente prima della pubblicazione.

| Uso | File (https://t91padel.com/cdn/shop/files/) |
|---|---|
| Hero desktop | Racchetta_HOLO_arancione_in_carbonio_pc.webp |
| Hero mobile | Racchetta_HOLO_arancione_in_carbonio_cell.webp |
| Prodotto Iriart | IRIART_3_COVER_PC_a5cd421b-ba5d-4364-9af6-ef683e77ac0d.webp |
| Prodotto Boss One K12 | BOSS_ONE_K12_5.0_COVER_PC_640x.webp |
| Logo (header e footer, nero; bianco via filtro CSS) | Logo_T91_Nero.svg |
| Community / abbigliamento donna | Abbigliamento_Donna_Computer.webp |

Mancano: una fotografia per servizio (riparazione, personalizzazione, centro, esperienza), (il logo T91 ora è quello vero del sito, caricato dal CDN).
Testo da confermare col cliente: "Spedizione in tutto il mondo" (preso dalla barra del sito attuale).

## Foto di campagna generate (IA)

Generate con Higgsfield (modello gpt_image_2_5, 2k) il 20/10/2026, usando come riferimento la racchetta Holo, la foto donna e la t-shirt dal sito del cliente. Sono immagini sintetiche di prototipo: i capi e il volto non sono di un vero shooting. Da sostituire con fotografia reale prima della pubblicazione.

| File | Uso | Prompt (sintesi) |
|---|---|---|
| assets/campaign/hero.jpg | Hero home | Giocatore in volo in uno smash al vetro del campo, racchetta Holo, sera sotto i riflettori, spazio scuro a sinistra |
| assets/campaign/donna-campo.jpg | Collezione Donna, Experience | Giocatrice in completo terracotta T91 esce dal campo con la racchetta Holo, luce di fine pomeriggio |
| assets/campaign/uomo.jpg | Collezione Uomo, Personalizzazione | Uomo con t-shirt bianca T91 appoggiato al vetro del campo, racchetta Holo in mano |
| assets/campaign/donna.jpg | (non usata al momento) | Donna in top verde salvia T91, racchetta Holo sotto il braccio |
| assets/campaign/dettaglio.jpg | Care / Repair | Mani sull'impugnatura della racchetta Holo, sfondo campo sfocato |

| assets/campaign/uomo-azione.jpg | Collezione Uomo (home) | Giocatore in volee di diritto a rete, t-shirt bianca T91, luce calda di fine pomeriggio |
| assets/campaign/donna-azione.jpg | Collezione Donna (home) | Giocatrice in affondo per un rovescio basso, completo terracotta T91, stessa luce |

| assets/campaign/lookbook-g1.jpg | Griglia campagna (home), tile 1 | Donna in completo T91 lungo un muro, ombre dure, racchetta Holo; direzione artistica da riferimento editoriale street |
| assets/campaign/lookbook-g2.jpg | Griglia campagna, tile 2 | Donna appoggiata a una panca contro una serranda d'acciaio, borsa e racchetta Holo |
| assets/campaign/lookbook-g3.jpg | Griglia campagna, tile 3 | Uomo disteso su una panca d'acciaio, sfondo grigio-verde, lancia una pallina |
| assets/campaign/lookbook-g4.jpg | Griglia campagna, tile 4 | Uomo in smash su sfondo di luce blu astratta |
Le immagini uomo.jpg, donna.jpg, uomo-azione.jpg, donna-azione.jpg, donna-campo.jpg (tranne Experience) non sono più usate nella home.

## Correzioni foto griglia (20/10/2026)

Rigenerate con Higgsfield usando come riferimento i capi e gli ambienti veri forniti dal cliente (top e leggings verdi, borsone arancione, abito lilla, felpa e pantaloncini oliva, foto di campi indoor). Sostituiscono lookbook-g1/g2/g3.

| File | Uso | Contenuto |
|---|---|---|
| assets/campaign/v2-g1.jpg | Griglia tile 1 | Donna in top e leggings verde salvia T91 tra i campi indoor, luce dura |
| assets/campaign/v2-g2.jpg | Griglia tile 2 | Donna con abito lilla T91, borsone arancione T91, racchetta Holo, panca e serranda |
| assets/campaign/v2-g3.jpg | Griglia tile 3 | Uomo con felpa e pantaloncini oliva T91 su panca nera |
Capi e borsone sono riprodotti dall'IA a partire dai riferimenti: controllare fedeltà di logo e dettagli prima della pubblicazione.

## Foto prodotto della pagina Racchette (20/10/2026)

11 immagini in `assets/racchette/`, generate con Higgsfield (gpt_image_2_5, 2k, 4:5). Ogni racchetta è stata ricostruita a partire dalla foto frontale ufficiale del catalogo T91 (t91padel.com), con luce, composizione e grana presi da un riferimento fornito dal cliente (racchetta appoggiata a una parete monocromatica, ombra lunga) e la parete nel colore della racchetta. Del riferimento non è stato riprodotto né il prodotto né alcun marchio.
Sono immagini sintetiche di prototipo: grafica, logo e scritte stampate sulle racchette vanno verificati sul prodotto vero e le foto sostituite con scatti reali prima del lancio.
I nomi, i prezzi ("Da €328,90") e i link alle schede vengono dal catalogo attuale del sito T91. I filtri Linea, Carbonio, Gioco ed Edizione sono dedotti da nomi e tag di quel catalogo.


Aggiornamento: logo e immagini del cliente usate nel sito (logo T91, racchetta Holo, foto donna) sono ora copiate in `assets/ext/` e non più caricate da t91padel.com. Restano esterni solo i link alle schede prodotto del sito attuale.


### Aggiornamento foto Racchette: sfondo luminoso (20/10/2026)

Le 11 immagini in `assets/racchette/` sono state rigenerate con lo stesso procedimento ma con una direzione artistica più chiara, data da una foto di riferimento del cliente: parete colorata opaca e satura, luce diffusa high-key, ombra morbida a sinistra, racchetta appoggiata. Ogni racchetta ha un colore di parete diverso. Le versioni precedenti, con sfondi scuri e drammatici, non sono più nel progetto (restano nella cronologia di git).

### Aggiornamento sfondi tono su tono (20/10/2026)

Su richiesta, 8 delle 11 immagini in `assets/racchette/` sono state rigenerate con la parete nella stessa famiglia di colore della racchetta, in tinta più chiara (giallino per Finder Pro K12 Master 5.0, lilla chiaro per Finder Pro K12 3.0 PWR, lavanda per Boss One 18K, arancio chiaro per Boss One K12 e Huracán 3K, tre grigi diversi per le racchette nere). Restano quelle già tono su tono: Boss One K3 (azzurro), Finder Pro Master K3 (rosa) e Huracán 12K (arancio).

## Pagina prodotto Boss One K12 Pro Master 6.0 (20/10/2026)

15 immagini in `assets/prodotto/`, generate con Higgsfield (gpt_image_2_5, 2k, 4:5) partendo dalle foto ufficiali del catalogo T91, con la stessa direzione artistica delle foto delle racchette: parete opaca tono su tono, luce diffusa, ombra morbida a sinistra, grana fine.

| File | Uso |
|---|---|
| g2-tre-quarti, g3-profilo | Galleria: tre quarti e profilo del telaio |
| g4-piatto, g5-gola, g6-impugnatura | Galleria e sezione tecnologia: dettagli di piatto, gola e impugnatura |
| g7-azione | Galleria e blocco "La pala del n.1": giocatore in smash di sera (immagine sintetica) |
| g8-set | Galleria e blocco "Cosa c'è nel mio borsone": racchetta, borsone, cappellino, overgrip |
| a-borsone, a-cap, a-overgrip, a-copritesta | Set e "Spesso comprati insieme" |
| a-tshirt, a-short, a-calza, a-zaino | "Completa il tuo look" |

La prima immagine della galleria è `assets/racchette/boss-one-k12-pro-master.jpg`. Prodotti, grafiche e logo vanno verificati sul prodotto vero. Immagini sintetiche da sostituire con scatti reali prima del lancio.

### Contenuti da confermare (dal mockup)

I testi vengono da https://noknok-web.github.io/T91_F/T91_mockup_pagina_prodotto.html; la descrizione e i dati tecnici dal catalogo ufficiale. Da confermare con il cliente: valutazione 4,9 e 770 recensioni (le quattro recensioni mostrate sono d'esempio e riferite ad altri modelli), rate Klarna, prezzo T91 Club (-30%), ritiro a Osio Sotto (Click & Collect non ancora attivo), spedizione gratuita 24/48h e reso 30 giorni, il blocco "n.1 d'Italia" (nome dell'atleta e citazione da inserire), prezzi del set e dei prodotti abbinati, valori di potenza/controllo, video di 1:45 (non ancora prodotto), articoli del blog.

### Fascia Mystery Box (21/10/2026)

`assets/campaign/mystery-box.jpg`: generata con Higgsfield (gpt_image_2_5, 2k, 16:9) partendo dall'immagine della Mystery Box presa dalla home di t91padel.com (scatola nera con linea dorata luminosa). Ambientata su una panchina in legno a bordo di un campo da padel blu, al tramonto, con i riflettori. Immagine sintetica da sostituire con uno scatto reale. Il "60%" nel testo è quello indicato dal cliente; il sito attuale parla di sconti "fino al -60%" su listino, da verificare con T91 prima della pubblicazione.

## Blog (21/10/2026)

Pagine: `blog.html` e tre articoli (`articolo-*.html`), generati da `tools/blog.py`. Sono sintesi scritte con parole nostre di tre pubblicazioni esterne, **a solo scopo illustrativo per la presentazione al cliente**. Le tre foto in `assets/blog/` sono scaricate dalle stesse pubblicazioni: i diritti restano degli autori e vanno sostituite con foto proprie o con immagini licenziate prima di qualsiasi uso pubblico.

| Articolo | Fonte | Foto |
|---|---|---|
| Il warm-up nel padel | https://www.padelisland.it/warm-up-nel-padel/ (Padel Island) | `warm-up.jpg`, dalla pagina dell'articolo |
| Un Master da applausi: si chiude il GdB Padel Tour | https://www.giornaledibrescia.it/sport/altri-sport/match-spettacolari-festa-master-gdb-padel-tour-da-applausi-foto-bakrte7f (Giornale di Brescia) | `gdb-padel-tour.jpg`, foto Newreporter Papetti |
| Premier Padel a Roma: nove giorni al Foro Italico | https://www.mrpadelpaddle.com/padel-italia/bnl-italy-major-premier-padel-9-giorni-intensi-di-padel/ (MrPadel Paddle) | `foro-italico.jpg`, foto A. Fioriti |

Nota: l'articolo sul Foro Italico descrive il programma di un'edizione passata del torneo (date di luglio 2023); nell'articolo T91 le date non sono riportate.

### Mappa dei centri (21/10/2026)

La fascia "Trova T91 vicino a te" in home usa Leaflet 1.9.4 (`assets/vendor/`, licenza BSD) al posto di Google Maps, che richiede una chiave API: mare blu scuro, confini dei paesi in bianco, nessuna tessera esterna. I confini vengono da Natural Earth tramite `world-atlas` (dominio pubblico, `assets/mondo.geo.json`). I 70 centri (nome, indirizzo, telefono, coordinate) sono copiati dalla pagina pubblica di t91padel.com in `assets/centri.json`; i nomi dei referenti non sono riportati. Da aggiornare quando T91 cambia l'elenco.

### Foto fascia "From Players to players" (21/10/2026)

`assets/campaign/iriart-salandro.jpg`: fotografia fornita dal cliente (file `20260531_Emiliano_Martin_Iriart_Mauro_Agustin_Salandro_ZAF_2401.JPG`, evento BNL Italy Major Premier Padel 2026) con Emiliano Iriart e Bubu Salandro. Sostituisce la foto precedente. Diritti e liberatorie vanno confermati con T91 e con il fotografo prima di un uso pubblico.

Dettaglio della mappa (21/10/2026): confini delle regioni e delle province italiane da openpolis/geojson-italy (dati ISTAT, semplificati in `assets/it-regioni.geo.json` e `assets/it-province.geo.json`). Nomi di paesi, mari e città (circa 80) scritti a mano in `js/centri.js`, mostrati in base al livello di zoom: paesi e grandi città da lontano, regioni da zoom 6, province da zoom 7.
