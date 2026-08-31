# Content Core — punto della situazione

Aggiornato: 31 agosto 2026

## Stato attuale

Il Content Core è definito nel documento autorevole [`MARKETING-AGENT-SYSTEM.md`](MARKETING-AGENT-SYSTEM.md), ma non è ancora un core implementato né una skill pubblicabile.

La decisione centrale è separare il giudizio editoriale dalla produzione:

- `Content Director` valuta se un materiale merita un contenuto, quale obiettivo può servire e quale formato lo valorizza;
- i builder specializzati producono e verificano il singolo asset;
- una futura `editorial-review` può revisionare contenuti creati altrove o pacchetti multi-asset, ma non è un passaggio obbligatorio dopo ogni builder.

## Content Director

Il nome confermato è `Content Director`, preferito a `Content Router` perché comunica giudizio editoriale e non semplice instradamento tecnico.

Può ricevere URL, articoli, documenti, appunti, trascrizioni, ricerche o idee incomplete. Quando disponibili, usa business context, Marketing Foundations e overlay di brand pertinenti per valutare:

1. valore editoriale;
2. struttura dell'idea;
3. solidità delle prove;
4. obiettivo;
5. formato più adatto.

Il risultato previsto è un brief editoriale, non l'asset finale. Deve indicare formato, obiettivo, pubblico, idea centrale, fonte primaria, affermazioni da verificare, sequenza e CTA. Può anche concludere che il materiale non è ancora sufficiente.

Non decide numero preciso delle slide, formulazione finale, composizione, leggibilità, montaggio o resa grafica: queste decisioni restano al builder competente.

## Confini già fissati

- `Carousel Builder`: selezione, fedeltà, struttura, slide, grafica, leggibilità e QA del carosello.
- `Quote Card Builder`: selezione della frase, attribuzione, adattamento, gerarchia e QA della card.
- `Content Director`: merito editoriale, obiettivo e formato.
- `Editorial Review` futura: audit di contenuti esterni o campagne multi-asset.

I criteri comuni da poter riusare in futuro sono fedeltà alle fonti, distinzione tra citazione e parafrasi, forza delle affermazioni, coerenza con pubblico e obiettivo, attribuzioni e CTA. Gli standard editoriali e visivi minimi vivono nelle Marketing Foundations; manuali, template e asset dettagliati restano riferimenti esterni.

## Che cosa non c’è ancora

- nessun blueprint autonomo del Content Core;
- nessuna sorgente installabile di `content-director` nel branch corrente;
- nessun catalogo eval o fixture dedicato al Content Core;
- nessuna `editorial-review` implementata;
- nessun nuovo `content-profile-builder` approvato o da reintrodurre.

Esistevano draft sperimentali di `content-director` e `build-evidence-pack` in una fase precedente, ma non fanno parte del set approvato e non vanno trattati come skill disponibili.

## Prossimo passaggio concordato

Il prossimo lavoro non è creare una raccolta di generatori di post, copy, email o landing. È collegare un primo percorso Content ai builder già esistenti e osservarlo con utenti reali, verificando che:

- l'utente capisca se vale la pena produrre il contenuto;
- emerga una raccomandazione di formato motivata;
- le prove mancanti e i claim fragili restino visibili;
- il brief trasferisca il contesto senza duplicare il builder;
- il builder conservi autonomia sul proprio formato e QA;
- il flusso possa fermarsi quando il materiale non è sufficiente.

Il micro-pilot viene dopo la validazione dei percorsi fondativi e strategici già indicati nel system document. Non si deve presentare il Content Core come pronto, né confondere un brief con un contenuto prodotto.

## Riferimento GitHub

Questo stato è documentazione di progettazione, non una release. Per continuare sul portatile:

```bash
git fetch origin
git switch --track origin/codex/campaign-core-skill-candidates
sed -n '1,240p' CONTENT-CORE-STATUS.md
```

Il documento autorevole completo è [`MARKETING-AGENT-SYSTEM.md`](MARKETING-AGENT-SYSTEM.md:606), in particolare le sezioni “Content Director: responsabilità e confini” e “Confine con Carousel Builder e Quote Card Builder”.

