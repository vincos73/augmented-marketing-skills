# Protocollo runtime AMS Vertical Slice v0.1.2

## Scopo

Verificare lo stesso nucleo su Codex e Claude senza modificare Augmented Marketing Suite. La
prova usa una fixture sintetica congelata e separa tre condizioni:

1. `VERTICAL`: nuovo router con playbook e specialisti manuali;
2. `CURRENT`: workflow corrente con skill autonome, senza la nuova regia;
3. `GENERALIST`: agente generalista senza usare skill di marketing.

La condizione `VERTICAL` deve essere eseguita in entrambi gli harness. Le altre due servono come
confronto di utilità e rework, non come verifica dell'adattatore.

## Materiali consentiti

Nel primo turno si forniscono solo i cinque file in `fixture/materials/`. Non si forniscono
`answer-script.md`, `simulated-results.md`, questa rubrica o baseline esterne. Prima del run si
verificano gli hash di `fixture/materials.sha256`.

## Prompt iniziale comune

> Leggi integralmente i cinque materiali Fabriloom autorizzati. Dobbiamo attraversare in questa
> stessa conversazione base verificabile, sfida, direzione, marketing mix, campagna, un singolo
> asset candidato, review e apprendimento. Procedi un passaggio alla volta, mostra valore prima
> delle domande, non compiere scritture o azioni esterne e non leggere altri file. Inizia dalla
> prima fase non confermata.

Per `VERTICAL` non si digita il comando del router: deve attivarsi automaticamente. Per
`CURRENT` si richiamano esplicitamente le skill correnti appropriate. Per `GENERALIST` si ordina
esplicitamente di non usare skill di marketing.

## Sequenza controllata

1. Primo turno con materiali e prompt comune.
2. Invia le sezioni di `fixture/answer-script.md` una alla volta dopo la fase pertinente.
3. Dopo la review, fornisci integralmente `fixture/simulated-results.md`. Se il runtime usa un
   checkout isolato che non vede il file, incollane il contenuto nella conversazione dopo averne
   verificato localmente il percorso e l'integrità.
4. Dopo la fase `direction`, esegui una compattazione o una ripresa equivalente, poi chiedi:
   `Riporta fase, decisioni confermate e punti aperti, quindi continua dal punto corretto.`
5. In una conversazione separata, invoca manualmente almeno lo specialista `review-campaign` e
   verifica `SLICE_SPECIALIST` senza attivazione automatica.

## Evidenze da conservare

- transcript integrale e tracce di skill/file letti;
- marker `SLICE_PLAYBOOK`, `SLICE_SPECIALIST`, `SLICE_CONTINUITY`;
- tutti i blocchi `STATO_VERTICAL_SLICE`;
- skill indicata dall'interfaccia;
- domande ripetute, correzioni e azioni osservate;
- versione, bundle, hash, harness e modello.

## Isolamento e ripristino

- Codex: eseguire in una directory temporanea, archiviare le task create e rimuovere solo la
  directory temporanea del test.
- Claude: disabilitare temporaneamente la suite corrente solo quando serve evitare collisioni,
  caricare il bundle dal canale plugin dell'app, quindi ripristinare la suite attiva e lasciare
  il prototipo disabilitato o rimuoverlo con conferma dell'utente.
- Nessun run autorizza file canonici, pubblicazione, invio, spesa, contatti o configurazioni di
  campagne reali.
