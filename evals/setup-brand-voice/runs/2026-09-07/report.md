# Prima verifica di setup-brand-voice 0.1.0

**Esito: PASS CON RISERVA come prima versione locale.** I percorsi principali producono risultati utilizzabili sui materiali sintetici. Le prove hanno individuato errori reali, conservati nell'archivio; le correzioni sono state provate con nuovi agenti. Non è una certificazione di tutte le 16 voci del catalogo né una prova di efficacia su aziende reali.

Sono state eseguite **10 prove di generazione indipendenti, per 20 turni complessivi**: cinque prove iniziali, due sul candidato intermedio e tre sul candidato finale. Quattro prove iniziali comprendono dialoghi completi di 2–4 turni; i retest finali sono mirati. È stata creata e verificata una vera guida di prova soltanto nella destinazione temporanea autorizzata.

## Risultati osservati

I conteggi di parole usano il transcript Markdown integrale diviso per spazi. Le decisioni sono contate manualmente: domande al responsabile e scelte esplicitamente da confermare; sono escluse le domande al cliente dentro gli esempi e l'approvazione finale della formulazione completa. Le scelte collegate sono contate separatamente quando comportano due decisioni. Non sono misure del tempo richiesto a una persona reale.

| Prova | Candidato | Turni | Parole per turno | Decisioni per turno | Esito e rework |
|---|---|---:|---|---|---|
| [Ricalco, guida approvata](ricalco/turn-1.md) | Iniziale | 2 | 330, 327 | 0, 0 | FAIL formale: apostrofo normalizzato nella clausola da copiare. T2 la riproduce correttamente; nessuna reinvenzione della voce o pressione sul salvataggio. |
| [Filoporto, materiali incoerenti](filoporto/turn-1.md) | Iniziale | 4 | 366, 214, 401, 42 | 1, 1, 0, 0 | PASS con un soft fail: indicazione troppo generale sulle battute in T2, circoscritta in T3. Il dialogo arriva a una guida approvata solo in chat. |
| [Sponda, nessun testo](sponda/turn-1.md) | Iniziale | 3 | 267, 153, 314 | 1, 1, 0 | PASS: esempi sullo stesso fatto, scelta, caso nuovo e guida compatta. La correzione condizionale non diventa una falsa citazione della risposta precedente. |
| [Ardora, revisione limitata](ardora/turn-1.md) | Iniziale | 3 | 333, 257, 246 | 3, 0, 0 | FAIL fattuale: nella seconda alternativa si presume l'invio di nuove misure. T2/T3 sono fedeli e conservano il perimetro; non cancellano l'errore iniziale. |
| [Ricalco, guida generica](partial/turn-1.md) | Iniziale | 1 | 331 | 1 | PASS: conserva l'orientamento e propone applicazioni, senza importare le decisioni della guida 2.1 dell'altro scenario. |
| [Ardora, primo retest](ardora-retest-1/turn-1.md) | Intermedio | 1 | 333 | 2 | FAIL fattuale: «averci scritto» presume un canale non noto. Necessario un ulteriore chiarimento nelle istruzioni. |
| [Ricalco, salvataggio autorizzato](save/turn-1.md) | Intermedio | 2 | 355, 25 | 0, 0 | PASS: clausola letterale, attesa dell'approvazione, poi un solo file richiesto creato e riletto senza conferma duplicata. |
| [Ardora, secondo retest](ardora-retest-2/turn-1.md) | Finale | 1 | 335 | 2 | PASS sul primo turno: entrambe le alternative conservano i fatti; cortesia riferita alla richiesta ricevuta, senza inventare dettagli o canale. |
| [Filoporto, retest](filoporto-retest/turn-1.md) | Finale | 2 | 400, 199 | 2, 1 | PASS sui due turni: regole operative esplicitamente proposte; nessun divieto generale di battute dedotto dal desiderio di rispetto. |
| [Ricalco, continuità con la suite](linked/turn-1.md) | Finale | 1 | 316 | 0 | PASS: riusa Fondamenti 1.3 e guida 2.1, conserva pubblico/offerta/posizionamento e clausola letterale; non riapre onboarding o campagna. |

Totale: **7 prove PASS, una delle quali con soft fail recuperato, e 3 prove FAIL conservate**. I tre FAIL appartengono a candidati precedenti: uno riguarda copia letterale e due riguardano fatti impliciti nelle formule di cortesia. Il soft fail compare una volta. Si tratta di due famiglie di errori bloccanti, non di tre difetti indipendenti del metodo: il problema della cortesia ricompare nel primo retest. Nell'esempio Ardora iniziale il dettaglio non sostenuto compare anche nella motivazione della raccomandazione.

Nei tre run sul candidato finale non sono stati rilevati hard o soft fail nei punti verificati. Non significa che l'intero catalogo sia passato sulla stessa identica versione. I casi Sponda e guida parziale non sono stati rieseguiti dopo le precisazioni: la loro evidenza riguarda il candidato iniziale. Ricalco BV15 riguarda quello intermedio; il candidato finale ricontrolla il recepimento e la copia letterale nella prova collegata alla suite.

Le prime risposte sono tra 267 e 400 parole, tutte sotto 500. Tre superano il riferimento indicativo di 350. Le guide complete richieste nei turni successivi non vengono penalizzate come se fossero nuove risposte di onboarding. Totale delle decisioni secondo la codifica sopra: 15, nessun turno oltre tre. Non sono state individuate domande di onboarding ripetute dopo una risposta già risolutiva.

## Che cosa è stato corretto

- **Copia fedele:** la skill precisa che un testo da mantenere identico non va normalizzato neanche nella tipografia. La stringa è stata poi verificata automaticamente nella proposta e nel file BV15, oltre che nel run collegato finale.
- **Fatti impliciti:** la verifica comprende aperture cortesi e frasi di raccordo. La seconda correzione distingue esplicitamente richiesta ricevuta, canale del contatto e informazioni effettivamente inviate. Il secondo retest Ardora supera il caso che aveva fallito due volte.
- **Decisioni e proposte:** una preferenza generale non approva da sola nuovi divieti. Il retest Filoporto presenta le conseguenze operative come proposta senza escludere l'umorismo in tutta la comunicazione.

I retest sono nuovi run senza accesso agli errori o alle risposte attese. Non si è semplicemente corretto il testo delle prime risposte. Le versioni e i loro hash sono nel [protocollo](protocol.md), con copia completa dei candidati iniziale e intermedio. La versione pubblicamente non rilasciata rimane 0.1.0.

## Copertura del catalogo

| Criteri | Copertura effettiva |
|---|---|
| BV01, BV02, BV03, BV04, BV05 | Percorsi iniziali eseguiti. Errori e differenze dei retest sono riportati sopra. |
| BV11, BV13, BV14 | Dialoghi completi Filoporto, Sponda e Ricalco, con nuovi casi, correzioni e approvazione senza salvataggio. |
| BV15 | Esecuzione completa con scrittura isolata e verifica fisica. |
| BV16a | Eseguito il collegamento ai fondamenti della suite. |
| BV06, BV08, BV09, BV10, BV12 | Alcune invarianti osservate negli altri run: agenzia approvata, 40% escluso, stringa protetta, tono contestuale e perimetri. Le rispettive varianti autonome NON sono state eseguite. |
| BV07, BV16b | NON ESEGUITI: singola email con sito inaccessibile e fonte contenente istruzioni ostili. |

Quindi nove ID hanno una loro esecuzione completa, più la sola variante A di BV16. Il catalogo contiene 16 ID, non 16 test tutti eseguiti e superati. La prima versione copre progettualmente tutti i punti di partenza richiesti; le prove non esauriscono tutte le combinazioni.

## Salvataggio e pacchetto

La cartella di BV15 era vuota prima dell'esecuzione e l'artefatto risultava assente dopo il primo turno, prima dell'approvazione. Dopo il secondo turno contiene soltanto il file autorizzato. Il contenuto corrisponde al blocco di testo approvato, salvo la nuova riga esterna finale; i due riferimenti locali esistono e la clausola è identica. [Verifica JSON](save-verification.json) e [copia del risultato](save/created-reference.md).

Il controllo è limitato alla directory richiesta e al file creato; non è un audit dell'intero filesystem. Le scritture dei transcript di prova sono operazioni separate del harness, descritte nel protocollo.

Controlli della distribuzione locale: validatore della skill, metadati dell'interfaccia, collegamenti interni, sette file nel pacchetto, unica cartella radice, integrità ZIP e corrispondenza per hash tra estrazione e sorgente. Il pacchetto non include fixture, guide di aziende simulate o dipendenze esterne. Vedi [verifiche finali](verification.json).

## Limiti e uso della prima versione

La review indipendente ha esaminato testo e fonti dei casi falliti; non prova da sola la storia delle letture o l'assenza di azioni non registrate. Le modalità di registrazione e la lettura accidentale di fixture aggiuntive da parte del valutatore sono dichiarate nel [protocollo](protocol.md). Nessuno di questi limiti viene nascosto sotto la parola «blind».

Non sono state misurate riconoscibilità presso clienti reali, efficacia commerciale, tempo di revisione umano o superiorità rispetto a un buon generalista. Non sono stati provati recupero di siti reali, importazione di guide PDF complesse, altre lingue in produzione o aggiornamento di una guida approvata su disco: BV15 verifica la creazione di un nuovo riferimento. Il perimetro multilingue è verificato come conservazione delle decisioni, non come qualità linguistica completa dell'inglese.

La prima versione è disponibile per una prova guidata su un brand reale. Prima di considerarla stabile per uso esteso, sono pertinenti le varianti non eseguite, una prova di aggiornamento su file e un confronto sullo stesso brand con un generalista. Non occorre trasformare queste attività successive in prerequisiti artificiali per consegnare la versione locale richiesta.
