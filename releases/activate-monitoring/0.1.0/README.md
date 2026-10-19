# Monitoraggio: piano, esecuzione e file dell’utente

Questa distribuzione autonoma in italiano collega **setup-monitoring 0.1.2** e **activate-monitoring 0.1.0**. La prima prepara il piano; la seconda lo esegue, conserva lo storico e consegna i risultati. Non richiede SQLite, database, eseguibili aggiuntivi o tre agenti. I plugin della Suite 1.0.0/1.0.2 non sono modificati da questa uscita.

## Download e sorgente

- [Activate Monitoring 0.1.0 — ZIP](https://github.com/vincos73/augmented-marketing-skills/releases/download/activate-monitoring-v0.1.0/activate-monitoring-0.1.0.zip)
- [Setup Monitoring 0.1.2 — ZIP](https://github.com/vincos73/augmented-marketing-skills/releases/download/activate-monitoring-v0.1.0/setup-monitoring-0.1.2.zip)
- [Release GitHub](https://github.com/vincos73/augmented-marketing-skills/releases/tag/activate-monitoring-v0.1.0)
- [Sorgente di activate-monitoring](source/activate-monitoring/) e [sorgente di setup-monitoring](source/setup-monitoring/)
- [Manifest dei contenuti](manifest.json) e [checksum](SHA256SUMS)

Ogni ZIP contiene una sola cartella skill, con `SKILL.md`, riferimenti e metadata facoltativi in `agents/openai.yaml`. Usa il caricamento di skill supportato dal tuo ambiente; i due ZIP non sono plugin completi. Se hai già un piano approvato e autosufficiente, puoi usare activate-monitoring senza installare setup-monitoring. Questa pubblicazione su GitHub non è una pubblicazione nel catalogo ChatGPT.

## Come si usa

1. Con setup-monitoring: «Voglio seguire menzioni e notizie del mio brand per preparare un briefing settimanale». La skill prepara `monitoring-plan.md` e raccoglie solo le decisioni necessarie.
2. Dopo l’approvazione: «Usa activate-monitoring per eseguire questo piano e conservare i risultati nella mia cartella Monitoraggi».
3. In seguito: «Aggiorna questo monitoraggio» oppure «Che cosa era emerso e quali rettifiche ci sono state?».

La cartella viene scelta una volta. Un esempio:

```text
Monitoraggi/NomeBrand/
  monitoring-plan.md
  registro.md
  report/
    2026-10-19_09-00-00_C0001.md
```

Il piano contiene le scelte approvate. Il registro conserva controlli, novità già osservate, rettifiche, pendenti e consegne. I report rimangono leggibili e consultabili. La cartella può essere quella indicata dall’utente; non deve stare nella directory della skill o in una cartella tecnica nascosta. Le convenzioni dei file funzionano su Windows e macOS senza un programma specifico per sistema.

## Capacità necessarie e limiti

La skill usa gli strumenti effettivamente disponibili per cercare, leggere e salvare. Non aggiunge da sola l’accesso a una cartella del computer. Per uno storico aggiornato automaticamente l’ambiente deve poter rileggere e scrivere in quella cartella fra esecuzioni. Se non può, la skill dichiara il limite e può proporre file portabili da salvare o ricollegare; un download non equivale a un salvataggio già avvenuto nella cartella.

La ricorrenza richiede un meccanismo dell’ambiente che riavvii davvero il lavoro, con strumenti e dati disponibili. «Predisposto», «programmato» e «primo ciclo eseguito» restano stati distinti. L’installazione della skill non avvia un servizio in background, non sincronizza computer e non autorizza email. Quando esiste un plugin di posta adatto, l’utente può scegliere un invio singolo o ricorrente con destinatari e contenuto definiti.

La consegna ordinaria comprende riepilogo in chat, report completo e storico quando il salvataggio è disponibile. Fonti del piano e ricerca aperta restano complementari. I risultati riportano prove, date e lacune; non promettono completezza del web o superiorità su una ricerca generalista.

## Verifiche di questa uscita

Sono previste soltanto verifica strutturale delle skill, lettura delle istruzioni, controllo dei riferimenti interni, parità fra sorgenti e ZIP e checksum. Non sono eseguiti nuovi confronti di ricerca, simulazioni comportamentali o prove integrate su ChatGPT desktop, Windows o macOS. La disponibilità delle funzioni dipende dall’ambiente che carica le skill.

Questa è una nuova versione del flusso in Markdown, distinta dalle precedenti preview sperimentali con SQLite. Gli esperimenti storici non ne provano le prestazioni. Non importa automaticamente database, non modifica vecchi archivi e non installa o attiva la skill sul computer dell’autore.

Il comando di manutenzione del repository è `python3 scripts/build_monitoring_release.py`; `--check` confronta gli asset con gli otto file sorgente senza eseguire un monitoraggio. Questo comando serve al packaging dell’autore, non all’utente della skill.
