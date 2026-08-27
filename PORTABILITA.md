---
artifact: portability-contract
version: 2
status: approvato
last_reviewed: 2026-08-27
scope: "Contratto minimo di portabilità per skill installabili di Augmented Marketing Suite"
---

# Contratto di portabilità

## Scopo

Augmented Marketing Suite deve mantenere lo stesso metodo, gli stessi confini di autorità e gli stessi artefatti essenziali negli ambienti che supportano l'installazione di skill, senza dipendere dalle funzioni esclusive di un singolo agente o fornitore.

Portabilità non significa esperienza identica su ogni piattaforma. Significa che una skill conserva il proprio risultato essenziale quando cambiano filesystem, connector, interfacce visuali, subagenti o altre capability opzionali.

## Principio di minima implementazione

Il contratto non introduce un nuovo layer software. Ogni skill applica soltanto i fallback necessari al proprio risultato. Router comuni, manifest trasversali, adattatori e connector dedicati vengono progettati solo quando un problema ripetuto e osservato dimostra che servono.

## Ambiente minimo supportato

Un ambiente rientra nel perimetro quando:

1. può installare o caricare una skill e le sue risorse incluse;
2. rende disponibili all'agente le istruzioni della skill durante il lavoro;
3. permette una conversazione in cui l'utente può fornire fonti, revisionare una proposta e approvare o rifiutare le decisioni.

I chatbot privi di un sistema di skill non fanno parte del perimetro minimo.

## Capability

| Livello | Capability | Contratto |
|---|---|---|
| obbligatoria | Skill installabile e caricabile | `SKILL.md` e le risorse necessarie devono essere disponibili all'agente |
| obbligatoria | Conversazione interattiva | Domande, revisioni e approvazioni devono poter avvenire senza un'interfaccia proprietaria |
| preferibile | Lettura e scrittura nel workspace | Permette artefatti persistenti, versionati e riusabili |
| opzionale | File allegati o cartelle esterne | Possono fornire fonti, ma non devono essere l'unico ingresso possibile |
| opzionale | Web e connector | Possono aggiornare o ampliare le evidenze, senza diventare dipendenze silenziose |
| opzionale | Subagenti, viste visuali e automazioni | Possono migliorare revisione e verifica, ma non possiedono lo stato canonico |

Una skill non deve dichiarare disponibile una capability che non ha osservato. Se una capability opzionale manca, deve indicare l'impatto concreto e continuare quando il risultato essenziale resta ottenibile.

## Contratto degli artefatti

Gli artefatti canonici restano Markdown leggibile, con percorso, versione, stato, riferimenti e provenienza espliciti.

- Se il workspace è scrivibile, la skill mostra il contenuto e il percorso proposti, ottiene l'autorizzazione richiesta e salva l'artefatto.
- Se il workspace non è scrivibile, la skill restituisce in chat il contenuto completo e il percorso previsto. Deve dichiarare `contenuto approvato in chat; file non creato` e non attribuire al risultato una versione canonica o uno stato osservabile su disco.
- Se un input necessario esiste ma non è accessibile, la skill chiede di allegarlo, incollarlo o renderlo disponibile attraverso una capability autorizzata. Non lo ricostruisce per supposizione.
- Nessuna decisione approvata deve esistere soltanto in memoria implicita, in uno stato nascosto o in una vista proprietaria.

La presenza di un file sorgente, l'installazione della skill, il caricamento nella sessione e la creazione di un artefatto sono stati distinti e devono essere riportati separatamente.

## Connector e strumenti esterni

Nessuna skill del nucleo Fondazione o Strategy Core richiede un connector per produrre il proprio risultato essenziale.

Quando un connector o uno strumento esterno è disponibile e pertinente:

- la skill può usarlo per acquisire o verificare evidenze;
- registra fonte, data e limiti del dato usato;
- distingue indisponibilità, errore e assenza di risultati;
- non sostituisce una verifica fallita con una certezza non supportata;
- non interpreta l'autorizzazione alla lettura come permesso di scrittura, pubblicazione, invio, acquisto o configurazione.

Le azioni esterne richiedono un'autorizzazione distinta e appartengono a workflow che dichiarano esplicitamente effetti, target e condizioni di arresto.

## Adattatori di ambiente

Comandi, manifest, hook, marketplace, instruction file e procedure di installazione specifiche sono adattatori, non il nucleo del prodotto.

Un adattatore può migliorare scoperta, caricamento, diagnostica o sicurezza, ma non può cambiare:

- lo scopo della skill;
- l'artefatto canonico;
- i marcatori di provenienza;
- i gate di approvazione;
- i confini tra decisione ed esecuzione.

Le istruzioni essenziali devono restare nella cartella distribuibile della singola skill. Un pacchetto installato separatamente non deve dipendere dalla presenza di questo documento nel repository.

### Adattatore OpenAI osservato

Il caricamento di un archivio generico in una chat ChatGPT non registra automaticamente skill o agenti. Per ChatGPT e Codex, la beta.3 distribuisce Augmented Marketing Suite (`augmented-marketing-suite`) con un manifesto `.codex-plugin/plugin.json` e presenta Augmented Marketing Assistant come skill tecnica di coordinamento (`augmented-marketing-assistant`). Questa forma non cambia il ruolo dell'Assistant: continua a orientare, mentre le cinque skill specialistiche possiedono metodo, artefatti e approvazioni.

L'adattatore OpenAI non introduce MCP, connector o nuove capacità di marketing. La sua installazione e il suo caricamento devono essere verificati in una nuova chat o sessione.

## Verifica minima

Ogni skill nuova o aggiornata deve essere verificata almeno in questi scenari:

1. workspace leggibile e scrivibile;
2. workspace leggibile ma non scrivibile;
3. fonte necessaria non accessibile;
4. capability opzionale disponibile;
5. capability opzionale assente o fallita;
6. installazione presente ma caricamento nella sessione non verificato.

La verifica strutturale dimostra la validità del pacchetto, non la portabilità del comportamento. Le differenze tra ambienti devono essere osservate con forward test separati.

## Decisioni ancora aperte

- quali ambienti con skill usare nel primo pilot comparativo;
- quali adattatori di installazione mantenere ufficialmente;
- se introdurre un manifest comune di release;
- quando un caso d'uso ripetuto giustifica un connector dedicato;
- come documentare in modo uniforme le capability osservate a runtime.

## Registro modifiche

- v2, 2026-08-27: documentato l'adattatore OpenAI dopo il fallimento osservato del bundle neutro su ChatGPT Web.
- v1, 2026-08-27: definito il contratto minimo indipendente dalla piattaforma.
