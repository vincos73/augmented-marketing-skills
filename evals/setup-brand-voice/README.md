# Prove di `setup-brand-voice` — prima versione

Pacchetto di test progettato il 7 settembre 2026 per la prima versione sorgente della skill. Le quattro aziende, le persone, i documenti, i dati e i testi sono interamente sintetici. La presenza di questi materiali non dimostra che la skill sia stata eseguita o che abbia superato le prove.

I criteri sono stati scritti separatamente dalla skill e dal blueprint, senza leggerli durante la loro preparazione. Si ispirano allo standard della suite e alle strutture di eval esistenti; questo è isolamento rispetto all'implementazione, non assenza di conoscenza del progetto.

## Organizzazione

- `fixtures/`: soli materiali aziendali da trattare come dati; l'autore, lo stato e l'ambito dichiarati fanno parte dello scenario sintetico.
- `inputs/test1-approved-guide.md` → Ricalco: una guida approvata da rendere utilizzabile.
- `inputs/test2-inconsistent-materials.md` → Filoporto: materiali incoerenti e nessuna guida.
- `inputs/test3-no-materials.md` → Sponda: nessun testo preesistente.
- `inputs/test4-scoped-revision.md` → Teralba: revisione limitata tra più brand, lingue e voci.
- `inputs/regressions.md`: richieste aggiuntive; inviare una sola variante per run.
- `operator/multiturn.md`: messaggi successivi da rilasciare uno alla volta.
- `reviewer/expected-behavior.md`: invarianti per il valutatore, non risposte modello da imitare.
- `eval-catalog.md`: 16 scenari, hard fail, soft fail e modalità di rendicontazione.

## Protocollo di isolamento

1. Il generatore riceve la skill, gli eventuali riferimenti della skill necessari all'esecuzione, un solo input e la sua allowlist di fonti. Non riceve questo README, il catalogo, le attese o i futuri turni dell'operatore.
2. Per un test realmente indipendente usare un agente nuovo, senza cronologia di authoring. Registrare il modello, la versione o hash del pacchetto, l'input esatto e i percorsi effettivamente letti.
3. Tutti i run sono in sola lettura e senza ricerca o azioni esterne, salvo la specifica prova isolata BV15. Una risposta simulata «approvo» o «salva» non annulla questo limite.
4. Congelare la risposta prima di fornire catalogo e attese al valutatore. Congelare anche ogni turno prima di rilasciare quello successivo.
5. Il valutatore riceve input e fonti autorizzate, risposta congelata, catalogo e sole attese pertinenti. I log di lettura/scrittura si valutano quando disponibili; il testo finale da solo non prova quali file siano stati letti o modificati.
6. Registrare separatamente prima risposta, dialogo completo, artefatto isolato e controllo strutturale. Non estendere l'esito di un primo turno all'intera skill.

I file della suite letti dall'autore spiegano il metodo; non sono fonti aziendali. Le fixture di regressione collegate sono a loro volta sintetiche e non dichiarano che esistano dati aziendali reali o installazioni attive.
