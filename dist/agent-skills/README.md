# Augmented Marketing Suite beta.7: skill portabili

Questa cartella contiene una custom skill per archivio ZIP. Ogni archivio ha una sola cartella radice, con `SKILL.md` e gli eventuali `references/`, ed è adatto ai flussi che caricano una skill alla volta.

## Archivi inclusi

| Archivio | Skill | Versione |
| --- | --- | --- |
| `setup-business-context-0.6.4.zip` | `setup-business-context` | `0.6.4` |
| `setup-marketing-system-0.3.1.zip` | `setup-marketing-system` | `0.3.1` |
| `define-marketing-challenge-0.1.3.zip` | `define-marketing-challenge` | `0.1.3` |
| `choose-marketing-direction-0.2.2.zip` | `choose-marketing-direction` | `0.2.2` |
| `define-marketing-mix-0.1.3.zip` | `define-marketing-mix` | `0.1.3` |

## Uso

1. Scegli una sola skill in base al risultato che vuoi ottenere.
2. Confronta il checksum dello ZIP con `SHA256SUMS`.
3. Carica lo ZIP nel flusso di custom skill del tuo ambiente, oppure estrailo nella destinazione locale documentata da quell'ambiente.
4. Apri una nuova chat o sessione e prova una richiesta pertinente.

Questi archivi contengono esclusivamente le cinque skill specialistiche. Non includono Augmented Marketing Assistant, perché è un adattatore per il pacchetto OpenAI/Codex. Per informazioni sui flussi Claude, ChatGPT, Codex e Projects, leggi `../../INSTALLAZIONE.md`.

## Limiti

- L'upload e la selezione automatica dipendono da prodotto, piano, amministratore e versione dell'ambiente.
- Allegare uno ZIP a una chat normale non prova l'installazione persistente.
- Questo pacchetto fa parte della release GitHub di Augmented Marketing Suite beta.7.
