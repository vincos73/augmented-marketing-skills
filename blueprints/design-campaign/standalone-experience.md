---
artifact: design-campaign-experience-blueprint
version: 0.1
status: bozza-di-progettazione
last_reviewed: 2026-08-29
implementation_status: roadmap
---

# Esperienza standalone di `design-campaign`

## Risultato dell'esperienza

Un responsabile marketing deve poter iniziare con una richiesta naturale come:

- «Voglio progettare una campagna per lanciare questo servizio»;
- «Abbiamo questa offerta e questi materiali: aiutami a costruire la campagna»;
- «La campagna attuale non funziona, ripensiamola»;
- «Trasforma questo brief in un piano coordinato».

Non deve conoscere il Marketing Agent System, scegliere un core o possedere artefatti precedenti. La skill usa i contesti approvati quando esistono, ma produce valore anche partendo soltanto dalla richiesta e dai materiali disponibili.

Il risultato è una Campaign Spec approvabile. La conversazione non coincide con un questionario e non anticipa l'intero template nel primo turno.

## Principi di interazione

1. **Proposta prima delle domande.** Ricava un primo funnel o percorso dai materiali prima di chiedere integrazioni.
2. **Linguaggio del lavoro.** Parla di brief, pubblico, funnel, messaggi, prove, canali, azione, responsabilità e risultati; non di contratto, architettura, gate, handoff, campi, core o file.
3. **Massimo tre decisioni per turno.** Una domanda principale per decisione; non accorpare temi che possono avere risposte o proprietari diversi.
4. **Profondità progressiva.** Mostra prima la logica della campagna, poi asset, responsabilità e misurazione.
5. **Contesto proporzionato.** L'assenza di Identity o Foundations non è un errore automatico; claim sensibili, conflitti o autorizzazioni mancanti possono invece bloccare la prontezza.
6. **Bozza reversibile.** Un'ipotesi esplicita può sostenere l'esplorazione, ma non diventa una decisione approvata attraverso la riscrittura.
7. **Nessuna esecuzione implicita.** Approvare o salvare la Campaign Spec non autorizza produzione, spesa, pubblicazione, invio o configurazione.

## Cinque momenti conversazionali

### 1. Attivazione e base utilizzata

La skill identifica che l'utente vuole progettare, correggere o rendere eseguibile una campagna. Legge la richiesta, gli allegati accessibili e gli eventuali contesti pertinenti realmente osservabili.

All'inizio della prima risposta utile mostra una nota compatta:

```text
Base utilizzata: brief del 28 agosto e pagina dell'offerta. Non risultano disponibili linee guida sui claim né dati storici della campagna.
```

Se carica artefatti canonici, indica entità, percorso o titolo, versione e stato. Se non li trova, non dichiara che non esistano: precisa soltanto che non sono stati forniti o non sono accessibili nel contesto corrente. Blueprint, eval e documentazione del framework non diventano fonti della campagna.

Non dedica un turno a descrivere che cosa farà.

### 2. Prima risposta utile

La prima risposta usa normalmente quattro gruppi manageriali.

#### Campagna che sembra servire

Formula in due o tre frasi:

- pubblico e situazione, se sostenuti;
- cambiamento che la campagna dovrebbe influenzare;
- offerta o azione verso cui accompagnare il pubblico;
- limite principale già visibile.

Se uno di questi elementi non è noto, lo mantiene aperto nella formulazione.

#### Funnel o percorso provvisorio

Mostra una sequenza di tre-cinque fasi, non un calendario completo. Usa `Awareness`, `Consideration`, `Conversion` e `Retention` o `Nurturing` quando descrivono davvero il percorso; altrimenti adatta i nomi al comportamento cercato. Per ogni fase indica soltanto:

| Fase | Cambiamento cercato | Messaggio o prova | Ruolo del canale | Passo successivo |
|---|---|---|---|---|
| | | | | |

I canali compaiono per la funzione che svolgono. Non vengono elencati per dimostrare ampiezza e non diventano strategie concorrenti quando appartengono allo stesso sistema.

#### Base e assunzioni decisive

Mostra solo gli elementi che possono cambiare il progetto:

- decisioni o fatti sostenuti;
- inferenze usate nella proposta;
- conflitti o prove mancanti;
- dipendenze operative che possono interrompere il percorso.

Non espone il registro interno completo né serializzazioni tecniche.

#### Decisioni necessarie adesso

Pone da zero a tre domande. Ogni domanda parte da una proposta da confermare o correggere e ammette uno stato esplicito di non conoscenza.

Nei casi semplici la prima risposta mira normalmente a 250-350 parole e resta comunque entro 500 parole, comprese tabella, domande e chiave delle fonti. Il limite è un tetto, non un obiettivo. Usa una sola rappresentazione del funnel o percorso e non la duplica subito in prosa.

### 3. Chiarimento e costruzione

Dopo ogni risposta la skill:

1. conferma in una frase o pochi punti soltanto la decisione acquisita;
2. aggiorna la sola parte del funnel o percorso che cambia;
3. rende visibile l'effetto su messaggi, canali, asset, percorso o misurazione;
4. pone altre domande solo se cambiano materialmente la Campaign Spec.

Non ripresenta a ogni turno l'intero funnel, la misurazione e ciò che manca prima del lancio. Quando le decisioni sono sufficienti passa direttamente alla revisione finale.

Non richiede di definire anticipatamente tutti gli asset. Prima stabilisce il sistema; la matrice degli asset viene derivata dalle funzioni necessarie.

Se emerge un bivio più ampio della singola campagna, presenta il problema in linguaggio manageriale:

```text
La scelta non riguarda soltanto come comunicare: cambia quale pubblico e quale proposta di valore l'azienda intende privilegiare. Posso mantenere una delle due ipotesi per esplorare la campagna in bozza, oppure possiamo fermarci e confrontare prima le direzioni.
```

Non obbliga l'utente a usare lo Strategy Core e non presenta una bozza esplorativa come campagna pronta.

### 4. Revisione finale e approvazione

Quando le decisioni essenziali sono sufficienti, la skill presenta una revisione manageriale compatta prima del documento completo:

- brief e obiettivo della campagna;
- funnel o percorso e ruolo dei canali;
- messaggio guida, prove e limiti;
- asset e responsabilità principali;
- percorso di risposta o conversione;
- misurazione, assunzioni e condizioni di stop;
- conflitti e punti aperti.

Offre tre azioni comprensibili:

- approvare mantenendo visibili i punti non bloccanti;
- correggere una o più decisioni;
- approfondire i punti selezionati.

La revisione manageriale è la rappresentazione approvabile delle decisioni. La skill chiede in un'unica domanda approvazione del contenuto e autorizzazione separata al salvataggio, senza mostrare anche il documento completo salvo richiesta. Se il workspace non è scrivibile dopo l'autorizzazione, restituisce il contenuto completo una sola volta; se il salvataggio non è autorizzato, non duplica automaticamente la revisione.

Durante un test, una simulazione o un eval non scrive nei percorsi canonici anche se il dialogo contiene approvazioni simulate.

### 5. Chiusura e passaggio alla produzione

Dopo il salvataggio o l'approvazione in chat, la skill riporta:

- che cosa è stato approvato;
- percorso e versione realmente creati, oppure il mancato salvataggio;
- punti aperti e condizioni che impediscono l'esecuzione;
- brief per i builder o responsabili necessari;
- revisione consigliata in base al rischio.

Non avvia automaticamente builder, acquisti media, invii, pubblicazioni o modifiche di sistemi. Se l'utente chiede di continuare e la capability è disponibile, il passaggio alla produzione resta una nuova azione osservabile e autorizzata.

## Tre modalità operative

### Progettazione completa

Usala quando l'utente vuole una nuova campagna o il brief è ancora incompleto. Segue i cinque momenti e produce una Campaign Spec nuova.

### Revisione diretta

Usala quando l'utente fornisce un brief di campagna già maturo. La prima risposta non ripete il brief: segnala coerenze, tensioni e decisioni mancanti, poi prepara direttamente la revisione finale.

### Fast lane per bozza interna

Usala quando l'utente chiede un'esplorazione reversibile a basso rischio. La skill può lavorare con contesto parziale se dichiara:

- che cosa è stato assunto;
- che cosa non è stato verificato;
- quali parti non possono essere usate per pubblicazione, spesa o claim sensibili;
- che cosa serve per passare da esplorazione a Campaign Spec approvabile.

La fast lane riduce il lavoro, non i confini di autorità.

## Comportamenti da evitare

- chiedere subito obiettivo, target, budget, canali, KPI e calendario come modulo fisso;
- restituire un elenco generico di tattiche prima di chiarire il meccanismo;
- inventare una persona, un target quantitativo o una baseline;
- confondere un canale con la strategia o l'output con il risultato;
- richiedere Identity o Strategy Core per principio;
- nascondere dietro un tono sicuro un claim, una dipendenza o un'autorità mancanti;
- mostrare il template completo o il frontmatter nella prima risposta;
- dichiarare la campagna pronta perché la Campaign Spec è ben scritta;
- procedere automaticamente alla produzione o all'esecuzione.

## Criteri osservabili per la prima risposta

La prima risposta standalone supera il controllo quando:

- produce una formulazione utile della campagna o un blocker concreto;
- mostra una sequenza, non una collezione di canali;
- distingue almeno ciò che è sostenuto da ciò che è assunto;
- individua le dipendenze capaci di spezzare la risposta o conversione;
- pone non più di tre domande, ognuna su una decisione principale;
- resta entro 500 parole e, nei casi semplici, mira a 250-350;
- non esegue azioni, non salva file e non simula approvazioni;
- non costringe l'utente a conoscere o completare il framework.
