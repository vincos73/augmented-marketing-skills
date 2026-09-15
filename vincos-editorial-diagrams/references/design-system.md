# Sistema compositivo v1.7.0

Questo sistema rende riconoscibile la serie senza ripetere lo stesso diagramma. Conserva `Frame`, palette e tipografia; varia una sola metafora strutturale in base alla domanda del lettore.

## Token per canvas 800×500

| Token | Valore | Funzione |
|---|---:|---|
| `canvas-margin-x` | 56 | margine laterale minimo |
| `title-baseline` | 68 | baseline del titolo |
| `content-top / bottom` | 112 / 400 | area analitica |
| `footer-top` | 440 | fascia riservata al lockup |
| `stroke-structure` | 1 | confini e guide quiete |
| `stroke-primary` | 1.75 | relazioni da leggere per prime |
| `stroke-secondary` | 1 dashed | feedback, controllo, contesto |
| `title / entity / label / note` | 30 / 22 / 17 / 14 | scala Barlow |
| `mono-meta` | 11–13 | IBM Plex Mono per stati, numeri e misure |
| `mono-budget` | 15% | quota massima del testo visibile in mono |
| `connector-clearance` | 4–8 | distanza ottica dal bordo quando la linea non entra nel nodo |
| `technical-field-opacity` | 6–10% | griglia locale, mai estesa all'intero canvas |
| `hatch-step / stroke / opacity` | 10–14 / 1 / 8–12% | retino obliquo locale per distinguere un ruolo, mai per creare una gerarchia implicita |
| `highlight-budget` | 1 | unico elemento focale in azzurro |

## Primitive e ruoli

- `Frame`: fondo, TitleBlock, area contenuto e footer safe zone. È invariabile nella serie.
- `TitleBlock`: titolo breve, normalmente allineato alla griglia a sinistra. Centratura ammessa soltanto per composizioni davvero simmetriche. Una riga descrittiva è facoltativa e deve spiegare la regola di lettura, non replicare il titolo o il disegno.
- `Card`: passaggio, opzione o contenuto. Usa padding, label e tratto standard.
- `FocalCard`: unica card azzurra. Il chamfer segnala una decisione o un nucleo, mai soltanto enfasi estetica.
- `Node`: attore, sistema o controllo. La dimensione dipende dal ruolo, non dalla simmetria.
- `Connector`: `primary` per il meccanismo principale; `secondary` o `feedback` per le relazioni subordinate.
- `OpenFrame`: quattro segni angolari delimitano un campo senza creare una scatola. Usalo per un solo nucleo o area operativa, non per ogni card.
- `TechnicalField`: griglia o puntinatura locale a bassa intensità che rende visibile un'area di elaborazione, coordinamento o misura. Non porta significato da sola.
- `HatchField`: retino obliquo locale, normalmente navy su panna. Distingue la natura di un ruolo o di una superficie senza introdurre un nuovo colore; non equivale a `FocalCard` e non dichiara maggiore importanza.
- `OrchestratorSidecar`: punto di ingresso esterno a uno stack. Usa un box con un solo angolo tagliato, percorsi tratteggiati verso i livelli che può attivare e, facoltativamente, un `HatchField` interno molto leggero.
- `Boundary`: dominio o livello. Deve chiarire contenimento, non fare da cornice decorativa.
- `Trajectory`: baseline per l'ordine e curva per l'intensità o maturità; i due ruoli non si sovrappongono.

## Ritmo e gerarchia

1. Definisci un solo focal object, percepibile anche in miniatura.
2. Costruisci una massa dominante, una secondaria e un livello di servizio senza affidarti a contorni pesanti.
3. Alterna pieni, vuoti e connessioni: evita file di card di uguale peso quando il contenuto non è davvero sequenziale.
4. Riduci il peso dei confini e delle relazioni contestuali per far emergere il meccanismo; se una relazione è importante, rendila più leggibile con spazio, direzione o contrasto prima di aumentarne lo stroke.
5. Preferisci bordi singoli, aperti o parziali quando il contenitore completo non è necessario. Non usare contorni doppi per creare enfasi.
6. Termina i connettori sul perimetro dei nodi. Se una relazione continua oltre un nodo, disegnala come segmenti distinti: nessun tratto deve restare nascosto sotto la card o attraversarne l'interno.
7. Usa il chamfer con coerenza: due tagli superiori per una decisione/card di transizione; quattro tagli per un nucleo. Non mescolare le due varianti nello stesso diagramma senza ragione semantica.

## Stack operativo con orchestratore laterale

Usa questa opzione quando una suite viene presentata come sistema operativo professionale e un assistente orienta il bisogno verso più capacità. L'orchestratore è un punto di ingresso, non un livello dello stack.

- Colloca l'orchestratore fuori dallo stack, normalmente a sinistra, in un `OrchestratorSidecar` con un solo angolo tagliato. I livelli interni usano box con angoli arrotondati: la differenza di forma comunica la differenza di ruolo.
- Non numerare l'orchestratore come livello e non aggiungere spiegazioni ridondanti come “punto di ingresso, non un livello” quando la posizione, la micro-label e le connessioni lo rendono già evidente.
- Mantieni i livelli interni della stessa larghezza quando appartengono allo stesso sistema. Riduci l'intensità di numerazione e descrizioni di livello; usa la stessa etichetta mono `N skill` per tutti i conteggi aggregati.
- Se l'orchestratore può orientare verso più livelli, disegna un percorso tratteggiato distinto verso ciascuno. I percorsi devono terminare con `connector-clearance` e non devono suggerire una sequenza obbligata fra i livelli.
- Se un livello di fondazione alimenta quello operativo, usa una freccia primaria ascendente nel vuoto fra i due box. La freccia parte dal livello inferiore e punta a quello superiore, resta separata da entrambe le forme e sostituisce un percorso laterale più lungo.
- Mantieni le superfici interne neutre quando una campitura azzurra farebbe apparire un gruppo di skill più importante degli altri. La gerarchia deve derivare da ruolo, forma, posizione e direzione.
- Il retino obliquo è una variante facoltativa del solo orchestratore: navy, tratto sottile, passo regolare e opacità bassa secondo i token. Applicalo sotto testo e metadati, ritaglia il pattern sulla geometria chamfered e ridisegna il contorno per ultimo. Il retino distingue il ruolo esterno; non va esteso a una categoria di skill o usato come focus wash.
- Per una tavola editoriale autonoma, usa titolo e sottotitolo in alto e il lockup ufficiale nella footer safe zone. In una variante intermedia o incorporata in un layout che fornisce già questi elementi, la testata può essere omessa; non presentare il mockup spoglio come diagramma finale brandizzato.

## Tipografia funzionale

- Barlow porta il messaggio: titoli, concetti, spiegazioni, conclusioni e label principali.
- IBM Plex Mono porta il sistema: numerazione, stati, input/output, tempi, misure, file e annotazioni dei connettori.
- Il mono resta breve, normalmente Regular o Medium, senza paragrafi e senza imitare un terminale.
- Non usare il cambio di font come unico codice: associa stato e misura anche a posizione, forma o label esplicita.

## QA percettiva

- In thumbnail si individua prima il fuoco e poi la relazione primaria?
- Il lettore capisce il tipo di struttura prima di leggere le label?
- C'è almeno una zona di riposo attorno al focal object?
- Le linee sembrano un supporto alla lettura, non il soggetto principale?
- Ogni connettore si ferma sul bordo senza attraversare o passare sotto un nodo?
- Il mono comunica metadati reali e resta subordinato a Barlow?
- La griglia, se presente, è locale e funzionale?
- Ogni freccia o bordo ha un ruolo riconoscibile?
- L'azzurro segnala una sola cosa?
