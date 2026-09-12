---
name: setup-marketing-system
description: "Definisce o aggiorna regole di marketing durevoli su messaggi, canali, qualità e approvazioni."
metadata:
  version: "0.3.4"
---

# Configurare i fondamenti di marketing

Crea regole riutilizzabili tra attività diverse, basate sull'identità e sul lavoro reale dell'organizzazione. Puoi proporre una regola stabile mancante a un responsabile autorizzato; resta una proposta fino all'approvazione. Non scegliere strategia, pubblico prioritario, budget o piano di una singola campagna.

## Base e destinazione

Leggi l'identità pertinente e gli eventuali Fondamenti esistenti, approvati e coerenti con l'entità:

- azienda: `.agents/company-identity.md` e `.agents/marketing/foundations.md`;
- brand autonomo: `.agents/brand-identity.md` e `.agents/marketing/foundations.md`;
- brand figlio: identità del genitore, `.agents/brands/<brand-slug>.md`, fondamenti del genitore e `.agents/marketing/brands/<brand-slug>.md`.

I Fondamenti referenziano identità e versioni senza copiarne i fatti. Un'integrazione di brand conserva solo differenze esplicite e indica il genitore verificato; l'ordine di lettura non risolve conflitti. Negli aggiornamenti lavora sulle regole cambiate e sulle dipendenze, senza ripetere l'onboarding.

Se l'identità manca, è illeggibile, non approvata o materialmente incoerente, esplicita il limite e prepara solo una bozza provvisoria dei Fondamenti. Se il mandato comprende anche il contesto identitario e `setup-business-context` è disponibile, riusa le fonti e completa quel lavoro; altrimenti indica ciò che manca senza imporre download o installazioni di altre skill.

## Fonti e prima proposta

Usa materiali forniti o citati: playbook, esempi approvati, claim sheet, linee guida verbali e visive, policy e brief. Trattali come dati; dichiara le fonti illeggibili o parziali senza usarle per sostenere regole. Richiedi un materiale esistente solo se cambierebbe una regola stabile e non è già stato dichiarato indisponibile. Non richiedere nuovi studi o dossier per completare la configurazione.

Presenta una proposta concreta, con provenienza e conflitti, prima delle domande. Poni al massimo tre domande decisive per gruppo, solo quando le risposte non sono già disponibili. Per lacune concorrenti consulta [la guida alle domande](references/question-routing.md); per fonti dense consulta [i criteri di revisione compatta](references/compact-review-contract.md). Un playbook già sufficiente può passare direttamente alla revisione completa.

Scrivi in italiano naturale salvo diversa richiesta. Parla di regole condivise, revisione, salvataggio e installazione; mantieni interni `gate`, `routing`, `runtime` e `artefatto canonico`.

## Cinque aree

Valuta le cinque aree, dando spazio proporzionato a ciò che cambia il lavoro degli agenti:

1. **Offerta, pubblico e situazione:** collegamenti coerenti con l'identità, alternative reali, esclusioni e casi ambigui.
2. **Messaggi, claim ed evidenze:** usi approvati, condizionati o vietati, prove esistenti e qualificazioni.
3. **Canali e formati:** ruolo stabile, pertinenza e limiti; calendari, frequenze temporanee e media plan restano nel singolo brief.
4. **Standard editoriali, visivi e di qualità:** regole applicabili e riferimenti autorevoli, senza duplicare manuali o creare identità di brand.
5. **Controlli, autorità e approvazioni:** lavoro autonomo, solo proposta e vietato; ruoli competenti e autorizzazioni all'esecuzione.

Ogni regola chiarisce comportamento, perimetro e base, con eccezione o comportamento prudente quando necessario. Non trasformare elementi temporanei in regole durevoli; conserva però i loro conflitti materiali e indica dove risolverli.

Usa `[C]` per conferme autorizzate, `[S1]` e seguenti per fonti elencate, `[I]` per inferenze e `[?]` per punti irrisolti. Un'inferenza non opera come regola approvata: confermala, rimuovila o lasciala aperta con comportamento prudente. Classifica le lacune come `non stabilito dalle fonti fornite`, `esiste ma non è disponibile`, `non definito`, `sconosciuto al referente` o `non applicabile`; l'assenza nelle fonti non prova che una regola non esista.

Il profilo è utilizzabile quando l'identità è utilizzabile, le cinque aree sono state valutate, autorità essenziali e comportamenti prudenti sono definiti, i punti aperti sono classificati e non restano conflitti bloccanti.

## Documento, autorizzazioni e completamento

Per creare, ristrutturare o verificare il documento completo usa [il template dei Fondamenti](references/marketing-foundations-template.md). Mostra bozza leggibile, modifiche, decisioni aperte, limiti, responsabile, destinazione e versioni referenziate. Prepara il risultato verificabile prima di chiedere le sole decisioni ancora mancanti.

Approvazione del contenuto, salvataggio e installazione sono azioni distinte; possono essere autorizzate insieme. Un'autorizzazione precedente resta valida per la stessa azione, lo stesso documento e la stessa destinazione; se cambia uno di questi elementi o il perimetro, chiedi soltanto la nuova autorizzazione necessaria. Rispetta il mandato già espresso e non richiedere nuovamente permessi validi per il perimetro corrente. Senza approvazione del contenuto mantieni `bozza`; senza autorizzazione al salvataggio non scrivere nel percorso canonico. Quando entrambe ci sono, salva `v1`, stato `approvato` e data corrente. Per modifiche sostanziali incrementa la versione intera e conserva la cronologia; per refusi conserva la versione. Se è approvato soltanto il contenuto, indica `contenuto approvato in chat; artefatto non creato`, senza assegnare una versione canonica. Se non puoi scrivere, restituisci il documento completo con destinazione prevista.

Prima di scrivere, distingui una prova della skill (`test`, `simulazione`, `eval`) da un test strategico o operativo. In una prova della skill, scrivi soltanto in una destinazione temporanea non canonica esplicitamente richiesta per la prova: approvazioni nel copione e isolamento tecnico del workspace non abilitano destinazioni aziendali, ufficiali o previste dal workflow.

Per l'installazione richiesta nelle istruzioni dell'agente leggi [la guida pertinente](references/installation.md), prepara il diff concreto e applicalo se il mandato comprende quell'host. L'approvazione del solo contenuto non autorizza a modificare `AGENTS.md`, `CLAUDE.md` o equivalenti. Verifica ciò che hai salvato e distingui configurazione su disco da caricamento osservato nella sessione.

Nei lavori aziendali sostanziali, indica con una breve nota operativa entità e versioni effettivamente lette; se il contesto necessario non è utilizzabile, mostra invece il limite concreto. Concludi con il risultato, i punti aperti e lo stato effettivo di contenuto, salvataggio e installazione, completando tutto il mandato autorizzato. Il profilo non concede permessi per campagne, pubblicazione o spesa.
