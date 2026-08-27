# Protocollo di valutazione

## Obiettivo

Misurare il cambiamento osservabile prodotto da ciascuna skill rispetto a una risposta baseline senza skill, a parità di fixture e richiesta. Il confronto valuta comportamento e utilità, non la somiglianza con una prosa attesa.

## Generazione

Per ogni skill si generano due risposte sullo stesso prompt:

1. baseline: l'agente non riceve la `SKILL.md` né i riferimenti della skill;
2. skill: l'agente riceve la `SKILL.md` pertinente e i riferimenti direttamente richiamati necessari al flusso.

Entrambe le risposte sono istruite a non scrivere file canonici, non installare istruzioni, non pubblicare claim e non usare informazioni esterne alla fixture. La risposta con skill deve applicare il workflow in chat e fermarsi prima di qualunque approvazione o installazione non autorizzata.

## Valutazione cieca

Il valutatore è istruito esplicitamente come **marketer strategico senior con almeno 15 anni di esperienza**. Riceve soltanto:

- la fixture e la richiesta;
- due risposte anonime chiamate A e B;
- la rubrica qui sotto.

Non riceve quale risposta sia baseline o con skill e non deve tentare di inferirlo. Si eseguono due passaggi indipendenti con ordine invertito:

- Passaggio 1: A = baseline, B = skill.
- Passaggio 2: A = skill, B = baseline.

Il secondo passaggio è eseguito da un nuovo agente valutatore con lo stesso ruolo e la stessa istruzione, per evitare che il primo giudizio diventi contesto implicito. Le identità reali dei candidati vengono ricostruite soltanto nell'analisi aggregata.

## Rubrica

Ogni dimensione riceve un punteggio intero da 1 a 5 per ciascuna risposta:

1. **Qualità strategica**: per l'identità, qualità della diagnosi di entità, offerta, pubblico, alternative e confini; per i Fondamenti, qualità delle regole stabili e delle conseguenze. Non premiare strategia inventata fuori perimetro.
2. **Disciplina delle evidenze**: provenienza visibile, distinzione tra fatto, inferenza, conflitto e lacuna, gestione dei claim e delle fonti non attendibili.
3. **Utilità decisionale**: capacità di far avanzare il responsabile con una sintesi utile, domande ad alta conseguenza e prossimi passi proporzionati.
4. **Rispetto di perimetro e autorità**: separazione tra bozza, approvazione, salvataggio, installazione, pubblicazione ed esecuzione; assenza di strategia o campagna inventata.
5. **Chiarezza**: comprensibilità per un responsabile, linguaggio naturale, struttura leggibile, assenza di gergo non necessario.
6. **Proporzione**: rapporto tra dettaglio e richiesta, priorità ai rischi materialmente rilevanti, assenza di questionari o inventari superflui.

Per ciascuna risposta il valutatore registra anche:

- hard fail: numero di violazioni critiche, con descrizione;
- soft fail: numero di carenze non critiche, con descrizione;
- criticità complessiva: `nessuna`, `bassa`, `media` o `alta`;
- osservazioni e correzioni necessarie.

## Misure

La lunghezza è il numero di parole dell'output completo, calcolato con `wc -w` sul file conservato. Per ogni dimensione, il gap di un passaggio è `punteggio risposta con skill - punteggio baseline`. Il gap riportato è la media dei due passaggi controbilanciati. Il gap complessivo è la media dei sei gap dimensionali.

La severità non viene ridotta a un punteggio promozionale: si riportano separatamente hard fail, soft fail e criticità. Un singolo hard fail di privacy, provenienza, autorità o pubblicazione resta visibile anche se la media è positiva.

## Limiti

È un eval sintetico con due fixture e due giudizi indipendenti. Non è un pilot con marketer reali, non misura adozione, tempo di lavoro reale, correzioni in uso, qualità longitudinale o risultati di business. Non produce claim di marketing sulla Suite o sulle skill.
