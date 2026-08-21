# Augmented Marketing Skills

Repository privato delle sorgenti per una famiglia di skill che aiuta manager e agenti a prendere decisioni di marketing più informate, tracciabili e riutilizzabili.

## Stato attuale

Le skill sorgente attualmente presenti sono:

- [`setup-business-context`](skills/setup-business-context/SKILL.md): costruisce una carta d'identità verificabile di un'azienda o di un brand prima che un agente svolga attività che la riguardano;
- [`content-profile-builder`](skills/content-profile-builder/SKILL.md): conserva profili editoriali e visivi riutilizzabili;
- [`build-evidence-pack`](skills/build-evidence-pack/SKILL.md): separa prove, inferenze, assunzioni e verifiche aperte;
- [`content-director`](skills/content-director/SKILL.md): valuta il materiale e prepara un brief prima della produzione.

`setup-business-context` non definisce strategie, non crea campagne e non configura strumenti.

Le skill successive sono una roadmap documentata in [`FRAMEWORK.md`](FRAMEWORK.md). Non vanno considerate funzionalità già disponibili.

## Struttura

```text
skills/                     sorgenti delle skill
  setup-business-context/   identità aziendale o brand
  content-profile-builder/  profili editoriali e visivi
  build-evidence-pack/      prove e incertezze
  content-director/         giudizio editoriale e brief
FRAMEWORK.md                principi, confini e roadmap
```

## Prova locale in Codex

Le sorgenti in `skills/` non costituiscono da sole un'installazione attiva. Per la scoperta locale, Codex cerca le skill in `.agents/skills/`. In questo checkout l'installazione di prova viene mantenuta come collegamento locale e resta esclusa dal versionamento: può contenere contesto aziendale o brand-specifico che non appartiene alla sorgente distribuita.

Per una distribuzione riutilizzabile oltre il singolo repository, le skill saranno in futuro confezionate come plugin.
