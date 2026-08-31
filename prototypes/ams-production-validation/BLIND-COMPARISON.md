# Confronto cieco

Data: 31 agosto 2026

## Metodo Codex

Le risposte Codex congelate sono state copiate con tre codici anonimi. Sono stati rimossi nomi di
candidato, marker architetturali e riferimenti espliciti alle skill. Il valutatore, eseguito in un
profilo pulito con `gpt-5.6-sol` e reasoning `xhigh`, ha letto soltanto:

- le tre risposte anonime;
- i cinque materiali Fabriloom;
- le decisioni controllate e i risultati sintetici;
- `EVAL-RUBRIC.md`.

La chiave è rimasta in `private/blind-key.md` fino al congelamento della valutazione. Dopo il
congelamento la mappatura è risultata:

| Codice cieco | Candidato |
|---|---|
| ORCHID | Vertical Slice v0.1.2 |
| RIVER | CURRENT beta.8 |
| LANTERN | GENERALIST |

Il valutatore aveva contato come gap l'assenza dei marker rimossi per l'anonimizzazione. Dopo la
rivelazione, quei rilievi sono stati esclusi: i marker esistono nell'evidenza Vertical Slice
originale e non sono requisiti di CURRENT o GENERALIST.

## Risultato comparativo

| Misura | VERTICAL | CURRENT | GENERALIST |
|---|---:|---:|---:|
| Hard fail | 0 | 1 | 0 |
| Soft fail sostanziali | 2 occorrenze di conferme accorpate | 3 criteri | 3 criteri |
| Fasi completate | 8/8 | 4/8 | 8/8 |
| Claim materiali inventati | 0 | 0 | 1, corretto in review |
| Domande ripetute | 0 | 1 | 2 |
| Continuità | alta | alta fino all'arresto | buona |
| Chiarezza per marketer | alta, più densa | buona fino al finale | molto buona |
| Rework | basso | strutturale | medio |
| Invocazioni tecniche nel percorso | 0 con router automatico | 5 | 0 |
| Contesto da ripetere | nessuno sostanziale | stato da trasferire alla capacità mancante | basso |

## Classifica cieca

1. **VERTICAL**: migliore copertura e coerenza decisionale.
2. **GENERALIST**: completo e sicuro, con più riconferme e più rework.
3. **CURRENT**: accurato nelle prime fasi, ma incapace di completare il percorso.

## Vantaggio rispetto al generalista

La Vertical Slice mostra un vantaggio reale ma circoscritto su Codex:

- rappresenta esplicitamente Product, Price, Place e Promotion;
- collega in modo coerente direzione, campagna, funzione dell'asset e CTA;
- arriva alla review con un asset già collocato correttamente nel percorso;
- non riapre informazioni già stabilite;
- richiede meno revisione sostanziale.

Il GENERALIST conserva un vantaggio di leggibilità nel calendario della campagna e completa tutto
il percorso senza attrito tecnico. La Vertical Slice non dimostra quindi un vantaggio universale:
dimostra una migliore governance decisionale su questo singolo compito controllato.

CURRENT non mostra un vantaggio end-to-end rispetto al generalista. La prudenza dell'arresto evita
di inventare una capacità, ma trasferisce all'utente il costo di colmare metà del percorso.

## Numerosità

Non sono state aggiunte repliche. Una prova per candidato è coerente con il baseline v0.1.2 e il
risultato Codex non è ambiguo: due candidati completano 8/8, uno si ferma a 4/8; tra i due completi
le differenze di rework sono osservabili e localizzate. Questo non misura la variabilità tra run.

## Valutazione cieca Claude

Le tre risposte Claude sono state congelate e anonimizzate con codici diversi da quelli Codex. Un
nuovo valutatore isolato, eseguito con `gpt-5.6-sol` e reasoning `xhigh`, ha ricevuto soltanto i
tre candidati anonimi, i materiali Fabriloom, le decisioni controllate, i risultati sintetici e
la rubrica. La mappatura è stata aperta solo dopo il congelamento della valutazione:

| Codice cieco | Candidato |
|---|---|
| MICA | GENERALIST |
| PINE | Vertical Slice v0.1.2 |
| QUARTZ | CURRENT beta.8 |

| Misura | VERTICAL | CURRENT | GENERALIST |
|---|---:|---:|---:|
| Hard fail | 4 criteri | 2 criteri | 4 criteri |
| Fasi completate | 8/8 | 4/8 | 8/8 |
| Claim o decisioni inventate | 1 claim quantitativo nell'asset | 0 | 1 claim empirico e 1 durata non supportata nell'asset |
| Domande dirette | circa 14 | 12 in quattro fasi | 24 |
| Continuità | alta, con scelta anticipata della soluzione | buona fino all'arresto, con due decisioni riaperte | alta |
| Chiarezza per marketer | la migliore e più compatta | buona fino all'arresto | alta, ma verbosa |
| Rework | alto su asset e apprendimento | strutturale | alto su asset e apprendimento |
| Attrito manuale | medio | molto alto | basso tecnicamente, alto conversazionalmente |
| Contesto da ripetere | basso | medio-alto | basso |

La classifica cieca Claude è:

1. **GENERALIST**, per copertura completa, continuità e capacità di autocorrezione;
2. **VERTICAL**, molto vicino al primo e più leggibile, ma con un claim inventato non rilevato in
   review e conclusioni causali eccessive;
3. **CURRENT**, accurato e prudente nelle prime quattro fasi, ma incompleto per costruzione.

Tutti e tre risultano `NO-GO` se giudicati come singole risposte con la soglia rigida della
rubrica. Per VERTICAL e GENERALIST pesano soprattutto claim non supportati e conclusioni causali
che i dati non consentono. Per CURRENT pesa la mancanza della capacità end-to-end. Questa nuova
valutazione non riscrive il referto v0.1.2 congelato: applica la rubrica al nuovo confronto
pre-produzione e rende visibili errori sostanziali che il controllo strutturale precedente non
aveva escluso.

## Conclusione tra harness

| Harness | Primo | Secondo | Terzo |
|---|---|---|---|
| Codex | VERTICAL | GENERALIST | CURRENT |
| Claude | GENERALIST | VERTICAL | CURRENT |

Il vantaggio della Vertical Slice sul GENERALIST non è stabile tra i due harness. Su Codex emerge
una migliore governance decisionale e meno rework; su Claude il GENERALIST è leggermente avanti
per completezza e autocorrezione, ma nessuno dei due supera la soglia rigida. CURRENT arriva
ultimo in entrambi e non dimostra un vantaggio reale end-to-end.

Non sono state aggiunte repliche. La conclusione di prodotto non è ambigua: il limite di CURRENT
è strutturale e si ripete sui due harness. La vicinanza fra VERTICAL e GENERALIST rende instabile
la loro classifica relativa, ma un'altra replica prima del redesign non risolverebbe la capacità
mancante né i difetti di claim e causalità. Le nuove prove matched vanno eseguite dopo le
correzioni.
