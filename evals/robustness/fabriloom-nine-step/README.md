# Static evidence boundary Fabriloom su nove skill

Questo controllo elenca nell'ordine corretto le nove skill reali e risolve un'evidenza locale per ciascuna. Registra il confine tra il profilo conversazionale `chat-v1`, scenario statico pre-execution, e la fixture distinta `integrated-postexecution-v1`.

Non è un run comportamentale. Non concatena cinque passaggi a quattro stadi artefatto e non sostiene che le skill abbiano eseguito la catena. Il tracking resta `unverified` nello stato sorgente. Il profilo integrato richiede nuova evidenza Operations oltre il boundary e non eredita salvataggio, autorizzazione o esecuzione dalla conversazione.

    python3 evals/robustness/fabriloom-nine-step/scripts/check_bridge.py
