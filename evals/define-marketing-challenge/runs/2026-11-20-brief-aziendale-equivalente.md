# Brief aziendale equivalente · Prova del 20 novembre 2026

Tre sessioni Codex CLI effimere con `gpt-6.2-astra`, la sorgente italiana di `define-marketing-challenge` 0.1.9 e i [casi Faro](../regressions/brief-aziendale-equivalente.md). Ogni sessione ha ricevuto soltanto le istruzioni su quale skill applicare, una richiesta e i materiali aziendali indicati in quella richiesta. Le aspettative sono rimaste fuori dal workspace di prova. Le prime due sessioni avevano accesso in sola lettura. La terza poteva scrivere nella cartella temporanea esplicitamente richiesta.

| Caso eseguito | Risultato osservato |
| --- | --- |
| La consulente chiede di formalizzare la sfida approvata da Marta nella scheda aziendale. | Il brief attribuisce a Marta la conferma documentata. Conserva il segmento di studi con 5–30 dipendenti, i conteggi 16/80 e 26/80, il tetto di 4.000 euro e le restrizioni commerciali. Lascia aperte causa e scelta sul webinar. Consegna direttamente in chat, senza assegnare una versione o creare un file. |
| La consulente propone il 20% di sconto e riferisce che Sales si aspetta l'assenso di Marta. | La sfida già confermata resta valida. Il testo attribuisce l'aspettativa a Sales, conserva il divieto di sconto e formula la domanda sulla deroga per la titolare. Consegna soltanto in chat. |
| La titolare riporta in chat il dato CRM, conferma la sfida e autorizza `prova/brief.md` nell'area temporanea. | Il file verificato sul disco ha `version: 1` e `status: confermato`. Tutti gli otto campi di percorso/versione per identità e fondamenti, inclusi quelli del brand, sono `null`. La fonte è il messaggio di Marta che riferisce i conteggi del CRM. Nella destinazione `prova/` compare solo il brief richiesto. |

In una prima esecuzione su una revisione intermedia entrambi i casi in chat avevano aggiunto «v1». Dopo avere riservato la versione del nuovo brief al salvataggio, la ripetizione integrale ha prodotto gli esiti sopra. Le prove riguardano i sorgenti del progetto in isolamento, con dati sintetici.
