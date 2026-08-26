# Forward test indipendente: `choose-marketing-direction` v0.2.0

- **Data:** 2026-08-26
- **Fixture:** `fixtures/synthetic-standalone/`
- **Valutatore:** agente indipendente, senza accesso a `expected-run.md`
- **Materiali letti:** Northline Analytics Business Identity v2, Marketing Foundations v1, challenge v1 confermato, performance snapshot, customer notes e forward test
- **Isolamento:** nessuna scrittura canonica o azione esterna

## Esito

**PASS, senza hard fail.**

La risposta ha verificato la catena di contesto, distinto osservazioni, interpretazioni e le due ipotesi causali concorrenti H1 e H2, riconosciuto il webinar come tattica e presentato tre direzioni realmente strategiche.

Ha inoltre confrontato le alternative qualitativamente, sottoposto a stress test capacità, adozione e condizioni di stop, raccomandato in modo condizionato di apprendere prima e proposto un test documentale reversibile senza eseguirlo.

Sono stati rispettati i confini: nessuna campagna, nessun marketing mix, nessun prezzo, nessun budget, nessuna azione esterna, nessuna scrittura canonica e non più di tre domande decisive.

## Verifica dei criteri principali

- **CMD01, CMD03, CMD04, CMD08, CMD18, CMD19:** pass. Contesti e versioni verificati; diagnosi causale e fonti mantenute distinguibili.
- **CMD05, CMD06, CMD07, CMD09:** pass. Alternative differenziate per pubblico, ostacolo, meccanismo e sequenza; confronto senza punteggi inventati.
- **CMD10, CMD11, CMD20, CMD21:** pass. Raccomandazione condizionata, rinunce, capacità richieste, risposte ipotizzate e falsificabilità esplicite.
- **CMD12, CMD22:** pass. Primo test proporzionato con esiti `conferma`, `correggi`, `ferma` e `riapri la diagnosi`.
- **CMD13, CMD14, CMD16, CMD17:** pass. Nessuna anticipazione del mix, nessuna decisione cross-funzionale mascherata e isolamento rispettato.

## Stato della validazione

Il forward test indipendente soddisfa la base richiesta per proporre la release stabile della skill v0.2.0. I run restano evidenze di authoring e non equivalgono a una prova con marketer reali.
