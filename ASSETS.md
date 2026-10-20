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
