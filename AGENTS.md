# NAVIR project guidance

## Project identity

- Address the user as “燃燃様々”.
- This is a fictional Beauty Tech / high-speed hairdryer portfolio project, not a production ecommerce application.
- Preserve the established direction: brand `NAVIR`, concept `FLOW`, slogan `Shape the Air.`, and visual balance of roughly 70% `AIR SCULPT` plus 30% `FLOW EDITORIAL`.
- Preserve the restrained palette documented in the project files. Burgundy is a controlled accent or one deliberate field, not decoration scattered across the page.
- Do not redefine the brand direction, add shopping-cart/account/payment features, or introduce showy motion unless the user explicitly changes the brief.

## Source of truth

- Read `HANDOFF.md` before starting work and update it before ending a meaningful work session.
- Treat `assets/` as source imagery, `work/` as editable generators, `deliverables/` as reviewable outputs, and `tmp/` as references or QA evidence.
- Preserve earlier accepted exports. Create a clearly versioned new file instead of overwriting an accepted deliverable unless the user explicitly asks for replacement.
- Keep scripts and documents on relative project paths whenever practical so the repository works on both company and home computers.

## Visual acceptance

- Evaluate the whole composition, rhythm, hierarchy, spacing, crop quality, and legibility; successful rendering alone is not acceptance.
- Prefer asymmetrical editorial layouts with active negative space, one dominant visual event, and sparse technical notation.
- Do not fill the page with generic cards, unnecessary interface chrome, decorative gradients, shadows, or excessive fine detail.
- When alternatives remain unapproved, label them as options and do not silently promote one to the final master.

## Validation and handoff

- Before editing, run `git status` and read the latest handoff entry.
- After editing, verify every changed export opens correctly and compare important dimensions against the intended format.
- Record changed files, validation performed, unresolved decisions, and the exact next action in `HANDOFF.md`.
- For company/home switching: pull before work, avoid simultaneous unpushed edits on both computers, then commit and push before switching machines.
