# Direzione da un brief aziendale o da una conferma in chat

20 novembre 2026. Sono state eseguite le due varianti del [caso Faro, richiesta 4](../../define-marketing-challenge/regressions/brief-aziendale-equivalente.md) sulla sorgente italiana `choose-marketing-direction` 0.2.9. Due sessioni Codex CLI separate, ciascuna su due turni con un proprio workspace temporaneo. Entrambe hanno ricevuto la skill e i dati del caso, senza i criteri dell'esaminatore.

| Origine del brief | Primo turno | Dopo l'approvazione di Marta |
| --- | --- | --- |
| Scheda `faro.md` priva di versione | L'agente usa la sfida della scheda e presenta due strade, una legata alla scelta del corso e l'altra al momento del riacquisto. La cartella di destinazione è ancora vuota. | Crea soltanto `prova/direzione-faro.md`, approvata v1. La sezione Fonti identifica `faro.md`, segnala che la versione non è indicata e distingue la successiva conferma della direzione in chat. |
| Formulazione e vincoli confermati dalla titolare in chat | L'agente confronta guida alla scelta, dimostrazione dell'utilità e possibile revisione dell'offerta. La cartella di destinazione è ancora vuota. | Crea soltanto `prova/direzione-faro.md`, approvata v1. Il documento indica Marta, il perimetro aziendale, le condizioni commerciali e la provenienza dei dati CRM riferiti in chat. |

In entrambe le varianti il secondo turno conferma la direzione di approfondire come gli studi decidono sul riacquisto e autorizza solo il salvataggio. Ho riletto i documenti prodotti. Il webinar resta un'opzione e il test proposto attende l'autorizzazione ai contatti. Le copie temporanee riportano i riferimenti nel testo. Nessuna cita un inesistente `challenge.md`; il file della prima variante coincide ancora con la scheda iniziale e nel workspace della seconda variante non è stata creata una scheda aziendale. Le prove riguardano la sorgente in un ambiente locale con dati sintetici.
