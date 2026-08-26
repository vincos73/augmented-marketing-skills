# Configurare l'identità aziendale approvata

Leggi questa reference soltanto dopo che l'identità ha superato il gate 1 di approvazione e l'utente ha scelto l'host dell'agente.

## Salvaguardie comuni

Prima di proporre una modifica:

1. Controlla i file esistenti alla radice `AGENTS.md`, `AGENTS.override.md`, `CLAUDE.md`, `.claude/CLAUDE.md` e `CLAUDE.local.md` pertinenti all'host scelto.
2. Individua eventuali istruzioni o import già presenti per il contesto aziendale. Aggiornali invece di aggiungere un duplicato.
3. Conserva ogni contenuto non pertinente. Non sostituire mai un intero file di istruzioni per installare questo contesto.
4. Mostra l'aggiunta o il diff esatto e spiega che i file di istruzioni guidano il comportamento dell'agente, ma non concedono nuovi permessi né autorizzano azioni esterne.
5. Applica soltanto le modifiche all'host approvate esplicitamente dall'utente.

Usa commenti stabili intorno al blocco inserito, così gli aggiornamenti successivi potranno individuarlo in sicurezza:

```markdown
<!-- setup-business-context:start -->
[managed instructions]
<!-- setup-business-context:end -->
```

Se esiste già un blocco con questi marcatori, sostituisci soltanto il suo contenuto. Se esistono istruzioni semanticamente equivalenti senza marcatori, adattale con attenzione invece di creare regole concorrenti.

## Adattatore Codex

Codex legge le istruzioni del progetto in `AGENTS.md` prima di lavorare. Preferisci il file `AGENTS.md` alla radice che si applica al workspace. Se a quel livello è attivo un `AGENTS.override.md`, spiega il problema di precedenza e non modificare il file inattivo come se l'installazione fosse riuscita.

Usa un blocco conciso come questo:

```markdown
<!-- setup-business-context:start -->
## Identità aziendale

Prima di lavorare per o su [Entity], leggi `[identity-path]` e applica i suoi fatti approvati, la terminologia e i vincoli. Non trattare le incognite note come fatti. Per il lavoro su un brand figlio, leggi anche il file corrispondente sotto `.agents/brands/`.
<!-- setup-business-context:end -->
```

Conserva l'identità canonica nel suo file. Non duplicare l'intero documento dentro `AGENTS.md`.

Dopo la modifica, rileggi dal disco il blocco salvato. Riporta che l'istruzione è stata configurata sul disco, non che la sessione corrente l'abbia caricata o che ogni risposta futura del modello sia garantita.

Codex rileva le istruzioni del progetto una volta per esecuzione. Spiega che il nuovo blocco è configurato sul disco per le esecuzioni successive e che l'utente deve iniziare un nuovo task o una nuova sessione Codex prima di provarlo. Se l'host può riportare le fonti di istruzioni caricate, usa quel controllo in sola lettura; altrimenti non dichiarare che la sessione corrente abbia ricaricato la modifica.

## Adattatore Claude Code

Claude Code legge i file di progetto `CLAUDE.md`, non `AGENTS.md` direttamente. Preferisci un `CLAUDE.md` esistente alla radice; se non esiste, proponi di crearne uno. Conserva le scelte già fatte dal progetto tra `.claude/CLAUDE.md` e `CLAUDE.local.md` invece di spostarle in silenzio.

Claude Code supporta gli import di file con `@percorso`. Per una singola azienda o un brand autonomo, usa un import diretto così l'identità approvata viene caricata insieme alle istruzioni del progetto:

```markdown
<!-- setup-business-context:start -->
@[identity-path]
<!-- setup-business-context:end -->
```

Sostituisci `[identity-path]` con il percorso relativo reale, per esempio `@.agents/company-identity.md`; non lasciare le parentesi nella riga installata.

Quando il workspace usa anche Codex, il file di Claude può importare anche le istruzioni condivise dell'agente:

```markdown
@AGENTS.md
```

Non aggiungere due volte questa riga. Un link simbolico non è necessario.

Per un'azienda con più brand, importa l'identità aziendale come genitore sempre caricato. Aggiungi un'istruzione concisa per leggere il file pertinente `.agents/brands/<brand-slug>.md` quando un'attività riguarda un brand figlio; non importare ogni brand per impostazione predefinita.

Dopo la modifica, rileggi dal disco l'import salvato e il percorso dell'identità referenziato. Spiega che Claude tratta questi file come contesto persistente del progetto, non come controlli di sicurezza vincolanti.

Claude Code può mostrare una finestra di approvazione al primo uso degli import di file. Di' all'utente di controllare e accettare il percorso esatto dell'identità prima di affidarsi all'import. Quando disponibile, verifica i file caricati con la vista `/memory` di Claude in una nuova sessione; un import osservato sul disco è configurato, ma non dimostra che la sessione in esecuzione lo abbia caricato o approvato.

## Altri host di agenti

Non indovinare nomi proprietari dei file di istruzioni e non dichiarare compatibilità non verificata. Mantieni portabile l'identità approvata e indica all'utente che cosa deve verificare per il proprio host: il file di istruzioni del progetto, il suo ambito di caricamento e la possibilità di referenziare o importare l'artefatto dell'identità.
