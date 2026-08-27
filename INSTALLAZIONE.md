# Installazione di Augmented Marketing Assistant

La beta 0.1.0-beta.2 è un plugin OpenAI per ChatGPT e Codex. Riunisce le cinque skill disponibili e un adattatore tecnico che espone Augmented Marketing Assistant negli ambienti OpenAI.

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
| Plugin Augmented Marketing Assistant | 0.1.0-beta.2 |
| Adattatore OpenAI (`augmented-marketing-assistant`) | 0.1.0-beta.2 |
| Setup Business Context (`setup-business-context`) | 0.6.2 |
| Setup Marketing System (`setup-marketing-system`) | 0.2.1 |
| Define Marketing Challenge (`define-marketing-challenge`) | 0.1.1 |
| Choose Marketing Direction (`choose-marketing-direction`) | 0.2.0 |
| Define Marketing Mix (`define-marketing-mix`) | 0.1.1 |

## ChatGPT sul web

Allegare lo ZIP a una chat normale permette a ChatGPT di leggerne i file, ma non registra il plugin e non rende le skill disponibili nelle chat successive.

Finché questa beta non è presente nel catalogo Plugin generale, installala come plugin personale soltanto se Plugin Creator è disponibile nel tuo account o workspace:

1. apri una nuova chat in modalità Work;
2. richiama Plugin Creator (`@plugin-creator`);
3. allega lo ZIP della beta.2;
4. usa la richiesta seguente;
5. al termine, apri il catalogo Plugin e verifica la sezione personale o “Created by me”;
6. installa il plugin e avvia una nuova chat.

````text
Crea un plugin personale dal pacchetto allegato Augmented Marketing Assistant 0.1.0-beta.2.

Verifica che la radice contenga .codex-plugin/plugin.json e che il manifesto dichiari skills/ come directory delle skill. Non aggiungere MCP, connector, hook o altri componenti.

Registra il plugin nel mio marketplace personale senza modificare le skill incluse. Al termine dimmi come installarlo dal catalogo Plugin e ricordami di provarlo in una nuova chat.
````

Se Plugin Creator o i plugin personali non sono disponibili, lo ZIP non può essere installato direttamente da una chat normale. In quel caso è possibile soltanto ispezionarlo oppure installare separatamente le singole skill con il meccanismo disponibile nell'ambiente.

## Codex

Il pacchetto usa lo stesso manifesto OpenAI. Aggiungilo attraverso un marketplace personale o di progetto e installalo dal catalogo Plugin. Dopo l'installazione, avvia una nuova sessione: la presenza dei file sul disco non dimostra che la sessione corrente li abbia caricati.

## Come iniziare

In ChatGPT puoi richiamare esplicitamente l'adattatore con una menzione `@` e il nome Augmented Marketing Assistant. In Codex puoi richiamarlo con `$augmented-marketing-assistant`.

Puoi anche descrivere direttamente il bisogno, per esempio:

> Vorrei che l'agente conoscesse bene la mia organizzazione prima di aiutarmi con il marketing.

L'Assistant deve spiegare prima il passaggio utile in linguaggio comune e indicare poi tra parentesi il nome tecnico della skill pertinente.

## Verifica della beta

La beta.2 può essere validata strutturalmente e installata come plugin OpenAI. Restano da verificare con test separati:

- l'installazione effettiva nell'account ChatGPT dell'utente;
- il caricamento delle sei skill in una nuova chat;
- l'handoff completo dall'Assistant alla skill pertinente;
- la comprensibilità presso marketer esterni;
- gli adattatori per piattaforme diverse da OpenAI.

La beta.1 resta un archivio neutro per installazioni manuali. Non deve essere presentata come plugin ChatGPT.
