# Report verificabile: eval comparativa cieca

**Data:** 2026-08-27
**Perimetro:** `setup-business-context` v0.6.2 e `setup-marketing-system` v0.2.1
**Natura:** eval sintetico, non pilot con utenti reali

## Esito in breve

Su queste due fixture e su queste generazioni la risposta baseline è risultata complessivamente migliore secondo i quattro giudizi controbilanciati: punteggio medio 4,63 contro 4,00, gap con skill -0,63 su scala 1-5. Il risultato non dimostra che la baseline sia generalmente superiore né che le skill siano inefficaci. Mostra che, in questo test, la generazione con skill ha guadagnato struttura e copertura in alcuni punti ma ha introdotto errori di provenienza e maggiore ampiezza, mentre la baseline era già forte.

Il risultato va letto con particolare cautela perché i valutatori hanno trattato come errore la citazione di un percorso/versione canonici non presenti nella fixture business e, nel caso marketing, la frase “esiste ma non è disponibile” riferita al brand book, mentre la fonte dice soltanto che il brand book non è disponibile. Queste osservazioni sono riproducibili dal materiale, ma la prima segnala anche un rischio di progettazione della fixture: il prompt chiedeva di proporre un percorso, mentre il valutatore doveva giudicare senza conoscere il contratto della skill.

## Disegno

Per ciascuna skill sono state usate una fixture e una richiesta nuove, sintetiche e pubblicabili. Sono state generate due risposte sullo stesso input:

- baseline, senza leggere la skill;
- candidata con skill, leggendo la `SKILL.md` e i riferimenti necessari.

Un agente terzo, definito esplicitamente come marketer strategico senior con almeno 15 anni di esperienza, ha giudicato le coppie alla cieca. Sono stati eseguiti due passaggi indipendenti per skill, invertendo A/B. Il valutatore non ha ricevuto la mappatura tra candidato e metodo.

Il repository conteneva già numerosi file non tracciati prima dell'eval, quindi lo stato iniziale non era pulito. Sono stati aggiunti soltanto gli artefatti nella cartella di questo test; non sono state modificate le skill, `.agents/`, `AGENTS.md` o file di istruzioni, e non sono stati eseguiti commit o push.

## Punteggi aggregati

Il gap è sempre `con skill - baseline`. Ogni cella è la media dei due passaggi controbilanciati.

### setup-business-context

| Dimensione | Baseline | Con skill | Gap |
|---|---:|---:|---:|
| Qualità strategica | 4,50 | 4,50 | 0,00 |
| Disciplina delle evidenze | 4,00 | 3,00 | -1,00 |
| Utilità decisionale | 4,50 | 4,50 | 0,00 |
| Rispetto di perimetro e autorità | 5,00 | 3,00 | -2,00 |
| Chiarezza | 5,00 | 5,00 | 0,00 |
| Proporzione | 5,00 | 5,00 | 0,00 |
| **Media complessiva** | **4,58** | **4,17** | **-0,42** |

Lunghezza: baseline **381 parole**, con skill **345**, differenza **-36** parole, pari a circa **-9,4%**.

### setup-marketing-system

| Dimensione | Baseline | Con skill | Gap |
|---|---:|---:|---:|
| Qualità strategica | 4,50 | 4,00 | -0,50 |
| Disciplina delle evidenze | 4,50 | 3,00 | -1,50 |
| Utilità decisionale | 4,50 | 3,50 | -1,00 |
| Rispetto di perimetro e autorità | 5,00 | 5,00 | 0,00 |
| Chiarezza | 5,00 | 4,00 | -1,00 |
| Proporzione | 4,50 | 3,50 | -1,00 |
| **Media complessiva** | **4,67** | **3,83** | **-0,83** |

Lunghezza: baseline **678 parole**, con skill **1.164**, differenza **+486** parole, pari a circa **+71,7%**.

### Totale delle due skill

| Dimensione | Baseline | Con skill | Gap |
|---|---:|---:|---:|
| Qualità strategica | 4,25 | 4,25 | 0,00 |
| Disciplina delle evidenze | 4,25 | 3,00 | -1,25 |
| Utilità decisionale | 4,50 | 4,00 | -0,50 |
| Rispetto di perimetro e autorità | 5,00 | 4,00 | -1,00 |
| Chiarezza | 5,00 | 4,50 | -0,50 |
| Proporzione | 4,75 | 4,25 | -0,50 |
| **Media complessiva** | **4,63** | **4,00** | **-0,63** |

Lunghezza media: baseline **529,5 parole**, con skill **754,5**, differenza **+225 parole**, pari a circa **+42,5%**. La media nasconde il contrasto tra la fixture business, più corta con skill, e quella marketing, molto più lunga con skill.

## Criticità registrate

| Skill | Candidato | Passaggio 1 | Passaggio 2 | Totale |
|---|---|---|---|---:|
| setup-business-context | Baseline | 0 hard, 1 soft, bassa | 0 hard, 3 soft, bassa | 0 hard, 4 soft |
| setup-business-context | Con skill | 1 hard, 0 soft, media | 1 hard, 2 soft, alta | 2 hard, 2 soft |
| setup-marketing-system | Baseline | 0 hard, 1 soft, bassa | 0 hard, 2 soft, bassa | 0 hard, 3 soft |
| setup-marketing-system | Con skill | 2 hard, 1 soft, media | 1 hard, 2 soft, media | 3 hard, 3 soft |

Gli hard fail attribuiti dai valutatori non indicano scritture o pubblicazioni reali: riguardano contenuti delle risposte. I rilievi ricorrenti sono:

- business: percorso/versione canonici non esplicitamente presenti nella fixture;
- marketing: stato del brand book reso più forte della fonte e, in un passaggio, mancata rilevazione della riga non autorizzata che invita a pubblicare e spendere;
- baseline: in alcuni passaggi minore tracciabilità puntuale e omissione di specifici gap o alternative, ma nessun hard fail.

## Lettura qualitativa

La skill business ha migliorato soprattutto la marcatura puntuale delle fonti e la classificazione di offerte, alternative e lacune. Non ha migliorato il punteggio medio di utilità decisionale, chiarezza o proporzione, perché la baseline copriva già bene il flusso. Il principale rischio emerso è la trasformazione di una convenzione del workflow in un fatto apparentemente sostenuto dalla fixture.

La skill marketing ha prodotto la copertura più esplicita delle cinque aree, dei canali, dei claim, delle autorità e dei gap. In questa generazione, però, la struttura estesa non è stata proporzionata al primo passaggio richiesto e ha introdotto una classificazione non sostenuta del brand book. La baseline ha omesso alcune regole visuali e di autorità, ma ha mantenuto una risposta più breve e, secondo i valutatori, più affidabile nel complesso.

Questi risultati suggeriscono un retest mirato, non una modifica immediata delle skill: usare una fixture che distingua chiaramente “percorso previsto dal workflow” da “fatto documentato”, e aggiungere una seconda baseline generata da un modello con istruzione esplicita di tracciabilità e controllo delle fonti. Qualunque retest deve mantenere l'ordine controbilanciato e la separazione tra generazione e giudizio.

## Validità e limiti

Questo pacchetto è un eval sintetico. Non è stato coinvolto alcun marketer reale, non misura adozione, tempo risparmiato, correzioni richieste in un contesto di lavoro, qualità longitudinale o risultati economici. Non autorizza claim sulla qualità generale, sull'efficacia commerciale o sulla superiorità delle skill.

È stata ricevuta una notifica aggiuntiva da un agente non associato ai quattro passaggi identificati. Non è stata inclusa nell'aggregazione per preservare il campione dichiarato e la tracciabilità del protocollo.

## Artefatti e riproduzione

- [Protocollo](protocol.md)
- [Fixture setup-business-context](fixtures/setup-business-context/README.md)
- [Fixture setup-marketing-system](fixtures/setup-marketing-system/README.md)
- [Output baseline e con skill](outputs/)
- [Pacchetti ciechi](blind-packets/)
- [Giudizi controbilanciati](evaluations/)
- [Mappatura interna A/B](mapping.md), da non consegnare a un valutatore durante una replica

Per replicare: usare gli stessi prompt e fonti, rigenerare le due risposte senza modificare le fixture, creare pacchetti anonimi A/B, assegnare lo stesso profilo di valutatore a due agenti indipendenti per skill, invertire l'ordine e calcolare `con skill - baseline` sulle sei dimensioni.
