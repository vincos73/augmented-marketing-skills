# Stato Augmented Marketing Suite 1.0.2

**Aggiornato:** 10 ottobre 2026

| Distribuzione | Versione | Stato |
| --- | --- | --- |
| Pacchetto OpenAI e relativo sorgente | 1.0.2 | Preparato per la pubblicazione GitHub; lo ZIP coincide con quello inviato a OpenAI |
| Catalogo ChatGPT | 1.0.2 | In review, non pubblicato |
| Plugin Claude, skill italiane e ZIP portabili | 1.0.0 | Release GitHub esistente; non aggiornati da questa uscita |

Il [pacchetto OpenAI](releases/1.0.2/openai/) è una distribuzione in inglese diversa dai sorgenti italiani 1.0.0 nella cartella principale [`skills/`](skills/). I due insiemi hanno testi diversi; quindi la 1.0.2 OpenAI è conservata integralmente in `releases/1.0.2/openai/source/` senza sostituire le skill italiane. Il logo e i metadati del listing sono nella stessa cartella sorgente.

Lo ZIP GitHub ha SHA-256 `8e68e50f92a8aca57786cbf27cf7e3281672a224607d095232fe4d3f75c07da5`. Il controllo locale confronta tutti i 58 file dello ZIP con il sorgente e verifica manifest, immagini e numero di skill.

La [candidatura OpenAI](https://platform.openai.com/plugins/manage/plugins_6ac733d9a7c4819181cd6ada460e34b2?version=pluginrel_75f04a46504481919d752066ebcd2a85) è stata inviata l'8 ottobre e risultava **In review** dopo l'invio. Pubblicare il codice e lo ZIP su GitHub non completa la review di OpenAI. Il [rapporto della 1.0.0](RELEASE-STATUS.md) resta valido per Claude, le skill italiane e gli ZIP portabili.
