# Esempi canonici

Questi sei SVG sono punti di partenza strutturali, non output finali. Mantengono palette, tipografia Barlow con IBM Plex Mono per i soli metadati, gerarchia leggera, footer safe zone e attributi del validatore. Prima della consegna sostituisci il footer tecnico invisibile con il lockup ufficiale indicato da `$vincos-brand-guidelines` e riesegui il controllo visivo.

Ogni esempio applica il contratto comune in [design-system.md](design-system.md): frame costante, un fuoco, ruoli distinti per card, nodi e connettori, una sola metafora strutturale dominante.

| Famiglia | Usala quando | Evita | Template |
|---|---|---|---|
| mappa di sistema | contano componenti, confini e relazioni | sequenze travestite da architettura | [system-map.svg](../assets/examples/system-map.svg) |
| flusso | conta l'ordine da un ingresso a un risultato | cicli rappresentati come processi lineari | [flow.svg](../assets/examples/flow.svg) |
| ciclo | l'ultimo passaggio alimenta davvero il primo | frecce circolari decorative senza feedback | [cycle.svg](../assets/examples/cycle.svg) |
| gerarchia | contano livelli, inclusioni o responsabilità | contenitori usati solo per decorazione | [hierarchy.svg](../assets/examples/hierarchy.svg) |
| confronto | contano differenze tra alternative o scenari | troppe dimensioni dentro la stessa matrice | [comparison.svg](../assets/examples/comparison.svg) |
| evoluzione | conta il cambiamento nel tempo | eventi senza ordine o distanza significativa | [evolution.svg](../assets/examples/evolution.svg) |

Adatta contenuti e proporzioni, ma conserva il contratto comune:

- `viewBox` esplicito;
- area del contenuto marcata con `data-vincos-content="true"`;
- fascia inferiore riservata con `data-vincos-footer="true"`;
- chamfer verificabili soltanto tramite `polygon` e `data-vincos-chamfer-cut`;
- massimo un elemento azzurro con funzione focale;
- titolo, concetti e spiegazioni in Barlow; metadati brevi in IBM Plex Mono entro il budget;
- connettori lineari segmentati sul bordo dei nodi, senza tratti nascosti sotto le card;
- `OpenFrame` e `TechnicalField` soltanto quando definiscono un campo operativo reale;
- `<title>` e `<desc>` per descrivere il diagramma vettoriale.
