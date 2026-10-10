# Stato Augmented Marketing Suite 1.0.2

**Aggiornato:** 10 ottobre 2026

| Distribuzione | Versione | Stato |
| --- | --- | --- |
| Pacchetto OpenAI e relativo sorgente | 1.0.2 | [Release GitHub pubblica](https://github.com/vincos73/augmented-marketing-skills/releases/tag/augmented-marketing-suite-v1.0.2); lo ZIP coincide con quello inviato a OpenAI |
| Catalogo ChatGPT | 1.0.2 | In review, non pubblicato |
| Plugin Claude, skill italiane e ZIP portabili | 1.0.0 | Release GitHub esistente; non aggiornati da questa uscita |
| Pagina Vincos | plugin 0.12.3 | Aggiornata il 10 ottobre con link OpenAI 1.0.2 e Claude 1.0.0 |

Il [pacchetto OpenAI](releases/1.0.2/openai/) è una distribuzione in inglese diversa dai sorgenti italiani 1.0.0 nella cartella principale [`skills/`](skills/). I due insiemi hanno testi diversi; quindi la 1.0.2 OpenAI è conservata integralmente in `releases/1.0.2/openai/source/` senza sostituire le skill italiane. Il logo e i metadati del listing sono nella stessa cartella sorgente.

Lo ZIP GitHub ha SHA-256 `8e68e50f92a8aca57786cbf27cf7e3281672a224607d095232fe4d3f75c07da5`. Il controllo locale confronta tutti i 58 file dello ZIP con il sorgente e verifica manifest, immagini e numero di skill.

La [candidatura OpenAI](https://platform.openai.com/plugins/manage/plugins_6ac733d9a7c4819181cd6ada460e34b2?version=pluginrel_75f04a46504481919d752066ebcd2a85) è stata inviata l'8 ottobre e risultava **In review** dopo l'invio. Pubblicare il codice e lo ZIP su GitHub non completa la review di OpenAI. Il [rapporto della 1.0.0](RELEASE-STATUS.md) resta valido per Claude, le skill italiane e gli ZIP portabili.

La [pagina Vincos](https://vincos.it/augmented-marketing-suite/) usa il plugin WordPress 0.12.3: mostra OpenAI 1.0.2 con il download della release, segnala la review ChatGPT e mantiene il link Claude alla 1.0.0. Il [pacchetto e il sorgente del plugin pagina](releases/1.0.2/site/) sono archiviati separatamente. La verifica locale della pagina ha superato 33 controlli del builder, l'integrità e il checksum degli ZIP; WordPress ha confermato l'aggiornamento e la pagina pubblica mostra i due link. Il controllo PHP da CLI non è stato eseguito perché `php` non è installato in questo ambiente.
