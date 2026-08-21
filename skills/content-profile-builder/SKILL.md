---
name: content-profile-builder
description: "Create, select, update, import, or export reusable content profiles containing editorial and visual direction. Use when a brand or client needs persistent rules for content without embedding them inside a content-production skill."
---

# Content Profile Builder

A content profile is separate from the skill: it is the user's versioned, portable context for recurring content work. It does not replace the broader company or brand identity created by `setup-business-context`.

## Profile lifecycle

First inspect the project for existing profiles and the applicable company or brand identity. If several profiles are available, present their names and purpose, then ask which one applies; never merge them automatically.

Create or update a profile only from confirmed material. Keep editorial direction and visual identity together when both are known, but leave fields empty rather than guessing logos, colors, fonts, CTA, or claims policy.

Store project-local profiles under `content-profiles/<profile-slug>.md` when possible. For portable distribution, export a clearly named Markdown or JSON representation only after validation. Preserve version history and add a short changelog entry for substantive changes.

## What belongs in a profile

- audience, editorial objective, positioning themes, and source standards;
- voice, tone, prohibited formulas, claim and attribution rules;
- preferred formats, CTA boundaries, accessibility requirements;
- approved palette, typography, logo and visual guidance when supplied.

Do not put client secrets, credentials, raw research, transient campaign decisions, or tool configuration in the profile.

## Handoff

State the exact profile name and version selected. Downstream skills use it as direction, but must still flag conflicts with supplied source material or the approved company or brand identity.

Use [the profile template](references/content-profile-template.md) for new profiles and for validating imports.
