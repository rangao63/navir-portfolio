# NAVIR handoff

Last updated: 2026-09-22

Original Codex task: `01a08935-6e79-72f3-a03e-ed9da387fe33`

Repository: `https://github.com/rangao63/navir-portfolio` (private)

Repository status: `main` is connected to `origin/main`; the initial portable project snapshot has been pushed.

## Fixed brief

- Fictional high-speed hairdryer / Beauty Tech portfolio brand.
- Brand: `NAVIR`
- Core concept: `FLOW`
- Slogan: `Shape the Air.`
- Visual direction: approximately 70% `AIR SCULPT` + 30% `FLOW EDITORIAL`.
- Palette: warm white `#F4F2EF`, silver `#C8C8C4`, graphite `#202020`, pale grey `#DCDAD5`, burgundy `#6B1F32`.
- This is a portfolio narrative and visual-system project. Do not add cart, account, order, payment, or backend scope.

## Current state

- Brand direction is fixed; do not restart naming or concept exploration.
- The user selected `deliverables/NAVIR_PC_Template_GreyWhite_A_Airy.png` as the PC page structural baseline on 2026-09-22. This selects the layout direction, not a finished branded design.
- Recent Illustrator helper scripts were modified on 2026-09-21. Their visual result still needs to be judged in the intended Adobe workflow before being treated as accepted.

## Key editable sources

- `navir-visual-philosophy.md`
- `navir-visual-philosophy-v2.md`
- `navir-color-philosophy.md`
- `navir-pc-template-philosophy.md`
- `work/render_color_directions.py`
- `work/render_navir_v1.py`
- `work/render_navir_v2.py`
- `work/render_pc_detail_template.py`
- `build_navir_visual_sample_v01.jsx`
- `audit_navir_visual_sample_v01.jsx`
- `create_navir_3q_cutout.jsx`
- `create_navir_3q_polygon_cutout.jsx`
- `create_navir_3q_screen_asset.jsx`
- `assets/fonts/` contains the exact OFL-licensed fonts used by the Python renderers, so renders do not depend on a machine-specific Codex skill path.

## Reviewable outputs

- `deliverables/NAVIR_Brand_Board_1.0.png`
- `deliverables/NAVIR_Brand_Board_1.1_ColorField.png`
- `deliverables/NAVIR_BrandBoard_KV01_v1.pdf`
- `deliverables/NAVIR_Color_Directions_01.png`
- `deliverables/NAVIR_KV01_SHAPE_THE_AIR_v1.png`
- `deliverables/NAVIR_KV01_SHAPE_THE_AIR_v2_ColorField.png`
- `deliverables/NAVIR_PC_Detail_Template_BW_v1.png`
- `deliverables/NAVIR_PC_Template_GreyWhite_A_Airy.png`
- `deliverables/NAVIR_PC_Template_GreyWhite_B_Reverse.png`
- `deliverables/NAVIR_PC_Template_GreyWhite_C_Technical.png`

## Next action

1. Refine structure A in a new versioned output, preserving the current A/B/C exports.
2. Review the refinement at full size before treating it as an accepted branded page.
3. Validate the latest Illustrator-generated sample visually in Adobe; script execution alone is not approval.

## Home review: 2026-09-22

- Pulled `main` with `git pull --ff-only`; it was already current and the working tree was clean.
- Reviewed the three full-size grey-white PC structure PNGs in `deliverables/`. A and C use the same section geometry; C uses a darker grey hierarchy. B reverses the main left/right composition. These remain unapproved structural options, not a final branded page.
- The user subsequently chose A as the starting structure. B and C remain comparison options; no branded page has been approved.
- Inspected the repository's `tmp/block_v04_A01_qa2.png` and `tmp/block_v03_A07_qa.png` as QA evidence only. Their placeholder product shapes and blue fields do not establish approval against the fixed NAVIR palette. The latest Illustrator workflow has not been run or verified on this computer.
- Changed file: `HANDOFF.md` only. No design or website files were edited and no site was published.
- Exact next action: refine the selected A structure in a new versioned output and visually validate it. Independently validate the latest Illustrator-generated sample in Adobe before acceptance.

## Migration validation

- Python renderers now resolve the repository root from their own file location instead of `D:\codex用\NAVIR`.
- Required Instrument Sans and DM Mono font files plus their OFL licenses are stored in `assets/fonts/`.
- All four Python renderers executed successfully after the portability change.
- Every PNG renderer output remained byte-identical.
- The PDF generator now uses deterministic metadata; two consecutive renders produced the same SHA-256.

## Cross-computer routine

1. Start: `git pull --ff-only`, then `git status`.
2. Work on only one computer at a time.
3. End: update this file, commit all intended changes, and push.
4. Only start on the other computer after the push succeeds.
