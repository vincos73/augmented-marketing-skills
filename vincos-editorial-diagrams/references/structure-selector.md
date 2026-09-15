# Selettore strutturale e budget

Scegli la famiglia in base alla domanda del lettore:

| Il lettore deve capire... | Famiglia |
|---|---|
| parti interdipendenti e relazioni | mappa di sistema |
| la sequenza da A a B | flusso |
| un ritorno o feedback | ciclo |
| livelli, ruoli o inclusioni | gerarchia |
| differenze tra opzioni | confronto |
| cambiamenti nel tempo | evoluzione |

Prima del disegno registra `destinazione/dimensione`, `livello di dettaglio` (panoramica, operativo o analitico) e `pubblico`. Se mancano, segnala l'ipotesi.

Default prudenti per una tavola: 7 nodi o pannelli, 9 label, 10 connessioni e 2 livelli. Un ciclo può avere 6 tappe; una matrice resta 2×2. Se almeno due budget sono superati o la lettura è ridotta, prepara una `overview` e una tavola di `dettaglio`.

Prima di comporre, dichiara anche un `focal object`, una relazione primaria e, se presente, una relazione secondaria. Il fuoco occupa la maggiore salienza visiva; le relazioni non hanno tutte lo stesso peso. Per token, primitive e regole di ritmo, leggi [design-system.md](design-system.md).

## Invarianti SVG verificabili

Il validatore usa attributi semplici: `data-vincos-content="true"` marca il contenuto, `data-vincos-footer="true"` il footer, `data-vincos-chamfer-cut="24"` il taglio dichiarato in pixel. Per controllare i flussi lineari usa `data-vincos-node="true"` sui nodi e `data-vincos-connector="true"` su `line` o `polyline`: il connettore deve arrivare al bordo senza entrare nell'area interna del nodo.

Per un chamfer validabile, il valore è il minimo richiesto per entrambe le variazioni assolute `Δx` e `Δy` di almeno un lato del `polygon`, incluso il lato di chiusura ultimo-primo. `24` richiede quindi almeno un lato con `Δx ≥ 24` e `Δy ≥ 24`.

Il validatore controlla:

- `viewBox` numerico e positivo;
- footer interamente nella fascia inferiore del 12% e dentro il canvas;
- gap minimo di 24 px tra contenuto marcato e fascia footer;
- chamfer con cut di almeno 16 px, interno al canvas e fuori dal footer;
- presenza geometrica reale della diagonale dichiarata.
- assenza di attraversamenti interni tra connettori lineari marcati e nodi marcati.

I gruppi e gli elementi non supportati non possono essere marcati come contenuto o footer. Marca le primitive supportate: `rect`, `polygon`, `polyline`, `circle` e `line`. L'autovalidazione del chamfer accetta solo `polygon`; `path` resta ammesso dalla grammatica visiva, ma richiede una geometria equivalente `polygon` per il controllo oppure una revisione manuale del render. Il controllo dei connettori accetta soltanto `line` e `polyline`; curve e path richiedono revisione manuale a dimensione piena.

Per esempi delle sei famiglie e relativi anti-pattern, leggi [canonical-examples.md](canonical-examples.md).
