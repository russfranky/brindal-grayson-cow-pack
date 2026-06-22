#!/usr/bin/env python3
"""Execute automated QA registry tests and update the canonical spreadsheet."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import sys
import zipfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = Path(__file__).resolve().parent / "QUALITY_REGISTRY.csv"
TODAY = date.today().isoformat()


class TestResult:
    def __init__(self, test_id: str, passed: bool, note: str = "", severity: str = ""):
        self.test_id = test_id
        self.passed = passed
        self.note = note
        self.severity = severity


def run_cmd(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd or ROOT, capture_output=True, text=True)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_level() -> dict:
    return json.loads((ROOT / "variants/cel-band/levels/sample_level.json").read_text())


def automated_tests() -> list[TestResult]:
    results: list[TestResult] = []
    sys.path.insert(0, str(ROOT / "variants/cel-band/scripts"))
    from convert_level import TILE_TO_MC, level_to_blocks, parse_origin  # noqa: E402

    # F008 Build
    build = run_cmd(["./scripts/build_pack.sh"])
    results.append(
        TestResult("TC-F008-001", build.returncode == 0, build.stderr.strip() or "build_pack.sh exit 0")
    )

    dist = ROOT / "dist/Cel_Band_Pack.mcpack"
    pack_src = ROOT / "variants/cel-band/pack"

    # F009 Assemble output exists
    results.append(TestResult("TC-F009-001", dist.is_file() and dist.stat().st_size >= 8000))

    # F010 Validate
    val = run_cmd(["python3", "scripts/validate_pack.py"])
    results.append(TestResult("TC-F010-001", val.returncode == 0, val.stderr.strip()))

    # F011 Converter
    level = load_level()
    blocks = level_to_blocks(level, (0, 100, 0))
    block_ids = {b[3] for b in blocks}
    results.append(TestResult("TC-F011-001", len(blocks) == 50, f"blocks={len(blocks)}"))
    results.append(TestResult("TC-F011-002", "cobblestone" in block_ids, "walls use cobblestone"))
    results.append(TestResult("TC-F011-003", TILE_TO_MC.get("sand") == "sand"))
    try:
        parse_origin("1,2")
        results.append(TestResult("TC-F011-004", False, "invalid origin accepted"))
    except ValueError:
        results.append(TestResult("TC-F011-004", True))

    dl = run_cmd(["python3", "convert_level.py"], cwd=ROOT / "download")
    results.append(
        TestResult("TC-F011-005", dl.returncode == 0, dl.stderr.strip() or "download bundle default paths")
    )

    # F012 Sample level (Archive 2 canonical: 11 tile types, 45 tiles)
    types = {t["type"] for t in level["tiles"]}
    archive2_types = {
        "floor_lit",
        "floor_light",
        "floor_dark",
        "floor_shadow",
        "wall",
        "wood",
        "leaves",
        "water",
        "gold_relic",
        "jade_relic",
        "bronze_relic",
    }
    results.append(TestResult("TC-F012-001", types == archive2_types, f"missing={archive2_types-types}"))
    results.append(TestResult("TC-F012-002", len(level["tiles"]) == 45, f"tiles={len(level['tiles'])}"))
    results.append(
        TestResult(
            "TC-F012-003",
            (ROOT / "download/sample_level.setblock").is_file()
            and "setblock" in (ROOT / "download/sample_level.setblock").read_text(),
        )
    )

    # F013 Version
    ver = run_cmd(["python3", "variants/cel-band/scripts/pack_version.py", "--print", "semver"])
    results.append(TestResult("TC-F013-001", ver.returncode == 0 and ver.stdout.strip().count(".") == 2))

    # F020 Bundle parity
    d2 = ROOT / "download/Cel_Band_Pack.mcpack"
    results.append(TestResult("TC-F020-001", dist.is_file() and d2.is_file() and sha256(dist) == sha256(d2)))
    results.append(TestResult("TC-F020-002", (ROOT / "download/Voxel_Spec.pdf").is_file()))
    results.append(TestResult("TC-F020-003", (ROOT / "download/convert_level.py").is_file()))
    results.append(
        TestResult(
            "TC-F020-004",
            len(list((pack_src / "textures/blocks").rglob("*.png"))) >= 15,
        )
    )

    preflight = run_cmd(["python3", "scripts/preflight_check.py"])
    results.append(TestResult("TC-F023-001", preflight.returncode == 0, "preflight PASS"))

    manifest = json.loads((pack_src / "manifest.json").read_text())
    text = (manifest["header"].get("name", "") + manifest["header"].get("description", "")).lower()

    # F021 Branding
    results.append(TestResult("TC-F021-001", "lara" not in text and "croft" not in text and "lc go" not in text))

    # F022 Version sync
    version_file = (ROOT / "variants/cel-band/VERSION").read_text().strip().split(".")
    results.append(
        TestResult("TC-F022-001", manifest["header"]["version"] == [int(x) for x in version_file])
    )

    with zipfile.ZipFile(dist) as zf:
        names = set(zf.namelist())
        zip_manifest = json.loads(zf.read("manifest.json"))

    # F009 Pack zip structure
    results.append(
        TestResult(
            "TC-F009-002",
            "pack_icon.png" in names and "textures/blocks/cobblestone.png" in names,
        )
    )

    # F024 Dirt texture
    results.append(TestResult("TC-F024-001", (pack_src / "textures/blocks/dirt.png").is_file()))

    # F025 Sand tile + texture
    results.append(TestResult("TC-F025-001", TILE_TO_MC.get("sand") == "sand"))
    results.append(TestResult("TC-F025-002", (pack_src / "textures/blocks/sand.png").is_file()))

    # F026 Wood/leaves environment
    wood_blocks = level_to_blocks({"tiles": [{"x": 0, "z": 0, "type": "wood"}]}, (0, 100, 0))
    wood_ids = {b[3] for b in wood_blocks}
    results.append(
        TestResult("TC-F026-001", wood_ids == {"oak_log", "leaves"}, f"wood_blocks={wood_ids}")
    )
    results.append(
        TestResult(
            "TC-F026-002",
            "textures/blocks/log_oak.png" in names and "textures/blocks/leaves_oak_opaque.png" in names,
        )
    )

    # F027 Water
    water_count = sum(1 for t in level["tiles"] if t["type"] == "water")
    results.append(TestResult("TC-F027-001", water_count == 2, f"water_tiles={water_count}"))
    results.append(TestResult("TC-F027-002", "textures/blocks/water_still_grey.png" in names))

    # F028 Multi-format converter output
    results.append(
        TestResult(
            "TC-F028-001",
            (ROOT / "download/diorama_level.mcfunction").is_file()
            and "setblock" in (ROOT / "download/diorama_level.mcfunction").read_text(),
        )
    )
    results.append(
        TestResult(
            "TC-F028-002",
            (ROOT / "download/diorama_blocks.py").is_file()
            and "BLOCKS = [" in (ROOT / "download/diorama_blocks.py").read_text(),
        )
    )

    # F030 Unknown tile fallback
    unknown = level_to_blocks({"tiles": [{"x": 0, "z": 0, "type": "mystery_tile"}]}, (0, 100, 0))
    results.append(TestResult("TC-F030-001", unknown[0][3] == "stone"))

    # F031 Pack icon
    results.append(TestResult("TC-F031-001", "pack_icon.png" in names))

    # F032 Manifest UUID / format
    results.append(
        TestResult(
            "TC-F032-001",
            zip_manifest.get("format_version") == 2
            and bool(zip_manifest.get("header", {}).get("uuid"))
            and bool(zip_manifest.get("modules", [{}])[0].get("uuid")),
        )
    )

    # F033 QA suite (self-check: registry writable)
    results.append(TestResult("TC-F033-001", REGISTRY.is_file() and REGISTRY.stat().st_size > 0))

    # F036 Pre-commit
    results.append(TestResult("TC-F036-001", (ROOT / ".pre-commit-config.yaml").is_file()))
    ruff = run_cmd(["python3", "-m", "ruff", "check", "variants/cel-band/scripts", "scripts", "qa"])
    results.append(TestResult("TC-F036-002", ruff.returncode == 0, ruff.stderr.strip()[:120]))

    # F038 PR template
    results.append(TestResult("TC-F038-001", (ROOT / ".github/pull_request_template.md").is_file()))

    # F039 Issue templates
    results.append(
        TestResult(
            "TC-F039-001",
            (ROOT / ".github/ISSUE_TEMPLATE/bug_report.md").is_file()
            and (ROOT / ".github/ISSUE_TEMPLATE/feature_request.md").is_file(),
        )
    )

    # F040 SKIP_BUMP
    publish_sh = (ROOT / "scripts/publish_pack.sh").read_text()
    results.append(TestResult("TC-F040-001", "SKIP_BUMP" in publish_sh))

    # F041 Publish loop prevention
    publish_yml = (ROOT / ".github/workflows/publish.yml").read_text()
    results.append(
        TestResult(
            "TC-F041-001",
            "paths-ignore:" in publish_yml and "dist/**" in publish_yml,
        )
    )

    # F042 CI artifact upload
    ci_yml = (ROOT / ".github/workflows/ci.yml").read_text()
    results.append(
        TestResult("TC-F042-001", "upload-artifact" in ci_yml and "Cel_Band_Pack" in ci_yml)
    )

    # F043 Voxel spec (existence)
    results.append(TestResult("TC-F043-001", (ROOT / "download/Voxel_Spec.pdf").is_file()))

    # F044 Trademark audit doc
    results.append(TestResult("TC-F044-001", (ROOT / "docs/TRADEMARK_AUDIT.md").is_file()))

    # F045 WORKFLOW.md
    results.append(TestResult("TC-F045-001", (ROOT / "docs/WORKFLOW.md").is_file()))

    # F046 License
    results.append(TestResult("TC-F046-001", (ROOT / "LICENSE").is_file()))

    # F047 Variant README
    results.append(TestResult("TC-F047-001", (ROOT / "variants/cel-band/README.md").is_file()))

    # F048 Assemble-time branding injection
    results.append(
        TestResult(
            "TC-F048-001",
            zip_manifest.get("header", {}).get("name") == "Cel Band Pack",
        )
    )

    # F049 TESTING.md
    results.append(TestResult("TC-F049-001", (ROOT / "TESTING.md").is_file()))

    clean = run_cmd(["./scripts/clean.sh"])
    results.append(TestResult("TC-F017-001", clean.returncode == 0))

    results.append(TestResult("TC-F014-001", (ROOT / ".github/workflows/ci.yml").is_file()))
    results.append(TestResult("TC-F015-001", (ROOT / ".github/workflows/publish.yml").is_file()))
    results.append(TestResult("TC-F016-001", (ROOT / ".github/workflows/release.yml").is_file()))
    results.append(
        TestResult(
            "TC-F019-001",
            (ROOT / "docs/development.md").is_file()
            and "variants/cel-band/pack" in (ROOT / "docs/development.md").read_text(),
        )
    )

    return results


def manual_pending() -> set[str]:
    """Tests that require Bedrock device or human verification."""
    return {
        "TC-F001-001",
        "TC-F001-002",
        "TC-F002-001",
        "TC-F003-001",
        "TC-F004-001",
        "TC-F004-002",
        "TC-F005-001",
        "TC-F006-001",
        "TC-F007-001",
        "TC-F012-004",
        "TC-F018-001",
        "TC-F034-001",
        "TC-F035-001",
    }


def load_registry() -> list[dict[str, str]]:
    with REGISTRY.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_registry(rows: list[dict[str, str]]) -> None:
    if not rows:
        return
    with REGISTRY.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def update_registry(results: list[TestResult]) -> tuple[int, int, int]:
    rows = load_registry()
    result_map = {r.test_id: r for r in results}
    manual = manual_pending()
    passed = failed = pending = 0

    for row in rows:
        tid = row["Test Case ID"]
        if tid in result_map:
            r = result_map[tid]
            row["Current Status"] = "PASS" if r.passed else "FAIL"
            row["Last Tested Date"] = TODAY
            if not r.passed:
                row["Defect Count"] = str(int(row.get("Defect Count") or 0) + 1)
                row["Severity"] = r.severity or row.get("Severity") or "High"
                row["Notes"] = r.note
                failed += 1
            else:
                row["Notes"] = r.note or row.get("Notes", "")
                passed += 1
        elif tid in manual:
            row["Current Status"] = row.get("Current Status") or "MANUAL_PENDING"
            pending += 1
        else:
            row["Current Status"] = row.get("Current Status") or "NOT_RUN"
            pending += 1

    save_registry(rows)
    return passed, failed, pending


def main() -> int:
    if not REGISTRY.is_file():
        print(f"Missing registry: {REGISTRY}", file=sys.stderr)
        return 1

    results = automated_tests()
    passed, failed, pending = update_registry(results)

    print(f"QA suite: {passed} passed, {failed} failed, {pending} manual/not-run")
    for r in results:
        status = "PASS" if r.passed else "FAIL"
        print(f"  [{status}] {r.test_id}: {r.note}")

    if failed:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
