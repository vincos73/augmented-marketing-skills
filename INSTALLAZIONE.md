# Installazione di Augmented Marketing Assistant

Questo pacchetto beta riunisce Augmented Marketing Assistant e le cinque skill disponibili di Augmented Marketing Skills.

Non è un plugin universale. Le skill seguono una struttura portabile basata su cartelle con `SKILL.md`; il modo in cui un ambiente registra un agente o carica istruzioni persistenti può invece cambiare.

## Contenuto del pacchetto

```text
agents/augmented-marketing-assistant.md
skills/setup-business-context/
skills/setup-marketing-system/
skills/define-marketing-challenge/
skills/choose-marketing-direction/
skills/define-marketing-mix/
```

Le versioni incluse sono:

| Componente | Versione |
| --- | --- |
| Augmented Marketing Assistant | 0.1.0-beta.1 |
| Setup Business Context (`setup-business-context`) | 0.6.2 |
| Setup Marketing System (`setup-marketing-system`) | 0.2.1 |
| Define Marketing Challenge (`define-marketing-challenge`) | 0.1.1 |
| Choose Marketing Direction (`choose-marketing-direction`) | 0.2.0 |
| Define Marketing Mix (`define-marketing-mix`) | 0.1.1 |

## Installazione assistita

Apri una nuova conversazione nel tuo ambiente e fornisci lo ZIP oppure il link alla release. Puoi usare questa richiesta:

````text
Installa Augmented Marketing Assistant 0.1.0-beta.1 e le cinque skill incluse in questo pacchetto.

Prima di modificare file o configurazioni:
1. individua i percorsi supportati dal mio ambiente per skill e istruzioni persistenti o agenti;
2. spiegami quali file copierai e dove;
3. non sovrascrivere componenti esistenti senza il mio consenso.

Installa ogni cartella completa contenuta in skills/. Configura agents/augmented-marketing-assistant.md come agente o istruzione persistente soltanto con un meccanismo documentato e disponibile nel mio ambiente. Non trasformare l'Assistant in una nuova skill e non dichiararlo caricato se hai verificato soltanto la presenza del file.

Al termine, apri o richiedi una nuova sessione e verifica separatamente:
- percorso e versione di ciascuna skill;
- disponibilità delle skill nella nuova sessione;
- caricamento effettivo dell'Assistant;
- modalità con cui posso invocarlo.

Se il mio ambiente non supporta una delle operazioni, fermati e indicami il passaggio manuale minimo.
````

L'installazione del contenuto non autorizza l'agente a cambiare altre istruzioni, plugin o configurazioni non necessarie.

## Installazione manuale

1. Estrai lo ZIP senza modificare la struttura delle cartelle.
2. Copia ciascuna cartella contenuta in `skills/` nella directory delle skill prevista dal tuo ambiente.
3. Conserva l'intera cartella di ogni skill, inclusi `references/`, `agents/`, esempi e istruzioni di installazione.
4. Usa il meccanismo documentato dal tuo ambiente per registrare o caricare `agents/augmented-marketing-assistant.md` come agente o istruzione persistente.
5. Apri una nuova sessione e verifica che le cinque skill siano visibili e che l'Assistant sia stato effettivamente caricato.

La semplice presenza dei file sul disco non dimostra che una sessione già aperta li abbia caricati.

## Come iniziare

Non devi conoscere il nome delle skill. In una nuova sessione puoi scrivere:

> Aiutami a capire da dove iniziare con questa attività di marketing usando Augmented Marketing Assistant.

Puoi anche descrivere direttamente il bisogno, per esempio:

> Vorrei che l'agente conoscesse bene la mia organizzazione prima di aiutarmi con il marketing.

L'Assistant deve spiegare prima il passaggio utile in linguaggio comune e mostrare soltanto dopo il nome tecnico della skill pertinente, tra parentesi.

## Verifica e limiti della beta

Il pacchetto è stato verificato strutturalmente e l'Assistant ha superato scenari conversazionali interni e un test cieco in una sessione Codex separata. Non sono ancora dimostrati:

- l'installazione nativa con un unico gesto su tutti gli agenti;
- il comportamento completo su piattaforme diverse;
- la comprensibilità presso un campione di marketer esterni;
- l'handoff end-to-end dopo la produzione e l'approvazione di tutti gli artefatti.

Plugin specifici per singole piattaforme potranno essere aggiunti come adattatori separati senza cambiare il nucleo del metodo.
