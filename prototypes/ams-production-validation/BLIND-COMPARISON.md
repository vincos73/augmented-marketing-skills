# Confronto cieco

Data: 31 agosto 2026

## Metodo

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

Il confronto matched su Claude resta assente e impedisce una conclusione multipiattaforma.
