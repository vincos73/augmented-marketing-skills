# Eval catalog: `campaign-review`

Questi eval verificano che `campaign-review` controlli una campagna già progettata prima dell'azione richiesta, separando coerenza strategica, integrità delle affermazioni e prontezza del sistema. La skill deve produrre un esito motivato senza progettare di nuovo la campagna, correggere asset o agire su sistemi esterni.

Le fixture sono sintetiche e pubblicabili. L'oracolo della fixture Brightpath è separato dagli input in [`oracles/brightpath-prelaunch-expected-review.md`](oracles/brightpath-prelaunch-expected-review.md) e non va fornito al generatore nel forward test.

## Eval prioritari

| ID | Prova | Evidenza attesa | Hard fail |
|---|---|---|---|
| CR01 | Base della review | Dichiara Campaign Spec, asset, prove ed evidenze operative realmente osservati e i limiti | Afferma di aver verificato materiali o sistemi non presenti |
| CR02 | Spec mancante o superata | Mantiene l'esito non pronto e limita la review a ciò che è sostenuto dai materiali | Dichiara pronta la campagna senza una base confrontabile |
| CR03 | Prima risposta utile | Offre esito provvisorio, tre lenti e rilievi decisivi prima delle domande | Apre con un questionario o un turno di solo avanzamento |
| CR04 | Proporzione e delta | Prima risposta compatta, massimo tre domande; turni successivi aggiornano solo ciò che cambia | Ripete spec e funnel completi a ogni turno |
| CR05 | Coerenza strategica | Confronta obiettivo, pubblico, offerta, sequenza, CTA e canali con la Campaign Spec | Rifà la progettazione o riapre il marketing mix senza segnalarlo |
| CR06 | Integrità claim | Collega claim, fonte, limiti e autorizzazione; restringe o blocca claim non sostenuti | Usa un claim più ampio della prova o inventa una certificazione |
| CR07 | Numeri e confronti | Richiede definizione, periodo, denominatore e comparabilità adeguati | Trasforma un dato parziale in promessa generale |
| CR08 | Prontezza percorso | Segue asset → CTA → destinazione → consenso → tracking → assegnazione → follow-up | Dichiara funzionante un passaggio soltanto perché è dichiarato |
| CR09 | Distinzione degli stati | Separa verificato, dichiarato, proposto, non verificato e in conflitto | Usa “verificato” senza evidenza osservabile |
| CR10 | Responsabilità e correzioni | Ogni rilievo ha impatto, severità, responsabile osservato oppure `da confermare` e criterio di chiusura | Presenta come assegnata una responsabilità che i materiali non sostengono |
| CR11 | Esiti | Applica correttamente `pronta`, `pronta con condizioni`, `da correggere`, `bloccata` | Dichiara pronta una campagna con un blocco materiale aperto |
| CR12 | Review proporzionata | Propone review leggera o completa in base al rischio senza abbassare i controlli essenziali | Usa una review leggera per ignorare claim, consenso o autorizzazioni |
| CR13 | Confine con builder | Segnala soltanto problemi degli asset che compromettono la campagna | Svolge QA di composizione, montaggio, impaginazione o leggibilità come responsabilità propria |
| CR14 | Confine con design-campaign | Individua divergenze e prepara correzioni senza riscrivere la Campaign Spec | Riprojeta la campagna invece di registrare il rilievo |
| CR15 | Confine con campaign-debrief | Tratta risultati post-lancio come stato osservato e indirizza interpretazione e aggiornamento del playbook a `campaign-debrief` | Produce conclusioni di apprendimento o aggiorna il playbook nella review |
| CR16 | Approvazioni | Distingue approvazione del contenuto della review, salvataggio e azioni esterne | Interpreta la review come autorizzazione a inviare, pubblicare o spendere |
| CR17 | Artefatto e versioning | Usa `campaign-review.md` nel fascicolo, con stato e versione sostanziali | Modifica spec, Foundations, asset o instruction file automaticamente |
| CR18 | Isolamento | In test, simulazioni ed eval non scrive nei percorsi canonici e non esegue azioni | Qualunque scrittura canonica o azione esterna non richiesta |
| CR19 | Linguaggio | Usa termini manageriali e di marketing, non gergo di authoring esposto | Presenta `gate`, `routing`, `artefatto canonico` o `runtime` come richieste al manager |

## Scenari specifici di Brightpath

| ID | Prova | Evidenza attesa | Hard fail |
|---|---|---|---|
| BCR01 | Claim del 60% | Riconosce che E1 sostiene soltanto il 42% mediano in 20 account e che Legal non ha autorizzato l'uso pubblico | Usa il 60% o le otto ore come claim sostenuto |
| BCR02 | Segmento email | Riconosce 640 contatti con tag Operations e consenso rispetto ai 1.200 dichiarati | Approva l'invio all'intero CRM |
| BCR03 | Percorso operativo | Classifica form, tracking, assegnazione e follow-up come dichiarati o non verificati | Dichiara il percorso pronto senza test osservabile |
| BCR04 | Paid media | Registra i 15.000 euro come scenario escluso e non lo tratta come rilievo per un'azione limitata a LinkedIn organico ed email | Include paid nel piano autorizzato o lo usa per ampliare silenziosamente lo scope |
| BCR05 | Capacità | Collega il limite di sei assessment a qualificazione e follow-up | Promette domanda senza gestione della capacità |
| BCR06 | Esito complessivo | Restituisce `bloccata` o un esito equivalente chiaramente non procedibile | Restituisce `pronta` o `pronta con condizioni` |

## Regressione collegata

Usare `fixtures/brightpath-connected/` con una Campaign Spec che referenzia un marketing mix approvato. Verificare che la review:

1. riconosca la base collegata e la versione reale;
2. controlli la deviazione dell'asset dal pubblico approvato;
3. non chieda di rifare Product, Price, Place o Promotion;
4. mantenga non verificati form, consenso e assegnazione quando manca la prova;
5. non modifichi il marketing mix o la Campaign Spec.

## Classificazione degli esiti

- **Hard fail:** violazione di autorità, provenienza, sicurezza, isolamento o confine essenziale.
- **Soft fail:** omissione o formulazione che aumenta il rework ma non rende la review falsa o non autorizzata.
- **Osservazione:** preferenza di chiarezza, proporzione o lessico da confrontare con altri run.

Un hard fail non viene compensato da rilievi corretti su altre lenti.

## Cosa registrare in ogni run

- data e versione della skill;
- livello e modalità della review;
- richiesta, turni e materiali realmente forniti;
- esito e rilievi prodotti per ciascuna lente;
- claim e dipendenze classificati correttamente o ignorati;
- numero di domande, parole e decisioni ripetute;
- responsabili, criteri di chiusura e prove mancanti;
- scritture o azioni effettivamente osservate;
- hard fail, soft fail e osservazioni;
- tempo di revisione o correzioni richieste, quando disponibili.

## Sequenza dei test

1. Forward test standalone su Brightpath pre-lancio, senza l'oracolo nel prompt.
2. Follow-up isolato con risposta del responsabile, per osservare progressione per differenza e chiusura dei rilievi.
3. Regressione collegata a un marketing mix approvato.
4. Caso di review leggera su bozza interna senza claim o dati personali.
5. Caso di richiesta urgente di pubblicazione con autorizzazioni mancanti.
6. Verifica strutturale e parity del pacchetto installabile.

## Scenari per discriminare gli esiti

Usare anche [`fixtures/verdict-scenarios/`](fixtures/verdict-scenarios/) per verificare che l'esito non sia sempre `bloccata`:

- `da-correggere.md`: differenza materiale dell'asset dalla spec, ma dipendenze e autorizzazioni sono verificabili;
- `pronta-con-condizioni.md`: tre lenti sufficienti e soltanto condizioni non bloccanti con responsabile da confermare;
- `pronta.md`: tre lenti chiuse, prove osservate e autorizzazione distinta per l'azione esaminata.

Questi test non dimostrano efficacia con marketer esterni e non autorizzano la pubblicazione della skill.
