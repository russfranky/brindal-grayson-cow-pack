# QA Coverage Report — Iteration 2

**Date:** 2026-06-22  
**Branch:** `cursor/qa-iteration-2-16b0`

## Exit criteria status

| Criterion | Status |
|-----------|--------|
| All features in spreadsheet | Yes — 49 features (F001–F049) |
| All test cases documented | Yes — 67 registry rows (54 unique automated/static IDs + 13 manual) |
| Automated tests executed | Yes — 54/54 pass |
| Manual Bedrock tests executed | No — 13 require device or doc review |
| All defects resolved or waived | Yes — D001–D002/D004–D005 fixed; D003 waived (Archive 2 sample) |
| Critical/high open defects | 0 automated failures |

**Completion declaration:** Not fully complete — manual in-game validation and doc-review test cases remain. All automatable exit criteria satisfied.

## Coverage summary

| Metric | Count |
|--------|------:|
| Features discovered | 49 |
| Registry rows (test cases) | 67 |
| Unique automated/static test IDs | 54 |
| Manual pending | 13 |
| Pass (automated/static) | 54 |
| Fail | 0 |

## Features tested (automated/static)

F008 Build · F009 Assembly · F010 Validation · F011 Conversion · F012 Sample level · F013 Version · F014 CI · F015 Publish · F016 Release · F017 Clean · F019 Dev docs · F020 Download bundle · F021 Branding · F022 Version sync · F023 Preflight · F024 Dirt · F025 Sand · F026 Wood/leaves · F027 Water · F028 Multi-format output · F030 Unknown tile · F031 Pack icon · F032 Manifest UUID · F033 QA suite · F036 Pre-commit · F038 PR template · F039 Issue templates · F040 SKIP_BUMP · F041 Publish loop · F042 CI artifact · F043 Voxel spec · F044 Trademark audit · F045 WORKFLOW · F046 License · F047 Variant README · F048 Branding injection · F049 TESTING.md

## Defects found and fixed (this iteration)

| ID | Issue | Resolution |
|----|-------|------------|
| D005 | Registry documented walls as stone; code uses cobblestone | Updated F004 expected behaviour and TC-F004-002 |
| — | D003 sand tile regression after Archive 2 | Waived — Archive 2 canonical sample has 11/12 types; sand supported by converter |

## Defects from prior iterations (closed)

| ID | Issue | Fix |
|----|-------|-----|
| D001 | Walls → cobblestone without texture | Archive 2 added cobblestone.png |
| D002 | download/convert_level.py default paths | Path resolution relative to script dir |
| D004 | Weak validate_pack checks | Texture coverage, hash parity, branding, version sync |

## Remaining risks

1. **In-game texture application** — F001–F007, F012-004, F018 not verified on Bedrock device.
2. **Item/UI overrides** — Bedrock may ignore some UI paths on certain versions.
3. **Voxel spec PDF** — existence verified; internal franchise terms not redacted (see TRADEMARK_AUDIT.md).
4. **Repo URL** — docs still link to `charles-world-of-chaos` GitHub name.
5. **WORKFLOW.md** — references removed procedural tool; current pipeline is commit-and-assemble.

## Confidence score

**82 / 100** (+4 from iteration 1)

- Automated pipeline, conversion, packaging, branding, registry coverage: **98%**
- In-game player experience: **40%** (untested on device)
- Documentation/compliance review: **60%** (F034/F035 manual pending)

## Next iteration

1. Execute 13 manual test cases on Bedrock device; update `qa/QUALITY_REGISTRY.csv`.
2. Redact franchise terms in `download/Voxel_Spec.pdf` per TRADEMARK_AUDIT.md.
3. Re-run `python3 qa/run_qa_suite.py` after any texture or converter change.
