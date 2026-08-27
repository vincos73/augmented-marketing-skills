# Installazione di Augmented Marketing Suite

La beta 0.1.0-beta.5 è un plugin OpenAI per ChatGPT e Codex. Riunisce le cinque skill disponibili e Augmented Marketing Assistant, l'ingresso conversazionale che orienta verso la skill pertinente.

Non include MCP, connector, hook o automazioni.

## Contenuto

```text
.codex-plugin/plugin.json
skills/augmented-marketing-assistant/
skills/setup-business-context/
skills/setup-marketing-system/
skills/define-marketing-challenge/
skills/choose-marketing-direction/
skills/define-marketing-mix/
```

| Componente | Versione |
| --- | --- |
| Plugin Augmented Marketing Suite (`augmented-marketing-suite`) | 0.1.0-beta.5 |
| Augmented Marketing Assistant (`augmented-marketing-assistant`) | 0.1.0 stabile |
| Setup Business Context (`setup-business-context`) | 0.6.3 |
| Setup Marketing System (`setup-marketing-system`) | 0.3.0 |
| Define Marketing Challenge (`define-marketing-challenge`) | 0.1.2 |
| Choose Marketing Direction (`choose-marketing-direction`) | 0.2.1 |
| Define Marketing Mix (`define-marketing-mix`) | 0.1.2 |

## ChatGPT sul web

Allegare lo ZIP a una chat normale permette a ChatGPT di leggerne i file, ma non registra il plugin e non rende le skill disponibili nelle chat successive.

Finché questa beta non è presente nel catalogo Plugin generale, installala come plugin personale soltanto se Plugin Creator è disponibile nel tuo account o workspace:

Se hai già installato la beta.2 come Augmented Marketing Assistant, rimuovi quel plugin prima di installare la Suite. Il nuovo identificatore tecnico farebbe altrimenti comparire due plugin distinti.

Se hai installato una beta precedente di Augmented Marketing Suite, aggiorna o reinstalla lo stesso plugin con il pacchetto beta.5, poi apri una nuova chat per evitare di riusare skill già caricate nella sessione precedente.

1. apri una nuova chat in modalità Work;
2. richiama Plugin Creator (`@plugin-creator`);
3. allega lo ZIP della beta.5;
4. usa la richiesta seguente;
5. al termine, apri il catalogo Plugin e verifica la sezione personale o “Created by me”;
6. installa il plugin e avvia una nuova chat.

````text
Crea un plugin personale dal pacchetto allegato Augmented Marketing Suite 0.1.0-beta.5.

Verifica che la radice contenga .codex-plugin/plugin.json e che il manifesto dichiari skills/ come directory delle skill. Non aggiungere MCP, connector, hook o altri componenti.

Registra il plugin nel mio marketplace personale senza modificare le skill incluse. Al termine dimmi come installarlo dal catalogo Plugin e ricordami di provarlo in una nuova chat.
````

Se Plugin Creator o i plugin personali non sono disponibili, lo ZIP non può essere installato direttamente da una chat normale. In quel caso è possibile soltanto ispezionarlo oppure installare separatamente le singole skill con il meccanismo disponibile nell'ambiente.

## Codex

Il pacchetto usa lo stesso manifesto OpenAI. Aggiungilo attraverso un marketplace personale o di progetto e installalo dal catalogo Plugin. Dopo l'installazione, avvia una nuova sessione: la presenza dei file sul disco non dimostra che la sessione corrente li abbia caricati.

## Come iniziare

Descrivi direttamente il bisogno, per esempio:

> Vorrei che l'agente conoscesse bene la mia organizzazione prima di aiutarmi con il marketing.

Quando la richiesta corrisponde chiaramente a una skill specialistica, l'ambiente dovrebbe selezionarla direttamente. Usa Augmented Marketing Assistant soltanto quando non sai da quale passaggio iniziare: in ChatGPT puoi richiamarlo con `@Augmented Marketing Assistant`, in Codex con `$augmented-marketing-assistant`.

L'Assistant spiega prima il passaggio utile in linguaggio comune e indica poi tra parentesi il nome tecnico della skill pertinente. Se l'ambiente non gli permette di attivarla, ti chiede di invocarla direttamente e si ferma senza simularne il lavoro.

Nel catalogo, le skill sono mostrate con il titolo tecnico inglese, per esempio `setup-business-context`, e con una breve descrizione italiana. Nome della cartella, titolo visibile e nome da invocare restano così allineati.

## Verifica della Suite beta

La beta.5 può essere validata strutturalmente e installata come plugin OpenAI. Augmented Marketing Assistant v0.1.0 ha superato i test runtime Codex di richiesta ambigua, selezione diretta e handoff. Restano da verificare separatamente:

- l'installazione effettiva nell'account ChatGPT dell'utente;
- il caricamento delle sei skill in una nuova chat;
- il fallback dell'Assistant quando l'handoff non è disponibile;
- la comprensibilità presso marketer esterni;
- gli adattatori per piattaforme diverse da OpenAI.

La beta.1 resta un archivio neutro per installazioni manuali. Non deve essere presentata come plugin ChatGPT.
