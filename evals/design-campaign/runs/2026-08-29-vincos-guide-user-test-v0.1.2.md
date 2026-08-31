# Test dell'utente: `design-campaign` v0.1.2 sulla guida Da Chat a Work

## Esito

- Data: 2026-08-29
- Modalità: standalone, conversazione multi-turn
- Thread: `01a04cc6-ee34-7033-8761-6a81e559db59`
- Giudizio dell'utente: impianto riuscito; dettaglio accettabile ma risposta percepita come prolissa
- Hard fail osservati: nessuno sull'architettura della campagna
- Problemi di esperienza: ridondanza tra turni, gate troppo esteso, tentativo di salvataggio canonico dopo la dichiarazione che si trattava di un test

## Che cosa ha funzionato

- La skill è stata selezionata correttamente da una richiesta naturale.
- La prima risposta ha prodotto valore prima delle domande e ha chiesto pubblico, obiettivo e percorso dopo il download.
- Le risposte dell'utente hanno trasformato correttamente il lead magnet in un ponte diretto verso il corso, senza inventare nurturing.
- Sono stati separati download, CTA, iscrizione, attribuzione e disponibilità dell'offerta.
- Claim, consenso, HubSpot e blocchi operativi sono rimasti visibili.

## Che cosa ha aumentato il rework

1. La prima risposta era entro il limite della v0.1.2, ma vicina a una mini-spec; per un caso semplice bastavano una tesi, una sola architettura compatta e tre domande.
2. Dopo ogni risposta dell'utente il piano è stato quasi interamente riscritto invece di mostrare solo decisioni acquisite e parti cambiate.
3. Prima del gate sono state presentate più sintesi sovrapposte di pubblico, obiettivo, percorso e misurazione.
4. Dopo l'approvazione è stata riversata in chat una Campaign Spec molto estesa, con la stessa decisione ripetuta in contratto, base strategica, architettura, canali, asset, conversione, rischi e handoff.
5. Quando l'utente ha precisato che era soltanto un test, la skill ha comunque tentato il percorso canonico. Il sistema ha impedito la scrittura, ma il comportamento corretto era non tentarla.
6. La base dichiarata includeva il blueprint locale del Campaign Core: utile al metodo, ma non una fonte di business della campagna.

## Correzioni derivate

- prima risposta: mira a 250-350 parole nei casi semplici e massimo 500;
- una sola rappresentazione dell'architettura, senza duplicazione immediata in prosa;
- turni successivi per delta, senza riesporre il piano completo;
- revisione manageriale come rappresentazione approvabile, seguita da una sola domanda che distingue contenuto e salvataggio;
- template inteso come libreria modulare di campi, con sezioni opzionali solo quando aggiungono decisioni;
- blueprint, eval e documentazione del framework esclusi dalle fonti della campagna;
- test, simulazioni ed eval sempre fuori dai percorsi canonici.

## Limiti

È un test svolto dal proprietario del progetto, non un pilot con marketer esterni. Non misura minuti di revisione né confronto controllato con un agente generalista. La v0.1.3 derivata da questo test richiede validazione strutturale e retest comportamentale prima di sostituire la copia attiva v0.1.2.
