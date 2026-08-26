# Forward test indipendente di `define-marketing-challenge` v0.1.0

**Data:** 2026-08-26
**Valutatore:** agente separato con contesto vuoto
**Esito:** nessun hard fail; due soft fail osservati; correzioni confluite in `v0.1.1`

## Controlli di indipendenza

Il valutatore ha ricevuto soltanto la candidata `v0.1.0`, i suoi reference e i materiali grezzi dei tre casi. Non ha ricevuto la conversazione di authoring, il catalogo degli eval, `expected-run.md`, i self-check, README o il documento di architettura. Ha scritto esclusivamente in una directory temporanea e non ha modificato il repository né `.agents/`.

## Casi eseguiti

1. Relaybird, primo turno e bozza completa dopo le risposte della Marketing Director.
2. Forward test sulla sponsorship da 18.000 euro non approvata.
3. Brief cliente ricevuto da un'agenzia senza referente autorizzato presente.

Nel caso principale la prima risposta misurava 421 parole secondo il checker esistente, conteneva quattro sezioni Markdown e tre domande. Il checker ha contato correttamente parole e domande, ma ha restituito zero gruppi perché riconosce etichette in grassetto e non titoli Markdown; la struttura a quattro gruppi è stata quindi verificata manualmente.

## Esito per criterio

| ID | Esito | Evidenza o limite |
|---|---|---|
| DMC01 | Pass | Entità e versioni sono dichiarate; la bozza completa cita i percorsi letti. |
| DMC02 | Parziale | L'attivazione sui casi ambigui e il confine agenzia sono corretti; non era presente un caso già sufficientemente definito. |
| DMC03 | Pass | Entrambe le prime risposte Relaybird producono subito una sfida provvisoria e tre domande. |
| DMC04 | Pass manuale | 421 parole, quattro gruppi, tre domande nel caso principale. |
| DMC05 | Pass | Il calo resta un segnale e awareness, compliance e rollout restano spiegazioni non dimostrate. |
| DMC06 | Pass | Webinar, sponsorship e TikTok restano tattiche proposte. |
| DMC07 | Soft fail | La frase “interesse già osservato per contenuti operativi” può attribuire al pubblico target un segnale aggregato non collegato, anche se il limite viene chiarito altrove. |
| DMC08 | Soft fail | Alcune regole dei contesti sono marcate `[C]`, nonostante `[C]` fosse definito come conferma del referente; la decisione resta prudente ma la provenienza è ambigua. |
| DMC09 | Pass | Limiti economici, capacità e autorità delimitano il problema senza allocazione di spesa. |
| DMC10 | Pass | HR, compliance e variazioni dei Foundations non vengono approvati silenziosamente. |
| DMC11 | Non esercitato | Nessun caso richiedeva davvero una decisione non marketing. |
| DMC12 | Pass | Il caso agenzia viene fermato e trasformato in lettura provvisoria con domande per il cliente. |
| DMC13 | Pass | La causa può restare aperta; risultato e autorità mancanti sono trattati come nodi reali. |
| DMC14 | Pass | Bozza e destinazione sono mostrate; nessun file canonico viene scritto. |
| DMC15 | Parziale | Percorso e prima versione proposta sono corretti; la persistenza non era autorizzata. |
| DMC16 | Pass | Nessuna direzione, campagna, attivazione o test viene progettato. |
| DMC17 | Non esercitato | Nessun caso autorizzava il salvataggio e quindi l'handoff successivo non poteva essere verificato integralmente. |
| DMC18 | Pass | Tutte le prove sono rimaste in sola lettura rispetto ai percorsi canonici. |

## Correzioni decise

La patch `v0.1.1`:

- vieta di attribuire un segnale aggregato al pubblico target senza un collegamento sostenuto;
- riserva `[C]` alle conferme rese nel dialogo e usa `[Sx]` per i contesti canonici, con combinazione ammessa `[C; Sx]`;
- richiede normalmente un ID per ogni fonte materiale e tracciabilità dei conflitti;
- rende esplicito il fallback minimo per un brief cliente fuori perimetro;
- distingue il contenuto confermato in chat dall'artefatto effettivamente salvato.

Queste modifiche non ampliano lo scopo della skill e non cambiano il formato canonico del Brief della sfida.
