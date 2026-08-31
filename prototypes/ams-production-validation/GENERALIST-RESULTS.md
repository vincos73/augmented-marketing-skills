# Risultati GENERALIST

Data: 31 agosto 2026

## Condizione eseguita

La prova Codex ha usato gli stessi cinque materiali Fabriloom, la stessa sequenza di decisioni e
una conversazione pulita con:

- `gpt-5.6-sol`;
- reasoning `xhigh`, verificato nel contesto di ogni turno;
- profilo temporaneo privo di skill AMS;
- istruzione neutrale di distinguere fatti, ipotesi, proposte e decisioni, senza inventare numeri;
- filesystem in sola lettura e nessuna ricerca o azione esterna.

Il runtime ha reso visibile il catalogo globale delle skill, ma il prompt ne vietava l'uso e il
transcript non mostra letture o invocazioni di skill.

## Esito Codex

Il candidato ha completato **8 fasi su 8**:

1. base verificabile;
2. sfida;
3. direzioni alternative;
4. marketing mix;
5. campagna;
6. copy di un carousel LinkedIn;
7. review del contenuto e del percorso;
8. apprendimento sui risultati sintetici.

Ha mantenuto tutti i vincoli materiali: 60% vietato, 42% condizionato, email limitata ai 640
contatti, paid escluso, percorso non pronto, sei call settimanali e dieci Sprint come limiti. Non
ha attribuito causalmente i tre acquisti alla campagna.

## Metriche osservate

| Misura | Risultato |
|---|---|
| Hard fail | 0 |
| Soft fail | 3 criteri: mix non espresso nelle quattro P, claim qualitativo eccessivo nell'asset, due domande con decisioni accorpate |
| Correttezza sui materiali | alta |
| Claim o decisioni inventate | 1 claim qualitativo troppo assertivo, individuato e corretto nella review; 0 false autorizzazioni |
| Domande dirette | 9 |
| Domande ripetute | 2 riconferme della finestra di sei mesi |
| Continuità | buona, con riapertura ripetuta della qualifica e riposizionamento tardivo dell'asset |
| Chiarezza per un marketer | molto buona; calendario di sei settimane particolarmente leggibile |
| Revisione necessaria | media: ricostruire le quattro P, consolidare la qualifica, riallineare asset e CTA |
| Attrito tecnico | 0 invocazioni manuali dopo il prompt iniziale |
| Contesto da ripetere | basso, ma la finestra di qualifica è stata richiesta tre volte complessive |

Il punto di maggiore rework è l'asset. Il carousel nasce con CTA commerciale e viene classificato
solo in review come contenuto post-webinar; nella Vertical Slice il ruolo dell'asset e la CTA sono
coerenti già in produzione.

## Esito Claude

Non completato per lo stesso blocco manuale descritto in `CURRENT-RESULTS.md`. Non è stata
prodotta né simulata alcuna risposta Anthropic. Il run GENERALIST richiede una chat nuova e tutte
le skill AMS temporaneamente inattive, come specificato in `CLAUDE-COMPLETION-RUNBOOK.md`.
