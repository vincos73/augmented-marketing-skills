# Protocollo ed evidenze della prova

Data: 7 settembre 2026. Skill: setup-brand-voice 0.1.0, prima versione locale non pubblicata.

## Preparazione e isolamento

Il catalogo e le quattro fixture sono stati preparati da un agente distinto, con accesso ai requisiti del lavoro e ai learning della suite, senza lettura della nuova skill o del blueprint. Il coordinatore ha scritto l'implementazione e ha successivamente letto il catalogo per valutare i risultati. Questa separazione non equivale a un benchmark esterno.

Ogni dialogo di generazione è stato avviato in un agente nuovo con `fork_turns: none`, senza ereditare la conversazione del coordinatore. I messaggi iniziali autorizzavano soltanto skill, riferimenti necessari e fonti specificate per il caso; escludevano memoria, attese, catalogo, blueprint, altri test e ricerche esterne. Nei dialoghi a più turni si è riusato lo stesso agente per conservare la continuità richiesta dal test.

Il generatore ha ricevuto il singolo input e la relativa allowlist, oppure la sola richiesta estratta dalla variante. I turni del copione sono stati inviati uno alla volta dopo la consegna del precedente. I generatori non hanno ricevuto i difetti osservati nei run precedenti o indicazioni sulle risposte attese. I retest sono nuove esecuzioni del caso originale, non riscritture assistite dell'output sbagliato.

## Registrazione dei risultati

Il protocollo aggiunge una sola eccezione infrastrutturale alla sola lettura delle prove: il harness è autorizzato a registrare il testo integrale della risposta in una cartella temporanea dedicata. Questa registrazione è esplicitamente separata dal lavoro aziendale, per il quale resta valido il divieto di salvare. Non costituisce la creazione di una guida approvata.

Le risposte sono state restituite al coordinatore e copiate, senza riscritture, nei sottopercorsi di questo run. Un controllo byte per byte ha verificato l'identità con i transcript temporanei. Il manifest conserva gli hash. I file congelati non vengono sostituiti dopo le correzioni: ogni retest usa un percorso distinto.

Eccezione di registrazione: gli agenti dei retest finali Ardora e Filoporto e della prova collegata alla suite hanno restituito il testo senza scrivere il transcript, lasciando la registrazione al coordinatore. Il coordinatore ha copiato la parte della risposta simulata dai messaggi ricevuti, senza modificarla; le dichiarazioni operative separate non fanno parte del transcript. Per questi casi l'origine è il messaggio dell'agente, non un file da lui creato. Il manifest identifica anche questa modalità: il controllo fra copia temporanea e archivio non va presentato come confronto automatico con il messaggio originale.

La prova BV15 autorizza invece una vera scrittura, limitata al singolo file temporaneo specificato in `operator-variants.json`, dopo l'approvazione del testo. Il coordinatore ha creato e verificato vuota la cartella prima della prova. La concessione al harness di registrare i turni non autorizza scritture aggiuntive della skill. Le verifiche del file di risultato sono registrate separatamente.

I conteggi usano parole separate da spazi sul transcript Markdown integrale: includono alcuni elementi di markup e non sono una misura linguistica precisa. Il confronto con i limiti della prima risposta resta conservativo. Decisioni/domande e rework sono valutati manualmente, distinguendo domande esplorative dalla richiesta finale di approvare una guida già presentata.

## Versioni effettivamente provate

| Candidato | Impronta aggregata SHA-256 | Evidenza |
|---|---|---|
| Iniziale, prima delle correzioni | `4fbde076c19b40c2aca72c9f2be3ccf57aae797b70df0feb5a43b78e5f5df768` | `initial-skill-manifest.json` e copia completa `initial-skill.zip` |
| Intermedio, dopo la prima correzione | `f08d95c6cebb848f48d6f630134eae801864c6a2392bf5bb9569e26478aec7e6` | `intermediate-skill-manifest.json` e `intermediate-skill.zip` |
| Finale, dopo il chiarimento sul canale di contatto | `b22e89eae655961aa094b48e40b233193d47b219885b6f84b31514193a29f1a6` | `final-skill-manifest.json`, sorgente e pacchetto finale |

L'impronta aggregata deriva dal JSON ordinato della mappa percorso relativo → hash del contenuto. Non è l'hash del file ZIP. Tutti i candidati dichiarano 0.1.0: sono revisioni interne della prima versione, non release pubbliche diverse. Sono stati aggiunti soltanto tre paragrafi al file principale dopo i primi run; gli altri sei file sono identici.

Il modello e il ragionamento degli agenti sono ereditati dalla sessione. Il coordinatore non ha imposto un modello diverso; l'identificatore esatto del backend non è esposto nel risultato delle chiamate di collaborazione e non viene inventato. Tempi reali di revisione da parte di un responsabile marketing: non misurati.

## Secondo parere

Un agente che aveva svolto la ricerca su X ha esaminato i sei turni Ricalco/Filoporto già congelati e, in una richiesta distinta, il primo turno Ardora. Non ha letto skill o blueprint e non ha partecipato alla loro scrittura o a quella delle attese. Il suo precedente contesto di ricerca resta un limite alla cecità completa del valutatore.

Il parere ha confermato la proposta generale di escludere le battute in Filoporto T2, poi circoscritta correttamente in T3; ha individuato la normalizzazione dell'apostrofo nella clausola Ricalco T1, corretta in T2; ha rilevato che Ardora T1 ringrazia per nuove misure non dichiarate come ricevute dalla fixture. Non ha considerato «ci dispiace per il cambio di programma» un'attribuzione di responsabilità non documentata.

Nella raccolta iniziale delle fixture il valutatore ha letto anche quattro file di regressione Ricalco/Filoporto non richiesti; lo ha dichiarato e li ha esclusi dal giudizio dei due dialoghi. Si conserva questo limite invece di descrivere la review come audit strettamente limitato all'allowlist. La generazione dei dialoghi è distinta da questo passaggio di valutazione.

## Classificazione conservativa degli errori iniziali

1. **Ricalco T1 — copia letterale, hard fail formale.** La clausola contiene `L’assistenza` invece di `L'assistenza`. Il significato non cambia; il requisito di testo identico fallisce. Il catalogo distingue violazioni sostanziali e stringhe protette in modo non perfettamente uniforme: per questa verifica si adotta l'interpretazione più severa quando è richiesta identità letterale, incluse tipografia e punteggiatura. Il successo di T2 non cancella l'errore di T1.
2. **Ardora T1 — fatto implicito inventato, hard fail fattuale.** La formula «grazie per averci indicato le nuove misure» dà per ricevute informazioni che la fixture non dichiara ricevute. È plausibile ma non sostenuta. La prima alternativa è fedele; la seconda e la sua raccomandazione contengono due occorrenze dello stesso problema. T2 e T3 non lo ripetono, senza sanare retroattivamente T1.
3. **Filoporto T2 — preferenza trasformata in indicazione generale, soft fail.** «Cordialità senza battute» amplia una preferenza ancora non deliberata. T3 riconosce che il messaggio non conteneva battute e restringe la regola correttamente. Un problema, una occorrenza, recuperato dal feedback simulato.

La correzione del file principale precisa che vanno verificati anche i fatti impliciti nelle formule di cortesia, che i testi protetti non si normalizzano e che i nuovi obblighi ricavati da preferenze generali sono ulteriori proposte. Non si impongono divieti di umorismo o formule standard per tutti i brand.

Il primo retest Ardora, sul candidato intermedio, non ripete l'invio di nuove misure ma scrive «grazie per averci scritto»: il canale del contatto non è documentato. È una nuova manifestazione dello stesso problema dei fatti impliciti e viene registrata come ulteriore hard fail, non come successo parziale. Il secondo parere conferma il difetto. Il candidato finale chiarisce esplicitamente che una richiesta ricevuta non prova canale o dettagli trasmessi. Il secondo retest Ardora ringrazia per la richiesta, conservando solo l'evento noto.

## Limiti di ciò che è dimostrato

I transcript permettono di verificare contenuto, lunghezza, domande, stato dichiarato e fedeltà ai materiali. Le chiamate di avvio documentano le restrizioni assegnate agli agenti; gli elenchi delle loro letture/scritture sono dichiarazioni dei generatori. Questo archivio non contiene un audit completo e indipendente di tutte le loro operazioni storiche. Non dedurre l'assenza assoluta di accessi o effetti non registrati dal solo testo della risposta.

Il file BV15, quando creato, è verificabile fisicamente e distinto da quelle dichiarazioni. L'esecuzione non installa la skill, non modifica riferimenti aziendali reali, non pubblica contenuti e non prova il caricamento in sessioni future.

Le aziende, i fatti e le approvazioni dei copioni sono sintetici. Si verifica il funzionamento conversazionale, non la riconoscibilità per un'azienda reale o i risultati di marketing. Nessun confronto con generalista, nessuna valutazione cliente, nessun test di browser su siti reali o di importazione PDF complessi è incluso in queste prove.
