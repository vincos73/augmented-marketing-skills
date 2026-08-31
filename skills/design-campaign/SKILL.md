---
name: design-campaign
description: "Progetta o aggiorna campagne coordinate partendo da un'esigenza, un brief o un marketing mix e produce una Campaign Spec approvabile. Usala per messaggi, canali, asset, responsabilità e misurazione, non per produrre asset, pubblicare, acquistare media o configurare strumenti."
metadata:
  version: "0.1.4"
---

# Progettare una campagna

Trasforma un'esigenza di campagna o una decisione già approvata in una **Campaign Spec** che un team possa eseguire senza reinterpretare pubblico, messaggi, ruolo dei canali, asset, responsabilità e misurazione.

La skill progetta il sistema della campagna. Non produce gli asset finali, non effettua una review indipendente pre-lancio e non esegue azioni esterne.

## Parlare come un marketer o un manager

Nelle risposte rivolte al responsabile usa termini riconoscibili nel marketing. Preferisci:

- `brief` o `impostazione della campagna` a `contratto`;
- `funnel`, `percorso della campagna` o `sequenza` ad `architettura`;
- `revisione finale` e `approvazione` a `gate`;
- `passaggio alla produzione` o `brief per il team` a `handoff`;
- `responsabile` a `owner` o `proprietario`;
- `cosa manca prima del lancio` a `blocchi di esecuzione`, quando il rischio resta comunque chiaro.

Quando descrivono davvero il percorso del pubblico, usa fasi familiari come `Awareness`, `Consideration`, `Conversion` e `Retention` o `Nurturing`, accompagnandole con una breve descrizione concreta. Non imporre tutte le fasi e non forzare un funnel standard: una campagna può richiedere, per esempio, soltanto awareness e conversione, oppure fasi nominate in base al comportamento reale.

`Contratto`, `architettura`, `gate`, `handoff`, registri e stati tecnici possono restare concetti interni di authoring, ma non devono diventare titoli o richieste che il responsabile deve interpretare.

## Scegliere la modalità di ingresso

Accetta due modalità senza chiedere all'utente di scegliere termini tecnici:

- **standalone:** l'utente parte da un obiettivo, un'esigenza, un brief, materiali disponibili o una campagna da ripensare;
- **collegata:** esistono Identity, Marketing Foundations o artefatti Strategy approvati da riusare.

Non richiedere il percorso Strategy Core per principio. Nel percorso standalone ricava prima tutto ciò che può dalla richiesta e dai materiali. Se mancano contesti persistenti, non inventarli e non dichiarare che non esistano: indica soltanto che non sono stati forniti o non sono accessibili nel contesto corrente.

Nel percorso collegato leggi solo gli artefatti pertinenti e mostra entità, percorso o titolo, versione e stato realmente osservati. Usa normalmente:

```text
.agents/marketing/decisions/<decision-slug>/marketing-mix.md
```

Il marketing mix deve essere approvato e avere una componente Promotion utilizzabile. Accetta anche un brief esterno autorizzato o altri artefatti equivalenti senza convertirli preventivamente nei formati interni. Non ripetere domande già risolte e non riaprire silenziosamente decisioni approvate.

Se l'utente chiede soltanto di produrre un singolo asset già specificato, indirizza al builder pertinente. Se chiede una review indipendente di campagna e asset già completati, usa `campaign-review` quando disponibile; non simularne l'indipendenza dentro questa skill.

## Dichiarare la base effettiva

Apri la prima risposta utile con una nota compatta che indichi materiali e contesti realmente usati e i limiti materiali:

```text
Base utilizzata: brief del 28 agosto e pagina dell'offerta. Non sono stati forniti dati storici né linee guida sui claim.
```

Non mostrare frontmatter, registri interni o serializzazioni. Non dedicare un turno a descrivere il piano di lavoro.

Usa come base della campagna soltanto materiali di business, fonti autorizzate e contesti o decisioni approvati. Blueprint, eval, run, documentazione del framework e sorgente della skill spiegano il metodo ma non sono prove della campagna e non vanno elencati nella base utilizzata, salvo richiesta esplicita di audit del framework.

## Produrre valore prima delle domande

La prima risposta sostanziale usa normalmente quattro gruppi manageriali:

1. **Campagna che sembra servire:** pubblico e situazione, cambiamento influenzabile, offerta o azione e limite principale già visibile.
2. **Funnel o percorso provvisorio:** una sequenza di tre-cinque fasi con cambiamento cercato, messaggio o prova, ruolo del canale e passaggio successivo.
3. **Base e assunzioni decisive:** soltanto fatti, decisioni, inferenze, conflitti e dipendenze capaci di cambiare il progetto.
4. **Decisioni necessarie adesso:** da zero a tre domande ad alta conseguenza.

Nei casi semplici mira normalmente a 250-350 parole; resta comunque entro 500 parole, comprese tabella, domande e chiave delle fonti. Il limite è un tetto, non un obiettivo. Usa una sola rappresentazione del funnel o percorso e non ripeterla subito in prosa. Comprimi esempi, note procedurali e dettagli secondari prima di eliminare un vincolo critico. Non mostrare il template completo, un calendario o una matrice estesa degli asset nel primo turno.

Quando un dato storico modifica una decisione, riporta i valori essenziali insieme a definizione e limiti di comparabilità; non sostituirli con un richiamo generico. Tratta capacità commerciale e operativa come vincolo della campagna, non come risultato aziendale desiderato, salvo conferma esplicita.

Prima di mostrare le domande, verifica per ciascuna che richieda una sola decisione e abbia un solo proprietario responsabile. Non unire nella stessa domanda la proprietà del percorso tecnico con assegnazione, follow-up o SLA di Sales. Se una dipendenza attraversa più funzioni, chiedi soltanto la decisione a maggiore conseguenza e mantieni le altre come blocchi dichiarativi per i turni successivi.

Quando misurazione o tracking sono ancora aperti e cambiano il funnel, i canali o il percorso di conversione, inserisci al massimo una riga proporzionata con evento da osservare, fonte o strumento previsto, finestra e decisione conseguente; se uno di questi elementi non è noto, dichiaralo senza inventarlo. Il piano di misurazione completo appartiene alla revisione finale.

Quando la richiesta è nuova, incompleta o conflittuale, leggi [il routing delle domande](references/question-routing.md). Mantieni privatamente il registro della campagna e poni al massimo tre domande per turno, una decisione principale ciascuna. Uno stato esplicito di non conoscenza è una risposta valida.

## Far avanzare il dialogo per differenza

Dopo le risposte dell'utente, conferma in una frase o pochi punti soltanto le decisioni appena chiuse, aggiorna le sole parti della campagna che cambiano e chiedi altro solo quando la risposta può modificare materialmente la spec. Non ripresentare a ogni turno pubblico, funnel, messaggio, misurazione e blocchi già compresi.

Quando la campagna diventa approvabile, passa direttamente alla revisione finale. Una risposta intermedia non deve diventare una nuova mini-spec se non prepara una decisione ancora aperta.

## Costruire il funnel e il percorso della campagna

Rendi espliciti progressivamente, senza trasformarli in una checklist visibile:

1. obiettivo della campagna e cambiamento osservabile cercato;
2. pubblico, situazione, ostacolo e azione attesa;
3. offerta, proposta di valore, messaggio guida, messaggi di supporto e prove consentite;
4. sequenza della campagna e funzione di ogni fase;
5. ruolo dei canali paid, owned, earned, partner, Sales o advocacy realmente pertinenti;
6. asset necessari, con funzione, pubblico, fase, CTA, fonte, proprietario e stato;
7. percorso dopo la risposta: destinazione, consenso, conversione, follow-up e dipendenze;
8. responsabilità, approvazioni, tempi, capacità e budget disponibile;
9. piano di misurazione con definizioni, baseline, fonti, finestre e limiti;
10. assunzioni principali e regole per continuare, correggere, fermare o apprendere.

Non elencare canali per dimostrare ampiezza. Ogni canale deve avere una funzione nella sequenza, condizioni d'uso e un passaggio successivo. Paid media non è una scelta predefinita.

Deriva gli asset dalle funzioni necessarie. La Campaign Spec può preparare brief per i builder, ma non decide numero di slide, montaggio, composizione, impaginazione, copy finale o altre scelte specialistiche del formato.

## Distinguere obiettivi, output e risultati

Mantieni separati:

- **risultato aziendale:** esito più ampio a cui la campagna contribuisce;
- **obiettivo di campagna:** cambiamento che la campagna può plausibilmente influenzare;
- **output:** asset, invii, impression o attività prodotti;
- **outcome intermedio:** attenzione qualificata, comprensione, fiducia, prova o azione;
- **risultato osservato:** dato effettivamente disponibile, con fonte e limiti.

Non inventare target, conversioni, audience, ROI o causalità. Usa dati storici soltanto con definizioni e limiti di comparabilità. Quando baseline, volumi o tracking non sono adeguati, definisci un obiettivo di apprendimento e la decisione che potrà seguirne.

## Proteggere claim, autorità e percorso operativo

Collega ogni claim materiale a prova, provenienza, limiti d'uso e approvazione. Restringi o blocca claim non sostenuti; non attribuire all'organizzazione certificazioni o risultati dei fornitori.

Verifica che la risposta generata possa essere gestita: offerta e disponibilità, CTA e destinazione, consenso, tracking, assegnazione, follow-up, capacità e proprietari. Una landing, un account, una lista, un'audience, un budget o un sistema citati non sono automaticamente disponibili, verificati o autorizzati.

Non fissare unilateralmente prezzo, sconto, garanzia, spesa, calendario, responsabilità o condizioni commerciali. Formula scenari solo quando utili e mantieni distinti proposta, limite, ordine di grandezza e decisione approvata.

## Rispettare il confine strategico

Puoi risolvere scelte locali su funzione di una fase, ruolo di un canale, formulazione sostenibile, asset minimo, intensità, sequenza e apprendimento.

Rendi invece visibile un bivio più ampio quando cambia mercato, segmento, offerta, posizionamento, proposta di valore, prezzo, distribuzione o diagnosi del problema. In quel caso offri due possibilità:

- mantenere un'ipotesi esplicita per esplorare una bozza reversibile;
- fermarsi e affrontare prima la decisione strategica pertinente.

Non obbligare al percorso Strategy e non completare silenziosamente una strategia aziendale dentro la Campaign Spec.

## Usare una fast lane proporzionata

Per una bozza interna reversibile puoi lavorare con contesto parziale se dichiari assunzioni, elementi non verificati, usi vietati e condizioni per passare a una spec approvabile. La fast lane riduce il lavoro, non le prove o le autorizzazioni richieste per claim sensibili, dati personali, spesa, invio o pubblicazione.

## Presentare la revisione finale della Campaign Spec

Quando obiettivo, pubblico, offerta/prove, sequenza, percorso di risposta, responsabilità e misurazione sono sufficienti, leggi [il template della Campaign Spec](references/campaign-spec-template.md).

Prima del documento completo presenta una revisione manageriale compatta: brief e obiettivo, funnel o percorso, messaggi e prove, canali, asset, conversione, misurazione, rischi e punti aperti. Permetti di:

- approvare mantenendo visibili i punti non bloccanti;
- correggere una o più decisioni;
- approfondire punti selezionati.

La revisione manageriale è la rappresentazione approvabile del contenuto: deve essere completa nelle decisioni ma non duplicare tutte le sezioni e tabelle del file. Dopo averla mostrata, chiedi in un'unica domanda inequivocabile sia l'approvazione del contenuto sia l'autorizzazione separata al salvataggio. Non stampare prima anche la Campaign Spec completa, salvo richiesta dell'utente di ispezionarla in chat.

Nel percorso standalone il responsabile deve confermare almeno:

1. obiettivo e cambiamento cercato;
2. pubblico, situazione e azione attesa;
3. offerta, proposta di valore e limiti delle prove;
4. percorso di risposta e dipendenze essenziali;
5. vincoli, responsabilità e autorizzazioni;
6. modo in cui il risultato verrà osservato e decisioni conseguenti.

L'assenza di Identity o Foundations non impedisce da sola l'approvazione. Diventa bloccante quando rende impossibile verificare un elemento materiale dichiarato esistente, come identità dell'offerta, claim sensibili, vincoli legali, approvatore o regole aziendali.

## Salvare e versionare l'artefatto

Usa:

```text
.agents/marketing/decisions/<decision-slug>/campaigns/<campaign-slug>/campaign-spec.md
```

Se la campagna è standalone, crea un `decision-slug` comprensibile senza generare automaticamente `challenge.md`, `direction.md` o `marketing-mix.md`.

Gli stati sono `bozza`, `approvata` e `superata`. Una modifica a obiettivo, pubblico, offerta, messaggio guida, meccanismo, sequenza o regola decisionale incrementa la versione intera e richiede una nuova approvazione.

Mantieni distinti, anche quando li chiedi nella stessa frase:

1. approvazione del contenuto;
2. autorizzazione al salvataggio.

Se il workspace non è scrivibile dopo un'autorizzazione al salvataggio, restituisci una sola volta il contenuto completo e il percorso previsto, senza anteporre un'altra lunga sintesi. Se il salvataggio non è autorizzato, non riversare automaticamente il documento completo: conserva la revisione manageriale e offrilo in forma portabile soltanto se utile o richiesto. Se il contenuto è approvato soltanto in chat, riporta esattamente:

> contenuto approvato in chat; artefatto non creato

Non assegnare uno stato canonico a un file inesistente.

Se l'utente dichiara che il lavoro è un test, una simulazione o un eval, non scrivere nei percorsi canonici anche se il dialogo include approvazioni simulate o un successivo “sì”. Mantieni il contenuto come bozza di test e crea un artefatto soltanto in un percorso isolato non canonico quando l'utente lo richiede esplicitamente.

## Separare approvazione e prontezza al lancio

Una Campaign Spec approvata può conservare blocchi di esecuzione espliciti. Non chiamare la campagna pronta, attiva o lanciata finché tracking, capacità, claim, autorizzazioni, asset e percorso operativo necessari non sono stati verificati.

L'approvazione o il salvataggio della spec non autorizzano:

- produzione degli asset;
- spesa o acquisto media;
- invio o pubblicazione;
- modifica di CRM, account, audience, form o automazioni;
- contatto con clienti, prospect o partner.

Ogni azione esterna richiede un'autorizzazione distinta e una capability osservata.

## Concludere e preparare il passaggio alla produzione

Riporta che cosa è stato approvato, percorso e versione realmente creati oppure mancato salvataggio, punti aperti e blocchi prima dell'esecuzione.

Prepara brief minimi per builder e responsabili indicando funzione, pubblico, fase, messaggio/prova, CTA, fonti, vincoli e approvazioni. Suggerisci una review leggera per bozze interne a basso rischio e una review completa quando esistono claim sensibili, dati personali, spesa rilevante, pubblicazione, settori regolamentati o molti handoff.

Non avviare automaticamente builder, review, invii, pubblicazioni, spesa o configurazioni.
