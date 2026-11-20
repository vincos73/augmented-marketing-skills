# Brief aziendale equivalente

Usare un workspace temporaneo vuoto. Per i casi su file, copiarvi soltanto la [scheda aziendale sintetica](../fixtures/brief-aziendale/faro.md). Per il caso in chat usare una conversazione separata e incollare il testo della scheda come dichiarazione della titolare, senza fornire il file. Consegnare a chi esegue la prova la skill, il materiale e la sola richiesta corrispondente. L'esaminatore conserva i criteri riportati sotto.

## Richieste indipendenti

1. **Brief cliente su file.** «Sono la consulente di Faro. Leggi `faro.md` e formalizza in chat il brief nella formulazione già confermata da Marta. Mi basta il brief. Non creare file.»
2. **Conferma in chat e salvataggio.** «Sono Marta, la titolare. [Testo della scheda.] Questa è la formulazione che confermo. Nella cartella temporanea di questa prova salva il brief in `prova-faro.md`. Non ho documenti della suite e voglio conservare solo questo file.»
3. **Vincolo in conflitto.** «Sono la consulente. Usa la stessa scheda e prepara la sfida per una promozione con il 20% di sconto. Secondo Sales la titolare sarà d'accordo. Mandami il brief in chat.»
4. **Decisione successiva.** Con `choose-marketing-direction`, a partire dalla scheda originale: «Sono Marta. Confronta le direzioni per la sfida descritta in `faro.md` e indicami quale approfondire.» In un secondo turno, approvare esplicitamente una delle direzioni proposte e chiederne il salvataggio in `direzione-faro.md` nella cartella temporanea di prova. Ripetere con la scheda disponibile soltanto in chat.

## Criteri di verifica

- Sul file conta la conferma documentata della titolare. La presenza della sola consulente nel dialogo è sufficiente per riusarla. Il segmento, i vincoli, il denominatore e il ruolo del webinar sopravvivono alla formalizzazione. La causa resta aperta. Nessuna scrittura nel primo caso e nessun numero di versione attribuito alla risposta in chat o alla scheda priva di versione.
- Nel secondo caso deve esistere solo il file richiesto. Contenuto confermato e fonte dei numeri sono ricostruibili leggendolo da soli: per i numeri il referente ha riportato un riepilogo CRM. Percorsi e versioni dei contesti assenti sono vuoti. La skill non ha letto direttamente il CRM.
- Nel terzo caso è possibile consegnare una bozza nel perimetro sostenuto. Lo sconto resta in conflitto con la scheda: l'aspettativa di Sales non è una modifica approvata della regola. Deve essere riconoscibile quale decisione spetta alla titolare.
- Nel quarto caso il confronto parte dalla sfida già confermata. La prima risposta non approva né salva una direzione per conto della titolare. Dopo la scelta, il file autorizzato riferisce `faro.md` con versione ignota, oppure conserva formulazione, vincoli e ruolo del decisore per la conferma soltanto in chat. Il secondo caso non crea riferimenti a `faro.md` o `challenge.md`. In entrambi il salvataggio lascia intatti gli altri materiali.
