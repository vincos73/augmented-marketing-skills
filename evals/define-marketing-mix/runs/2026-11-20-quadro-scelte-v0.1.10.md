# Quadro · prova a due turni di `define-marketing-mix` 0.1.10

20 novembre 2026. Un agente con contesto nuovo ha ricevuto il sorgente italiano della skill, l'accesso ai suoi riferimenti e le [due richieste Quadro](../fixtures/quadro-scelte/forward-test.md) in successione. La seconda è stata consegnata solo dopo la prima risposta. I [criteri di verifica](../fixtures/quadro-scelte/expected-run.md) erano riservati al valutatore. Esecuzione sintetica in chat, senza operazioni sui documenti o le campagne del caso.

## Prima risposta

> Puoi passare oggi alle vendite dirette il **prezzo di rinnovo di 99 euro l’anno**, l’accesso dal portale clienti e l’invito alla prova guidata prevista dal contratto. La scheda può invitare lo studio a verificare sul proprio caso se l’aggiornamento fa risparmiare tempo. Il risultato resta un’ipotesi.
>
> **Per la scheda rivenditori lascia aperte le condizioni economiche.** Il 12% è la proposta del responsabile partnership. Finance decide venerdì. I 99 euro sono autorizzati per la vendita diretta.
>
> ### Quadro · Marketing mix v3 per il rinnovo annuale
>
> | P | Scelta | Stato | Base e uso |
> |---|---|---|---|
> | Product | Sessione guidata con prova pratica sul caso dello studio | Vincolo approvato | Il contratto prevede la sessione. La direzione ha confermato la prova pratica per favorire l’adozione tra i piccoli studi tecnici già clienti. |
> | Price | Rinnovo diretto a 99 euro l’anno | Scelta approvata | Finance ha approvato oggi il listino per la vendita diretta e il suo uso nella relativa scheda. Sostituisce gli 89 euro del v2 per questo rinnovo diretto. |
> | Price | Sconto rivenditori | Decisione esterna | Il responsabile partnership propone il 12%. La vecchia nota rimandava la decisione a Finance, che si riunisce venerdì. |
> | Place | Accesso alla prova dal portale clienti | Scelta approvata | Hai confermato il percorso già previsto nel v2. La scheda può indirizzare lo studio al portale. |
> | Promotion | Scheda per le vendite dirette | Scelta approvata | Hai confermato la scheda. Può riportare il listino diretto e invitare lo studio a confrontare il tempo richiesto per la stessa attività con e senza l’aggiornamento. |
>
> La v3 aggiorna il v2 sulla base delle decisioni che hai riportato qui. Hai approvato la sintesi nel perimetro indicato. **Stato del mix** — contenuto approvato in chat; artefatto non creato.

## Seconda risposta

> Nel **mix v4** cambia la voce **Price per i rivenditori**. Il 12% proposto nel v3 è superato. Finance ha approvato il **7% sui rinnovi di almeno dieci licenze acquistate tramite un rivenditore**. Per questi rinnovi lo sconto passa da *decisione esterna* a *scelta approvata*. In **Promotion** cambia l’indicazione per la scheda riservata ai rivenditori.
>
> | Scheda | Indicazione utilizzabile dalle vendite |
> |---|---|
> | Vendite dirette | «Il rinnovo costa 99 euro l’anno.» La scheda può continuare a invitare lo studio alla prova guidata dal portale clienti. |
> | Riservata ai rivenditori | «Per i rinnovi di almeno dieci licenze acquistate tramite un rivenditore è previsto uno sconto del 7%.» Per i rinnovi sotto soglia, Finance non ha indicato una condizione economica da riportare. |
>
> I 99 euro si riferiscono al listino diretto. La conferma di Finance autorizza la percentuale nella scheda riservata, senza indicare un prezzo finale per il canale rivenditori. L’aggiornamento del mix resta in chat.

## Valutazione

| Criterio | Esito | Evidenza |
| --- | --- | --- |
| Fonti e mix precedente | Superato | La direttrice può passare il listino diretto alle vendite sulla base dell'approvazione Finance riferita in chat. Gli 89 euro rimangono attribuiti all'anno precedente. |
| Indipendenza delle scelte | Superato | Nel primo turno la stessa P conserva due righe con 99 euro approvati e sconto partner affidato a Finance. L'approvazione della sintesi non rende disponibile il 12%. |
| Aggiornamento circoscritto | Superato | Nel secondo turno il 7% sostituisce la proposta del 12% per i rinnovi da dieci licenze tramite rivenditore. Resta utilizzabile nella scheda riservata. Il prezzo diretto mantiene la sua base e il suo impiego. |
| Continuità e isolamento | Rilievo sulla versione | Le risposte distinguono il vincolo contrattuale, il listino, l'esperimento e la decisione sullo sconto. L'agente ha chiamato i riepiloghi v3 e v4. L'ultima versione di file riferita dalla direttrice era v2 e il lavoro si è svolto interamente in chat. |

Gli stati commerciali e i relativi usi sono corretti. La successiva revisione ha precisato nelle istruzioni e nei criteri della prova che l'agente attribuisce un nuovo numero di versione al file solo in seguito a un salvataggio verificato. Le risposte sopra restano quelle del primo giro.

## Ripetizione sulla sorgente finale

Il caso è stato ripetuto con un altro agente in contesto nuovo, fornendo le stesse due richieste una alla volta. L'agente ha ricevuto solo il testo del turno corrente, il sorgente della skill e l'accesso ai suoi riferimenti. SHA-256 del `SKILL.md` provato: `c359bd129ee53e30144c8b9b858dc3ff26b9c7ee18ec1cd87695aa56c9b86412`.

### Prima risposta della ripetizione

> Oggi puoi passare a chi prepara la **scheda per le vendite dirette** il prezzo di **99 euro per il rinnovo annuale**, la prova guidata prevista dal contratto e l’accesso dal portale clienti. L’invito per i piccoli studi tecnici già clienti è concreto: «Prova l’aggiornamento su una tua pratica e verifica se ti fa risparmiare tempo».
>
> **Mix aggiornato per il rinnovo Quadro**
>
> | P | Scelta | Stato | Base e uso per le schede |
> |---|---|---|---|
> | Product | Sessione guidata con prova pratica | Vincolo approvato | [C] È prevista dal contratto. La scheda può invitare lo studio a provarla su un proprio caso. |
> | Price | Listino annuale diretto di 99 euro | Scelta approvata | [C] Finance ha approvato oggi il prezzo e il suo uso nella scheda diretta. Sostituisce gli 89 euro del mix precedente per questo rinnovo diretto. |
> | Price | Sconto ai rivenditori | Decisione esterna | [?] Il 12% è la proposta del responsabile partnership. Finance decide venerdì. Le condizioni per i rivenditori restano aperte. |
> | Place | Accesso alla prova dal portale clienti | Scelta approvata | [C] Hai confermato il percorso. La scheda diretta può indicare dove accedere. |
> | Promotion | Scheda a supporto delle vendite dirette | Scelta approvata | [C] Hai confermato la scheda e il suo scopo. Presenta il risparmio di tempo come domanda a cui rispondere con la prova. |
>
> Per chi lavora sulle **schede rivenditori**, l’indicazione interna è di lasciare aperta la sezione economica fino alla decisione di Finance. L’autorizzazione a riportare i 99 euro riguarda il canale diretto.
>
> Il risparmio di tempo resta un’**ipotesi da verificare**. [I] Durante la sessione lo studio può confrontare il tempo richiesto dalla stessa operazione con il metodo abituale e con l’aggiornamento.
>
> [S1] La base è il tuo riepilogo in chat della sfida, della direzione approvata e del mix v2 dell’anno scorso, insieme alle conferme sul rinnovo. **Stato della sintesi di marketing:** `contenuto approvato in chat; artefatto non creato`.

### Seconda risposta della ripetizione

> Cambia **la voce Price relativa allo sconto rivenditori**. La decisione che attendeva Finance ora è una **scelta approvata**. La proposta del 12% è superata.
>
> | Scheda | Che cosa possono indicare le vendite |
> |---|---|
> | Vendite dirette | **99 euro per il rinnovo annuale**, secondo il listino diretto già approvato. |
> | Scheda riservata ai rivenditori | **Sconto del 7% per i rinnovi di almeno dieci licenze acquistate tramite un rivenditore.** Sotto le dieci licenze il 7% non si applica. |
>
> Per **Promotion**, la novità è il permesso di riportare il 7% nella scheda riservata ai rivenditori, insieme alla soglia e alla condizione di acquisto. Finance ha confermato i 99 euro per il solo canale diretto, quindi quel prezzo non va usato come base per calcolare un importo netto rivenditore.
>
> La sintesi recepisce la conferma di Finance che hai riferito oggi in chat e aggiorna la voce rimasta aperta nel precedente riepilogo del mix v2. `Contenuto approvato in chat; artefatto non creato`.

### Esito della ripetizione

Superati i quattro criteri Quadro. In entrambi i turni v2 è l'unica versione di file citata ed è attribuita al riepilogo della direttrice. La prima risposta assegna due stati distinti alle scelte Price, lascia in sospeso lo sconto del 12% e rende utilizzabile il listino diretto di 99 euro. La seconda aggiorna la singola decisione di Finance, distingue le schede dei due canali e conserva rinnovo, soglia minima di dieci licenze e acquisto tramite rivenditore. Le approvazioni riguardano il contenuto in chat e l'agente non ha eseguito operazioni esterne.
