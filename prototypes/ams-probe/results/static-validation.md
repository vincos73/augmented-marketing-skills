---
artifact: ams-probe-static-validation
status: pass
probe_version: "0.0.1"
validated_on: "2026-08-30"
---

# Validazione statica AMS Probe

## Esito

**PASS**

## Controlli superati

- Sorgente neutrale unica per router, specialisti e playbook.
- Bundle OpenAI e Claude rigenerati in modo deterministico.
- Manifest OpenAI validato con `plugin-creator/scripts/validate_plugin.py`.
- Skill sorgente e skill OpenAI validate con `skill-creator/scripts/quick_validate.py`.
- Campi Anthropic presenti soltanto negli specialisti Claude.
- Policy `allow_implicit_invocation: false` presente soltanto negli specialisti OpenAI.
- Router model-invocabile in entrambi i target.
- Playbook generati byte-identici alla sorgente.
- Nessun `SKILL.md` annidato nelle reference del router.
- Radice degli ZIP corretta e nessuna cartella esterna aggiuntiva.
- Integrità di entrambi gli ZIP verificata con `unzip -t`.

Il validatore OpenAI non viene applicato al frontmatter Claude perché rifiuta correttamente i campi specifici Anthropic `disable-model-invocation` e `argument-hint`. Il verifier del probe controlla separatamente presenza, posizione e isolamento di questi campi.

## Archivi

| Target | File | SHA-256 | Dimensione |
|---|---|---|---:|
| OpenAI | `ams-probe-openai-v0.0.1.zip` | `7c0b3887d34a889e3ed26c86d2f996b2f91a5af506e7abe3c7ea09622dcc603a` | 7.215 byte |
| Claude | `ams-probe-claude-v0.0.1.zip` | `b93e9f9dac06e9338215efa00081f5821fc39f04067892a13a5720464c120ba1` | 5.981 byte |

## Isolamento

Tutti i file creati appartengono a `prototypes/ams-probe/`. Nessuna skill, distribuzione o configurazione esistente è stata modificata, installata o sostituita.

