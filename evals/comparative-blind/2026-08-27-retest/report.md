# Report del retest comparativo cieco

Data: 2026-08-27
Ambito: `setup-business-context` e `setup-marketing-system`
Tipo: eval sintetico, non validazione con utenti reali

## Esito in breve

Il retest corregge due confondenti dell'eval iniziale: la penalizzazione impropria di percorso/versione proposti e il confronto della skill soltanto con una baseline libera. Il risultato è misto:

- `setup-business-context`: vantaggio complessivo con skill di **+0,25 punti su 5**.
- `setup-marketing-system`: svantaggio complessivo con skill di **-0,13 punti su 5**.
- media non ponderata delle due skill: **+0,06 punti su 5**, non sufficiente per sostenere una superiorità generale.
- hard fail: **0 su tutti i 16 candidati giudicati**.

Contro la baseline libera, la skill business prevale in entrambi i passaggi. Contro la baseline source-disciplined prevale in un passaggio su due. Per marketing, la baseline prevale in tutti e quattro i passaggi. Il risultato quindi non giustifica un claim generale di efficacia delle skill.

## Disegno verificabile

Per ciascuna skill sono state generate tre risposte sulla stessa fixture sintetica, neutrale e pubblicabile:

1. baseline libera, senza skill e senza istruzioni aggiuntive;
2. baseline source-disciplined, senza skill ma con una richiesta generica di tracciabilità, gap e disciplina delle fonti;
3. risposta con la skill pertinente.

Ogni baseline è stata confrontata con la risposta con skill in due passaggi indipendenti, invertendo A/B. Totale: 8 giudizi ciechi, 4 per skill. Ogni valutatore ha ricevuto esplicitamente il profilo di **marketer strategico senior con almeno 15 anni di esperienza**, la fixture, la richiesta, la rubrica neutrale e due candidati anonimi. Non ha ricevuto la mappatura, il nome dei generatori o le `SKILL.md`.

Il gap è calcolato come `media con skill - media baseline`, con punteggio da 1 a 5. Le dimensioni sono: qualità strategica, disciplina delle evidenze, utilità decisionale, rispetto di perimetro e autorità, chiarezza e proporzione.

## Gap per dimensione

### `setup-business-context`

| Dimensione | vs baseline libera | vs baseline source-disciplined | complessivo |
|---|---:|---:|---:|
| Qualità strategica | +0,75 | +0,50 | +0,75 |
| Disciplina delle evidenze | +0,75 | +0,50 | +0,75 |
| Utilità decisionale | +0,25 | 0,00 | +0,25 |
| Perimetro e autorità | 0,00 | 0,00 | 0,00 |
| Chiarezza | 0,00 | -0,50 | -0,25 |
| Proporzione | 0,00 | 0,00 | 0,00 |
| **Media complessiva** | **+0,42** | **+0,08** | **+0,25** |

La skill migliora soprattutto tracciabilità, alternative e gestione dei limiti quando il confronto è con la baseline libera. Il vantaggio si riduce quasi a zero contro una baseline già source-disciplined. Un valutatore ha preferito la baseline per maggiore compattezza e chiarezza.

### `setup-marketing-system`

| Dimensione | vs baseline libera | vs baseline source-disciplined | complessivo |
|---|---:|---:|---:|
| Qualità strategica | -1,00 | 0,00 | -0,50 |
| Disciplina delle evidenze | -0,50 | 0,00 | -0,25 |
| Utilità decisionale | -1,00 | -1,00 | -1,25 |
| Perimetro e autorità | 0,00 | 0,00 | 0,00 |
| Chiarezza | +1,00 | 0,00 | +0,50 |
| Proporzione | +1,00 | +0,50 | +0,75 |
| **Media complessiva** | **-0,08** | **-0,08** | **-0,13** |

La skill rende la risposta più compatta e proporzionata, ma perde utilità decisionale. Le osservazioni ricorrenti riguardano l'omissione o la minore esplicitazione del conflitto Q4 e di alcune alternative operative già presenti nella baseline. Il compromesso non è favorevole alla skill nel compito testato.

## Lunghezza

Il limite comune era 450 parole per business e 650 per marketing.

| Skill | Baseline libera | Baseline source-disciplined | Con skill |
|---|---:|---:|---:|
| `setup-business-context` | 386 | 387 | 402 |
| `setup-marketing-system` | 625 | 567 | 605 |

Tutte le risposte rispettano il limite. La lunghezza non spiega da sola il risultato: la risposta marketing con skill è più corta della baseline libera, ma riceve un punteggio inferiore nell'utilità decisionale.

## Hard fail, soft fail e criticità

Non sono stati rilevati hard fail. I soft fail sono stati registrati separatamente e rappresentano gruppi di omissioni o debolezze, non violazioni critiche.

| Skill | Condizione | Soft fail baseline | Soft fail con skill | Criticità osservata |
|---|---|---:|---:|---|
| Business | vs libera | 2 | 0 | bassa / molto bassa per la skill |
| Business | vs source-disciplined | 1 | 0 | bassa |
| Marketing | vs libera | 3 | 5 | bassa per baseline, bassa-media per skill |
| Marketing | vs source-disciplined | 4 | 5 | bassa-media per entrambi |

Le schede normalizzate dei singoli giudizi sono in `evaluations/BC1.md`-`BC4.md` e `evaluations/MS1.md`-`MS4.md`.

## Interpretazione e limiti

Questo è un eval sintetico controllato. Dimostra come gli output sono stati giudicati su fixture costruite per il test e secondo una rubrica definita, non dimostra adozione, risparmio di tempo, accuratezza in contesti reali, qualità percepita da marketer reali o risultati di business.

Non sono stati usati casi, identità o risultati reali di Vincos e non sono stati prodotti claim di marketing sulla Suite o sulle skill. Un piccolo flusso di notifiche provenienti da agenti non associati ai pacchetti del retest è stato escluso dal campione e non contribuisce ai risultati; i soli giudizi inclusi sono BC1-BC4 e MS1-MS4.

Il retest suggerisce una decisione prudente: mantenere `setup-business-context` come candidata promettente, ma verificarla contro baseline professionali disciplinate; non promuovere `setup-marketing-system` sulla base di questo test, e usarne il risultato per un ulteriore ciclo mirato sull'utilità decisionale e sulla conservazione dei conflitti operativi.

## Artefatti e integrità del repository

- Protocollo: [`protocol.md`](./protocol.md)
- Prompt: [`prompts.md`](./prompts.md)
- Manifest delle fonti: [`source-manifest.md`](./source-manifest.md)
- Pacchetti ciechi: [`blind-packets/`](./blind-packets/)
- Output candidati: [`outputs/`](./outputs/)
- Mappatura interna, non fornita ai valutatori: [`mapping.md`](./mapping.md)
- Schede dei giudizi: [`evaluations/`](./evaluations/)

Le fixture originali sono state riusate senza modifica. Nessuna skill è stata modificata, nessun file fuori da `evals/comparative-blind/` è stato modificato per questo retest, e non sono stati eseguiti commit o push.
