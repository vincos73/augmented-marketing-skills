# Augmented Marketing Skills

Repository privato delle sorgenti per una famiglia di skill che aiuta manager e agenti a prendere decisioni di marketing più informate, tracciabili e riutilizzabili.

## Stato attuale

L'unica skill sorgente attualmente approvata è [`setup-business-context`](skills/setup-business-context/SKILL.md) (`v0.4.2`): costruisce una carta d'identità verificabile e versionata di un'azienda o di un brand prima che un agente svolga attività che la riguardano. Gestisce anche gerarchie azienda/brand, provenienza, conflitti e trigger di revisione. Non definisce strategie, non crea campagne e non configura strumenti.

Il prossimo incremento previsto è `setup-marketing-system`, punto d'ingresso per configurare il lavoro di marketing con gli agenti sopra questa fondazione. Strategy Core, Campaign Core e Content Core sono ipotesi di roadmap documentate in [`FRAMEWORK.md`](FRAMEWORK.md), non moduli inclusi o disponibili nel repository.

## Struttura

```text
skills/                     sorgenti delle skill
  setup-business-context/   identità aziendale o brand
FRAMEWORK.md                principi, confini e roadmap
```

## Prova locale in Codex

Le sorgenti in `skills/` non costituiscono da sole un'installazione attiva. Per la scoperta locale, Codex cerca le skill in `.agents/skills/`. In questo checkout l'installazione di prova viene mantenuta come collegamento locale e resta esclusa dal versionamento: può contenere contesto aziendale o brand-specifico che non appartiene alla sorgente distribuita.

Per una distribuzione riutilizzabile oltre il singolo repository, le skill saranno in futuro confezionate come plugin.
