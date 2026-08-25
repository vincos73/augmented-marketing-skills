# Augmented Marketing Skills

Repository privato delle sorgenti per una famiglia di skill che aiuta manager e agenti a prendere decisioni di marketing più informate, tracciabili e riutilizzabili.

## Stato attuale

L'unica skill sorgente attualmente approvata è [`setup-business-context`](skills/setup-business-context/SKILL.md) (`v0.5.0`): costruisce una carta d'identità verificabile e versionata di un'azienda o di un brand prima che un agente svolga attività che la riguardano. Gestisce anche gerarchie azienda/brand, provenienza, conflitti e trigger di revisione. Non definisce strategie, non crea campagne e non configura strumenti.

Il prossimo incremento, [`setup-marketing-system`](skills/setup-marketing-system/SKILL.md), è presente come candidata locale `v0.1.0` in authoring e valutazione: definisce le regole di marketing stabili che gli agenti devono applicare sopra il business context. Non è ancora una skill approvata o installata. Strategy Core, Campaign Core e Content Core sono ipotesi di roadmap documentate in [`MARKETING-AGENT-SYSTEM.md`](MARKETING-AGENT-SYSTEM.md), non moduli inclusi o disponibili nel repository.

## Struttura

```text
skills/                     sorgenti delle skill
  setup-business-context/   identità aziendale o brand
  setup-marketing-system/   candidata: regole marketing stabili
evals/                      fixture sintetiche, cataloghi e run di valutazione
MARKETING-AGENT-SYSTEM.md   principi, regole, confini e roadmap
```

## Prova locale in Codex

Le sorgenti in `skills/` non costituiscono da sole un'installazione attiva. Per la scoperta locale, Codex cerca le skill in `.agents/skills/`. In questo checkout l'installazione di prova viene mantenuta come collegamento locale e resta esclusa dal versionamento: può contenere contesto aziendale o brand-specifico che non appartiene alla sorgente distribuita.

Per una distribuzione riutilizzabile oltre il singolo repository, le skill saranno in futuro confezionate come plugin.

## Distribuzione della skill

La release stabile include un pacchetto ZIP versionato della sola skill e il relativo checksum. Per l'installazione manuale, consulta [`INSTALL.md`](skills/setup-business-context/INSTALL.md) oppure scarica la [release GitHub v0.5.0](https://github.com/vincos73/augmented-marketing-skills/releases/tag/v0.5.0).
