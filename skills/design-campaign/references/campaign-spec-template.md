# Template della Campaign Spec

Leggi questo riferimento quando presenti la revisione finale, crei, aggiorni o verifichi una Campaign Spec. Il template è una libreria di campi, non un indice da riprodurre integralmente. Conserva ciò che permette al team di eseguire, controllare e misurare la campagna senza reinterpretarne la logica. Non compilare righe vuote, non copiare documenti già referenziati e non ripetere la stessa decisione in brief, funnel, canali, asset, rischi e passaggio alla produzione.

Usa per default un nucleo compatto: fonti e decisioni di partenza, brief, funnel o percorso, messaggi e prove, attivazione, conversione, misurazione, rischi e autorizzazioni. Sezioni o tabelle separate per messaggi di supporto, canali, asset, responsabilità, budget e fonti entrano soltanto quando aggiungono decisioni, responsabili o limiti non già leggibili nel nucleo. Consolida sezioni affini nei casi semplici.

Scrivi nella lingua di lavoro del responsabile. Mantieni invariati nomi propri, claim approvati e termini tecnici necessari. Durante la revisione manageriale presenta il contenuto in linguaggio naturale e usa il lessico del marketing: brief, funnel o percorso, messaggi, canali, asset, conversione, misurazione e cosa manca prima del lancio. Mostra il frontmatter soltanto nel file generato o nella versione portabile completa richiesta dall'utente, non nella revisione compatta.

```markdown
---
artifact: campaign-spec
version: 1
status: bozza
entity: "[Nome dell'azienda o del brand]"
campaign: "[Nome comprensibile della campagna]"
scope: "[Offerta, pubblico, mercato e periodo coperti]"
owner: "[Responsabile autorizzato]"
entry_mode: standalone | collegata
strategic_basis_status: provvisoria | confermata-per-la-campagna | artefatti-approvati
created: YYYY-MM-DD
last_reviewed: YYYY-MM-DD
business_context_path: null
business_context_version: null
marketing_foundations_path: null
marketing_foundations_version: null
challenge_path: null
challenge_version: null
direction_path: null
direction_version: null
marketing_mix_path: null
marketing_mix_version: null
source_brief: null
supersedes: null
superseded_by: null
---

# Campaign Spec: [Titolo]

## Come usare questa spec

- Usa questo documento come guida condivisa per preparare la campagna, non come autorizzazione automatica all'esecuzione.
- Mantieni distinti decisioni confermate, fonti, inferenze, assunzioni e aspetti sconosciuti.
- Leggi artefatti e fonti referenziati senza copiarli integralmente.
- Affida ai builder le decisioni specialistiche dei singoli formati.
- Verifica separatamente autorizzazioni per produzione, spesa, invio, pubblicazione e configurazione.

## Marcatori di provenienza

- `[C]` confermato nel dialogo da un responsabile autorizzato
- `[S1]`, `[S2]`, ... sostenuto da una fonte elencata
- `[I]` inferito e in attesa di conferma
- `[?]` sconosciuto o irrisolto

Un'assunzione `[C]` è confermata come assunzione, non trasformata in fatto.

## Fonti e decisioni di partenza

| Riferimento | Percorso o fonte | Versione/data | Stato | Cosa sostiene | Limiti |
|---|---|---|---|---|---|
| Brief o richiesta | | | | | |
| Business Identity, se disponibile | | | | | |
| Marketing Foundations, se disponibili | | | | | |
| Sfida, direzione e marketing mix, se disponibili | | | | | |

## Brief della campagna

- **Esigenza o trigger:**
- **Risultato aziendale a cui contribuisce:**
- **Obiettivo che la campagna può influenzare:**
- **Pubblico e situazione:**
- **Ostacolo o condizione da cambiare:**
- **Azione attesa:**
- **Offerta o destinazione:**
- **Perimetro incluso:**
- **Esclusioni:**
- **Orizzonte temporale:**
- **Responsabile della decisione:**

## Scelte strategiche per la campagna

- **Tesi della campagna:**
- **Proposta di valore applicata:**
- **Meccanismo atteso:**
- **Assunzione più fragile:**
- **Che cosa non viene deciso da questa spec:**
- **Stato delle scelte:** provvisorie / confermate per la campagna / derivate da decisioni approvate

Nel percorso standalone, `confermata per la campagna` indica che il responsabile ha confermato le scelte necessarie a questa iniziativa. Non implica una strategia aziendale generale approvata.

## Funnel e percorso della campagna

| Fase | Stato del pubblico | Cambiamento cercato | Messaggio e prova | Ruolo del canale | Azione o passaggio successivo | Segnale osservabile |
|---|---|---|---|---|---|---|
| | | | | | | |

Mantieni normalmente da tre a cinque fasi. Usa `Awareness`, `Consideration`, `Conversion` e `Retention` o `Nurturing` quando descrivono davvero il percorso; altrimenti adatta i nomi al comportamento cercato. Aggiungi fasi solo quando corrispondono a cambiamenti o passaggi reali, non a singole date.

## Sistema di messaggi, claim e prove

### Messaggio guida

- **Formulazione o territorio:**
- **Perché è rilevante per il pubblico:**
- **Prova principale:**
- **Limiti o condizioni d'uso:**

### Messaggi di supporto

| ID | Messaggio o claim | Funzione | Pubblico/fase | Prova | Uso consentito | Approvazione necessaria | Stato |
|---|---|---|---|---|---|---|---|
| M1 | | | | | | | proposto / confermato / bloccato |

Non formulare claim finali oltre ciò che le prove sostengono. Un claim bloccato non viene riutilizzato nei brief degli asset.

## Ruolo dei canali

| Canale o sistema | Funzione nella sequenza | Pubblico e condizione | Fase | Dipendenze o limiti | Responsabile | Cosa non deve fare |
|---|---|---|---|---|---|---|
| | | | | | | |

Paid, owned, earned, partner, Sales e advocacy entrano soltanto quando svolgono una funzione necessaria. Un canale non viene dichiarato disponibile o autorizzato senza riscontro.

## Asset e passaggio alla produzione

| ID | Asset o deliverable | Funzione | Pubblico/fase/canale | Messaggio e prova | CTA e destinazione | Fonte o materiale | Responsabile | Builder o workflow | Stato |
|---|---|---|---|---|---|---|---|---|---|
| A1 | | | | | | | | | necessario / brief pronto / in produzione / disponibile / bloccato |

La Campaign Spec definisce funzione, vincoli e passaggio alla produzione. Non decide numero di slide, montaggio, composizione, formattazione o altri dettagli posseduti dal builder.

## Percorso di risposta e conversione

- **CTA principale:**
- **Destinazione osservata o proposta:**
- **Passaggio successivo:**
- **Follow-up e relativo responsabile:**
- **Disponibilità o capacità necessaria:**
- **Dati raccolti, consenso e limiti:**
- **Punti di interruzione possibili:**

| Passaggio | Sistema o responsabile | Stato osservato | Dipendenza | Comportamento prudente |
|---|---|---|---|---|
| | | verificato / dichiarato / proposto / non disponibile | | |

## Responsabilità, capacità e calendario decisionale

| Attività o decisione | Responsabile | Collaboratori | Approvazione | Scadenza o finestra | Dipendenze | Stato |
|---|---|---|---|---|---|---|
| | | | | | | |

### Capacità e budget

- **Capacità disponibile o limite:**
- **Budget o ordine di grandezza autorizzato:**
- **Base e responsabile:**
- **Che cosa resta da autorizzare:**
- **Conseguenza sul funnel o sul piano:**

Non richiedere un budget numerico se limiti, capacità o scenari bastano a definire responsabilmente il progetto. Non presentare uno scenario come allocazione approvata.

## Piano di misurazione e apprendimento

### Cosa misurare e perché

- **Domanda a cui i dati devono rispondere:**
- **Outcome principale osservabile:**
- **Output da distinguere dall'outcome:**
- **Baseline o confronto disponibile:**
- **Finestra di osservazione:**
- **Fonte dati e responsabile:**
- **Limiti di attribuzione:**

| Segnale o metrica | Definizione | Fase | Fonte | Baseline/target supportato | Finestra | Responsabile | Limiti |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

### Previsioni, assunzioni e regole decisionali

| Previsione o assunzione | Base | Segnale cercato | Se forte | Se debole | Se ambiguo o non misurabile |
|---|---|---|---|---|---|
| | | | continuare / scalare | correggere / fermare | migliorare misura / mantenere aperto |

Non inventare target, ROI o causalità. Quando baseline o volumi non sono adeguati, definisci un obiettivo di apprendimento e la prossima decisione utile.

## Rischi, dipendenze e aspetti aperti

| Tema | Stato | Impatto | Responsabile | Decisione o verifica richiesta | Comportamento prudente |
|---|---|---|---|---|---|
| | bloccante per la spec / bloccante per l'esecuzione / non bloccante | | | | |

## Approvazioni e autorizzazioni

### Approvazione della Campaign Spec

- **Stato:** bozza / approvata / superata
- **Approvata da:**
- **Data dell'approvazione:**
- **Punti aperti accettati:**
- **Autorizzazione al salvataggio:** sì / no

### Azioni esterne

| Azione | Stato dell'autorizzazione | Responsabile | Condizioni | Evidenza osservata |
|---|---|---|---|---|
| Produzione degli asset | non richiesta / richiesta / autorizzata | | | |
| Spesa o acquisto media | non richiesta / richiesta / autorizzata | | | |
| Invio o pubblicazione | non richiesta / richiesta / autorizzata | | | |
| Modifica di sistemi o account | non richiesta / richiesta / autorizzata | | | |

L'approvazione della spec non compila automaticamente questa tabella come `autorizzata`.

## Passaggio alla produzione

- **Asset o brief pronti:**
- **Builder o responsabili suggeriti:**
- **Revisione prima del lancio:** leggera / completa / non necessaria, con motivazione
- **Cosa manca prima del lancio:**
- **Condizione per raccogliere e interpretare i risultati:**
- **Passaggio successivo possibile:** `campaign-review`

## Fonti specifiche

| ID | Fonte | Data di accesso o fornitura | Cosa sostiene | Limiti o sensibilità |
|---|---|---|---|---|
| S1 | | | | |

## Registro modifiche

- v1 (YYYY-MM-DD): prima Campaign Spec approvata.
```

## Criterio di approvazione

La Campaign Spec può diventare `approvata` quando:

- obiettivo, pubblico, situazione, azione attesa e offerta sono comprensibili;
- la base è derivata da artefatti approvati oppure confermata per la singola iniziativa da un responsabile autorizzato;
- messaggi e claim sono sostenuti, limitati o bloccati coerentemente con le prove;
- la sequenza spiega il ruolo di canali e asset;
- il percorso di risposta è praticabile oppure mostra chiaramente i blocchi di esecuzione;
- responsabilità, capacità, limiti e autorizzazioni sono visibili;
- la misurazione distingue output, outcome e risultato aziendale senza attribuzione non supportata;
- assunzioni e regole decisionali permettono di continuare, correggere, fermare o apprendere;
- non resta alcun conflitto bloccante per la logica della campagna;
- il responsabile approva il contenuto e autorizza separatamente il salvataggio.

Una Campaign Spec approvata può conservare blocchi di esecuzione espliciti. Non può chiamarsi pronta al lancio finché tali blocchi non sono risolti e verificati.

## Percorso e versioning

Usa:

```text
.agents/marketing/decisions/<decision-slug>/campaigns/<campaign-slug>/campaign-spec.md
```

Se la campagna non deriva da un fascicolo Strategy esistente, crea un `decision-slug` comprensibile senza generare automaticamente `challenge.md`, `direction.md` o `marketing-mix.md`.

- Prima approvazione: `version: 1`, `status: approvata` e data corrente.
- Modifica sostanziale a obiettivo, pubblico, offerta, messaggio guida, meccanismo, sequenza o regola decisionale: incrementa la versione intera e richiede una nuova approvazione.
- Correzione di solo refuso o collegamento: conserva versione e registro.
- Campagna materialmente diversa: crea un nuovo fascicolo.
- Spec sostituita: imposta `status: superata` e indica `superseded_by`.

Se il workspace non è scrivibile dopo l'autorizzazione al salvataggio, restituisci una sola volta il contenuto completo e il percorso previsto senza dichiarare che il file esista. Se il salvataggio non è autorizzato, non duplicare automaticamente la revisione manageriale con l'intero documento; fornisci la versione portabile soltanto quando è utile o richiesta. Se il contenuto viene approvato soltanto in chat, riporta `contenuto approvato in chat; artefatto non creato`.

Durante test, simulazioni ed eval non scrivere nei percorsi canonici. Eventuali approvazioni simulate non cambiano questo confine.
