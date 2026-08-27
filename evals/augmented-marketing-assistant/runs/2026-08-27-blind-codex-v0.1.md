# Test cieco di Augmented Marketing Assistant v0.1 in Codex

**Data:** 2026-08-27

**Definizione verificata:** `agents/augmented-marketing-assistant.md`, prototipo v0.1

**Ambiente:** sessione Codex separata, in sola lettura

**Input consentito:** definizione canonica dell'Assistant e richieste sintetiche prive degli esiti attesi

**Input escluso:** file di eval, conversazione di progettazione e rubriche di valutazione

**Limite:** la sessione separata non costituiva un worktree Git isolato e non coinvolgeva marketer reali

## Prima esecuzione

| Scenario | Comportamento osservato | Esito |
| --- | --- | --- |
| Organizzazione non conosciuta | Ha proposto la costruzione dell'identità e il risultato persistente corretto | PASS |
| Regole stabili da ripetere | Ha distinto le Marketing Foundations dall'identità già disponibile | PASS |
| Community proposta come soluzione | Ha ricondotto la tattica alla formulazione della sfida | PASS |
| Brief approvato | Ha proposto il confronto tra direzioni senza scegliere al posto dell'utente | PASS |
| Direzione approvata | Ha coordinato offerta, prezzo, accesso e promozione | PASS |
| Carosello già definito | Non ha imposto Strategy Core, ma non ha proposto di verificare un builder esterno | SOFT FAIL |
| Richiesta completamente generica | Ha posto una sola domanda, ma ha distinto soltanto regole stabili e decisione specifica | SOFT FAIL |
| Invocazione diretta del marketing mix | Ha rispettato la scelta e richiesto l'accessibilità della direzione approvata | PASS |

È inoltre emersa una questione di esperienza: i nomi tecnici delle skill erano mostrati nel corpo della risposta senza una convenzione che privilegiasse prima il linguaggio di lavoro.

## Correzioni applicate

La definizione canonica è stata aggiornata in tre punti circoscritti:

1. spiegare prima il passaggio in linguaggio naturale e mostrare poi il nome tecnico della skill tra parentesi;
2. usare, per una richiesta completamente generica, una sola domanda che distingua contesto dell'organizzazione, regole stabili, decisione specifica e attività esecutiva;
3. proporre una skill esterna soltanto quando la sua presenza è osservabile, senza dedurne la disponibilità dalla richiesta dell'utente.

## Regression test

Sono state usate richieste nuove, senza mostrare gli esiti attesi.

| Scenario | Comportamento osservato | Esito |
| --- | --- | --- |
| Organizzazione non conosciuta | Ha spiegato identità e risultato, indicando `setup-business-context` tra parentesi | PASS |
| Marketing genericamente da sistemare | Ha posto una sola domanda che distingue i quattro tipi di bisogno | PASS |
| Carosello con input approvati | Non ha riaperto la strategia e ha indicato il builder pertinente tra parentesi, mantenendo approvazione e autorizzazione distinte | PASS |

## Verdetto

Il test non presenta hard fail residui negli scenari eseguiti. Il prototipo può passare a un micro-pilot con marketer reali.

Restano non dimostrati:

- comprensibilità e utilità percepita presso il pubblico target;
- handoff effettivo alle skill durante un lavoro completo;
- continuità dopo la produzione e approvazione di un artefatto;
- comportamento su agenti diversi da Codex;
- packaging e installazione dell'esperienza completa.
