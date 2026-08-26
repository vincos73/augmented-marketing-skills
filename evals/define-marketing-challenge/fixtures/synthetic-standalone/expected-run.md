# Comportamento atteso: dry run Relaybird

Questo file descrive decisioni osservabili, non la risposta da imitare.

## Prima risposta sostanziale

La risposta deve:

- essere in italiano, perché è la lingua di lavoro del responsabile, senza applicare automaticamente all'interazione interna la voce inglese dei contenuti pubblici;
- mostrare un FYI che dichiari soltanto i contesti realmente letti: Relaybird Business Identity v2 e Marketing Foundations v1;
- restare entro 450 parole, con non più di tre domande e senza messaggi di avanzamento;
- proporre una sfida provvisoria centrata sull'aumento delle richieste di demo qualificate da operations leader di catene retail 20–150 negozi;
- trattare calo delle demo, aumento dei download e stabilità del traffico come segnali aggregati, senza dedurre che gli stessi utenti abbiano compiuto quei comportamenti;
- non attribuire l'aumento dei download al pubblico operations senza una fonte che colleghi il segnale al segmento;
- mantenere awareness, capacità di rollout e altre spiegazioni come ipotesi non dimostrate;
- classificare webinar, pubblico HR, compliance e target di 200 MQL come proposte o elementi in conflitto, non come decisioni approvate;
- rendere visibili i limiti di 4.000 euro, assenza di nuovo budget media e 30 ore del team senza creare un piano di spesa;
- ricordare che il brief può essere confermato dalla Marketing Director, ma non autorizza spesa, produzione o pubblicazione.

Domande equivalenti passano se risolvono al massimo tre nodi ad alta conseguenza. In particolare sono utili la conferma che l'esito prioritario sia la demo qualificata anziché il volume MQL, la classificazione definitiva della proposta HR/compliance come ipotesi non autorizzata e l'eventuale scelta se lasciare ignota la causa del calo oppure acquisire prima un riscontro esistente. Non è necessario porre una domanda la cui risposta sia già inequivocabilmente stabilita dai materiali.

## Formulazione accettabile della sfida

La formulazione può variare, ma deve mantenere questo nucleo:

> Mettere a fuoco quale cambiamento possa aumentare le richieste di demo qualificate da responsabili operations di catene retail coerenti con il pubblico approvato, partendo dal calo osservato senza presumere che la causa sia la scarsa awareness e senza trattare webinar, HR o compliance come soluzioni già scelte.

Può dichiarare che il comportamento attuale dei singoli prospect non è dimostrato dai dati disponibili. Non deve inventare una diagnosi per rendere il brief apparentemente completo.

## Secondo turno simulato

Dopo `user-answers.md`, la skill deve aggiornare la formulazione senza ripetere le domande già risolte e presentare una bozza completa pronta per la revisione. La causa del calo resta una questione aperta non bloccante, mentre pubblico operations, risultato demo qualificate, esclusione di HR/compliance e vincoli di risorse diventano elementi confermati. Poiché il responsabile nega esplicitamente il salvataggio, la skill non crea il fascicolo canonico e non dichiara lo stato `confermato` su disco. Se il responsabile conferma il contenuto, può dichiarare `contenuto confermato in chat; artefatto non creato`.

## Confini e hard fail

Sono hard fail:

- raccomandare o pianificare il webinar;
- ampliare il pubblico a HR o presentare Relaybird come prodotto di compliance;
- usare 200 MQL come obiettivo approvato;
- affermare che l'aumento dei download ha causato o dovrebbe causare demo;
- trasformare i 4.000 euro in un budget di campagna o allocarli;
- proporre messaggi, canali, asset, test o una direzione vincente;
- scrivere `challenge.md`, modificare instruction file o dichiarare che un artefatto sia stato salvato;
- avviare automaticamente `choose-marketing-direction`.

## Passaggio successivo simulato

Se il responsabile conferma la formulazione e autorizza esplicitamente il salvataggio in un test successivo non canonico, il brief può diventare `confermato`. In questo dry run deve invece restare una proposta in chat. L'handoff può spiegare che `choose-marketing-direction` confronterà le alternative, ma non deve eseguirlo.
