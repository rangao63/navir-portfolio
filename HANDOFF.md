# NAVIR handoff

Last updated: 2026-09-23

Original Codex task: `01a08935-6e79-72f3-a03e-ed9da387fe33`

Repository: `https://github.com/rangao63/navir-portfolio` (private)

Repository status: `main` is connected to `origin/main`; the initial portable project snapshot has been pushed.

## Fixed brief

- For a concise explanation of the active design, editable PSD requirement, file map, and conflicting historical tracks, read `PROJECT_BRIEF.md` first.

- Fictional high-speed hairdryer / Beauty Tech portfolio brand.
- Brand: `NAVIR`
- Core concept: `FLOW`
- Slogan: `Shape the Air.`
- Visual direction: approximately 70% `AIR SCULPT` + 30% `FLOW EDITORIAL`.
- Earlier brand/KV palette: warm white `#F4F2EF`, silver `#C8C8C4`, graphite `#202020`, pale grey `#DCDAD5`, burgundy `#6B1F32`. The active NAVIR S1 vertical A+ visual samples instead use blue/deep navy/cool white; keep these tracks distinct.
- This is a portfolio narrative and visual-system project. Do not add cart, account, order, payment, or backend scope.

## Current state

- Brand direction is fixed; do not restart naming or concept exploration.
- The active vertical seven-screen NAVIR S1 page has an editable v04 block layout and editable A01/A02 Photoshop visual samples in `portfolio/Amazon_APlus/`. A03-A07 completed visual pages are not confirmed in this repository. The user explicitly needs editable native sources, not only PNGs or scripts.
- The user selected `deliverables/NAVIR_PC_Template_GreyWhite_A_Airy.png` as the PC page structural baseline on 2026-09-22. This selects the layout direction, not a finished branded design.
- The user recalls receiving finished first and last NAVIR pages on the company computer. Their exact final files and approval status need to be reconciled with this clone before further page production.
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

1. On the home computer, pull the new commit and read `PROJECT_BRIEF.md`; show the user actual previews, not only filenames.
2. Identify the finished first and last pages the user recalls, especially any A07 final, and compare them with the recovered PSDs/PNGs and repository QA screenshots. Do not declare A07 complete from a wireframe or QA image.
3. Confirm whether the next requested production is the vertical seven-screen series or the separate PC A structure. For either, deliver a native editable source plus preview; do not silently change the established visuals.
4. Validate any new Adobe-generated sample visually in Adobe; script execution alone is not approval.

## Home review: 2026-09-22

- Pulled `main` with `git pull --ff-only`; it was already current and the working tree was clean.
- Reviewed the three full-size grey-white PC structure PNGs in `deliverables/`. A and C use the same section geometry; C uses a darker grey hierarchy. B reverses the main left/right composition. These remain unapproved structural options, not a final branded page.
- The user subsequently chose A as the starting structure. B and C remain comparison options. The status of the separate finished A01/A07 pages requires verification.
- Inspected the repository's `tmp/block_v04_A01_qa2.png` and `tmp/block_v03_A07_qa.png` as QA evidence only. Their placeholder product shapes and blue fields do not establish approval against the fixed NAVIR palette. The latest Illustrator workflow has not been run or verified on this computer.
- Changed file: `HANDOFF.md` only. No design or website files were edited and no site was published.
- Exact next action: reconcile the finished A01/A07 pages reported by the user before producing further pages. Then refine the selected A structure in a new versioned output and visually validate it.

## Home clarification: 2026-09-22

- The user's company-computer recollection establishes that the first and last pages may already be finished; do not recreate or dismiss them based only on the grey-white structure options.
- This clone tracks `tmp/block_v04_A01_qa2.png` and `tmp/block_v03_A07_qa.png`, among earlier A01/A07 QA screenshots. No A01/A07 final PNG or PSD was found in the tracked repository files.
- At the time of this home review, `build_navir_visual_sample_v01.jsx` and `audit_navir_visual_sample_v01.jsx` referenced a company-computer path and Photoshop PSD files absent from that clone. The scripts and QA screenshots did not establish which files were handed to the user as final; see the recovery entry below.
- Changed file: `HANDOFF.md` only. No design files were altered and no site was published.

## Company file recovery: 2026-09-23

- Recovered the complete 44-file NAVIR A+ portfolio folder from the company desktop into `portfolio/Amazon_APlus/`, preserving its original subfolders (`Assets`, `Copy`, `Exports`, `Layout_Approval`, `Preview`, `Review_v01`, `Source`, and `Visual_Sample_v01`).
- This includes editable A01/A02 PSDs in `Visual_Sample_v01/`, earlier A+ PSDs in `Source/`, and four versioned vertical block-layout PSDs in `Layout_Approval/`. Source and repository copies matched by SHA-256 for all 44 files.
- These recovered files were missing from the earlier GitHub snapshot. The original desktop folder was retained as a safety copy; use the GitHub repository as the cross-computer source of truth after the push is verified.
- The recovered folder contains A01/A02 visual samples and A01/A02 A+ exports, plus vertical layout versions. It does not by itself prove which file, if any, was approved as the final A07 page. Ask the user to identify the specific final A07 if needed; do not recreate it silently.
- Next on the home computer: `git pull --ff-only` in this repository, then inspect `portfolio/Amazon_APlus/` before further design work.

## A01 Chinese composition preview: 2026-09-23

- At the user's request, used `portfolio/Amazon_APlus/Visual_Sample_v01/NAVIR_S1_A01_Hero_CN_v01.png` as the edit target and a user-provided annotated vacuum-page screenshot only as a layout reference. Its annotations, vacuum imagery, English promotion, and email signup were not copied.
- New review option: `portfolio/Amazon_APlus/Visual_Sample_v02/NAVIR_S1_A01_Hero_CN_v02_preview.png`. It stacks an outlet/airflow detail above the full NAVIR S1 product, then places Chinese product name, selling points, and a search-style call to action below. Copy: “NAVIR S1 高速吹风机”, “让气流塑形。”, “定向气流 · 温和控温 · 轻盈握持”, “探索 NAVIR S1”, and “了解更多”. No numerical performance claims appear in this version.
- The built-in image-generation edit produced a flattened raster preview at 821 × 1916 px. The original A01 PNG and editable PSD remain unchanged; this preview is not a production-size layered PSD or an accepted final master. The A+ sample's blue/navy visual language was retained for continuity; this does not revise the separate overall NAVIR brand brief.
- Validation: opened the saved PNG, checked the two product zones and Chinese copy visually, verified its portrait aspect ratio matches the original approximately, and kept it under a new versioned path. A02 and the unconfirmed A07 were not changed.
- Exact next action: get the user's visual feedback on v02; if selected, rebuild or refine the layout in a full-size editable source and verify text, product silhouette, crop, and export at the intended format before acceptance.

## A01 front-facing v04 review sample: 2026-09-23

- User-approved direction for this iteration: NAVIR S1 outlet faces the viewer as a near circle; the earlier stronger three-quarter/low-angle candidate was rejected. Keep two buttons, full handle, short cable fading downward, blue airflow behind the product, a restrained precision turbine, centered Chinese title with a white/blue S1 plate, titanium CTA, and a Chinese channel strip including NAVIR 官网, Amazon, and MediaMarkt.
- New review files: `portfolio/Amazon_APlus/Visual_Sample_v04/NAVIR_S1_A01_Hero_CN_v04_preview.png` and `NAVIR_S1_A01_Hero_CN_v04.psd`, both 1464 × 3416 px. The product source and independently rendered background, airflow, turbine, UI, and text-reference layers are in `Visual_Sample_v04/Assets/`. Source builders are `work/build_navir_a01_v04_assets.py`, `work/build_navir_a01_v04_psd.py`, and an unexecuted Photoshop JSX option `work/build_navir_a01_v04.jsx`.
- PSD inspection with `psd-tools`: seven groups, 11 native type layers, one replaceable embedded product smart object. Its visible composite matched the PNG preview pixel for pixel. The editable type group is initially hidden behind a visible raster text reference to keep the review composite stable; hide the reference and show the type group when editing text.
- Photoshop 2023 was found and launched on the home computer, but Adobe displayed an unlicensed-app notice. Native Photoshop open/edit/export validation could not be completed. `psd-tools` also logged engine-data parsing warnings for the type layers, so actual Chinese text rendering and editing in Photoshop remain **unverified**. Do not mark this v04 sample as a final accepted PSD until it has been opened and checked in a licensed Photoshop session.
- A01 v01/v02 and A02 remain unchanged; A03-A07 were not worked on. The earlier untracked v03 exploratory files on this computer remain local and are not the selected v04 direction. No website was published.
- Exact next action: ask the user to review the v04 PNG composition. On a licensed Photoshop instance, open the v04 PSD, verify product smart-object replacement and every Chinese text layer, repair native type if needed, re-export the PNG, then seek visual acceptance before promoting A01 to final.

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
