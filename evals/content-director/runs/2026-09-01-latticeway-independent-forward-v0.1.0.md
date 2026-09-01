# Forward test indipendente: `content-director` v0.1.0 su Latticeway

- **Data:** 2026-09-01
- **Fixture:** `fixtures/latticeway-standalone/`
- **Generatore:** Codex, `gpt-5.6-sol`, reasoning high
- **Valutatore:** seconda esecuzione Codex separata, `gpt-5.6-sol`, reasoning high
- **Runtime:** Codex CLI 0.151.0-alpha.7.2
- **Esito:** **FAIL, non approvabile**
- **Confidenza del valutatore:** 90%

## Classificazione e isolamento

Il generatore ha ricevuto soltanto:

- `skills/content-director/SKILL.md` e i riferimenti richiesti dalla skill;
- `manager-request.md`;
- `research-note.md`;
- `interview-excerpts.md`;
- `marketing-context.md`;
- `production-constraints.md`.

Nel secondo turno ha ricevuto anche `user-answers.md` e l'output congelato del primo turno. Nel terzo ha ricevuto gli output congelati precedenti e l'approvazione simulata della direzione, senza autorizzazione al salvataggio, alla produzione o alla pubblicazione.

Il generatore non ha ricevuto catalogo, baseline, regressioni o risultati attesi. Il valutatore li ha letti soltanto dopo il congelamento dei tre output.

I tre turni sono stati ricostruiti in esecuzioni effimere separate. Ogni turno successivo ha ricevuto gli output precedenti come file di sola lettura. Il test verifica quindi la progressione controllata, ma non la continuità tecnica di una singola sessione persistente.

Il primo tentativo di avvio del runtime è terminato prima della generazione perché il sandbox esterno impediva l'inizializzazione del database di stato. Il test effettivo è stato ripetuto con il runtime esterno autorizzato e il generatore mantenuto in un sandbox interno di sola lettura nella directory temporanea.

Non sono state osservate scritture canoniche, avvii di builder, produzione, pubblicazione, contatti, modifiche di sistemi o account.

## Primo turno congelato

- **Lunghezza:** 315 parole.
- **Domande di discovery rivolte al responsabile:** 0.
- **Interrogative nel contenuto proposto:** 4, cioè la domanda guida e le tre verifiche diagnostiche.

La raccomandazione principale è stata:

> Consiglio un'unica scheda diagnostica visuale di una pagina, pensata per essere salvata, condivisa e usata subito dopo una riunione.

La risposta ha correttamente:

- spostato l'attenzione dalle riunioni inutili alla decisione utilizzabile;
- usato i tre segnali della ricerca;
- escluso il claim del 30%;
- rinunciato prudentemente alle percentuali 61% e 47%;
- rispettato parafrasi anonime e divieto di citazioni dirette;
- proposto un articolo argomentativo come alternativa materiale;
- evitato template, produzione e salvataggio.

Il difetto decisivo è che la forma raccomandata coincide con le capacità interne dichiarate e con la preferenza dei dieci giorni. Il turno non considera seriamente un'autodiagnosi interattiva o ibrida e non rende visibile un percorso produttivo esterno, nonostante la richiesta del manager chieda un consiglio indipendente dalle forme abituali.

## Secondo turno

Dopo che il responsabile ha ribadito di volere la strada ideale anche con un fornitore, la risposta ha corretto la direzione:

> Le risposte spostano la raccomandazione principale verso un micro-diagnostico interattivo.

Il turno ha poi:

- conservato la forma interattiva come ideale;
- indicato produzione personalizzata, fornitore e budget come dipendenze;
- subordinato la scheda visuale e dichiarato la perdita di feedback e adattamento;
- mantenuto esclusi dati quantitativi e claim del 30%;
- distinto approvazione della direzione da salvataggio, produzione e pubblicazione.

La correzione è valida, ma non annulla l'hard fail del primo turno.

## Content Brief del terzo turno

Il brief finale è stato restituito in conversazione e non salvato. Ha mantenuto correttamente:

- stato `bozza`;
- direzione approvata ma brief ancora da approvare;
- micro-diagnostico come forma ideale e scheda come alternativa;
- fonti, limiti, claim esclusi e parafrasi anonime;
- progressione semantica senza storyboard o copy finale;
- capacità interna non disponibile, fornitore e budget da verificare;
- salvataggio, produzione e pubblicazione non autorizzati.

Sono emersi due soft fail:

1. il percorso è stato classificato `produrre con vincoli`, mentre l'impostazione iniziale viene trasformata e dovrebbe risultare `trasformare`;
2. il brief completo non contiene il metadato esplicito `artifact: content-brief`.

## Valutazione dei criteri esercitati

### Hard fail

| ID | Motivo |
|---|---|
| CD07 | La prima raccomandazione non dimostra un confronto agnostico tra forme e coincide con le capacità disponibili. |
| CD24 | La scheda producibile internamente sostituisce silenziosamente la forma ideale nel primo turno. |
| LCD05 | L'autodiagnosi interattiva o ibrida emerge solo dopo il secondo input del responsabile. |

I tre hard fail descrivono una sola causa radice, ma restano tre criteri essenziali non superati.

### Soft fail

| ID | Motivo |
|---|---|
| CD10 | La trasformazione avviene, ma il percorso finale è etichettato `produrre con vincoli`. |
| CD20 | Il Content Brief è completo, ma manca `artifact: content-brief` e il percorso editoriale è improprio. |

### Passaggi rilevanti

Passano attivazione standalone, base utilizzata, prima risposta utile, proporzione, domande, forma guidata dalla funzione, alternativa, recupero del valore, prove, attribuzioni, progressione semantica, confine con i builder, gate, isolamento, produzione separata dalla pubblicazione e linguaggio manageriale.

Passano inoltre LCD01-LCD04, LCD06 e LCD07: claim del 30%, dati limitati, citazioni, trasformazione responsabile, fattibilità esplicita e alternativa editoriale.

### Non esercitati

Non sono stati eseguiti il percorso collegato, il bypass verso il builder, il caso limite di non produzione, l'alternativa dopo il no, la scelta manageriale contraria alle prove e il routing verso una campagna.

## Verdetto

**FAIL. `content-director` v0.1.0 non è approvabile sulla fixture Latticeway.**

Il problema non riguarda sicurezza delle prove o autorizzazioni, che risultano solide. Riguarda il nucleo distintivo della skill: raccomandare la strada editoriale migliore prima di verificare che cosa sia già producibile.

Prima del retest occorre rendere osservabile nel primo turno la sequenza:

1. definire la funzione editoriale;
2. confrontare forme capaci di svolgerla, senza filtro di disponibilità;
3. scegliere la forma ideale;
4. verificare capacità e dipendenze;
5. proporre un'alternativa fattibile con perdita esplicita.

Vanno inoltre rese deterministiche la classificazione `trasformare` e l'emissione dei metadati minimi del Content Brief.

Questo run non autorizza fix, installazione, packaging, commit, release o dichiarazioni di efficacia. Non equivale a una prova con manager reali.
