#!/usr/bin/env python3
"""Проверка базы правил проектирования кухни.

Запуск из каталога docs/kitchen-construction-rules-2026-10-15:
    python3 -I tools/check_rules.py            # проверка
    python3 -I tools/check_rules.py --print-table   # печать таблицы NL для вставки в 04-drawers.md

Что проверяется:
  1. rules.yaml читается; поля обязательны; идентификаторы уникальны и соответствуют домену;
  2. теги достоверности допустимы; статус всегда «предложено»;
  3. все идентификаторы источников (src) есть в 14-sources.md;
  4. ссылки на AFABRIK (K01–K19, W01–W13, C01–C12) существуют;
  5. все примеры расчёта (calc) пересчитываются и совпадают с ожидаемым значением;
  6. все идентификаторы правил, упомянутые в Markdown, есть в rules.yaml, и каждое правило упомянуто;
  7. все X-/D-/Q-идентификаторы из правил и текстов описаны в 13-conflicts-and-open-data.md;
  8. относительные ссылки между Markdown-файлами ведут на существующие файлы;
  9. rules-catalog.md соответствует rules.yaml (формируется tools/render_catalog.py);
 10. таблица максимального NL в 04-drawers.md совпадает с расчётом.
"""
import math
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOMAINS = ["DIM", "CAR", "FRN", "HNG", "DRW", "LFT", "MOD", "JNC", "ISL", "GLA", "LAY", "SUP", "ASM"]
TAGS = {"Н", "П", "И", "Р", "?"}
REQUIRED = ["id", "title", "rule", "basis", "status", "src", "afabrik", "needs", "note"]
errors = []


def err(msg):
    errors.append(msg)


def afabrik_ok(ref):
    m = re.fullmatch(r"([KWC])(\d\d)", ref)
    if not m:
        return False
    n = int(m.group(2))
    return {"K": 1 <= n <= 19, "W": 1 <= n <= 13, "C": 1 <= n <= 12}[m.group(1)]


# ---------- таблица максимального NL ----------
SERIES = {
    "LEGRABOX": [270, 300, 350, 400, 450, 500, 550, 600, 650],
    "TANDEMBOX": [270, 300, 350, 400, 450, 500, 550, 600, 650],
    "Atira": [260, 300, 350, 420, 470, 520, 620],
    "ArciTech": [270, 300, 350, 400, 450, 500, 550, 650],
}
SYSTEMS = [
    ("Blum LEGRABOX (Δ=3)", "LEGRABOX", 3),
    ("Blum TANDEMBOX antaro (Δ=3)", "TANDEMBOX", 3),
    ("Hettich Atira, ящик (Δ=15)", "Atira", 15),
    ("Hettich Atira, внутр. ящик (Δ=24)", "Atira", 24),
    ("Hettich ArciTech (Δ=21, консервативно)", "ArciTech", 21),
    ("Hettich ArciTech (Δ=3, лучший случай)", "ArciTech", 3),
]
SCENARIOS = [
    ("нижний 560, задняя накладная", 560, 0),
    ("нижний 560, задняя в пазу", 560, 20),
    ("Gola 575, задняя накладная", 575, 0),
    ("Gola 575, задняя в пазу", 575, 20),
    ("верхний 320, задняя накладная", 320, 0),
    ("верхний 320, задняя в пазу", 320, 20),
]


def nl_max(series, delta, lt):
    ok = [n for n in series if n + delta <= lt]
    return max(ok) if ok else None


def nl_table():
    head = "| Система \\ Корпус | " + " | ".join(f"{n} (LT {d - k})" for n, d, k in SCENARIOS) + " |"
    sep = "|---|" + "---|" * len(SCENARIOS)
    rows = []
    for label, key, delta in SYSTEMS:
        cells = []
        for _, d, k in SCENARIOS:
            v = nl_max(SERIES[key], delta, d - k)
            cells.append("—" if v is None else str(v))
        rows.append(f"| {label} | " + " | ".join(cells) + " |")
    return "\n".join([head, sep] + rows)


# ---------- основная проверка ----------
def main():
    if "--print-table" in sys.argv:
        print(nl_table())
        return 0

    data = yaml.safe_load((ROOT / "rules.yaml").read_text(encoding="utf-8"))
    rules = data["rules"]

    sources_md = (ROOT / "14-sources.md").read_text(encoding="utf-8")
    source_ids = set(re.findall(r"^\|\s*([A-Z]{2}-\d\d)\s*\|", sources_md, flags=re.M))

    conflicts_md = (ROOT / "13-conflicts-and-open-data.md").read_text(encoding="utf-8")
    defined_refs = set(re.findall(r"^\|\s*((?:X|D|Q)-\d\d)\s*\|", conflicts_md, flags=re.M))

    seen = set()
    for r in rules:
        rid = r.get("id", "?")
        for f in REQUIRED:
            if f not in r:
                err(f"{rid}: нет поля {f}")
        m = re.fullmatch(r"R-([A-Z]{3})-(\d\d)", rid)
        if not m or m.group(1) not in DOMAINS:
            err(f"{rid}: неверный формат идентификатора")
        if rid in seen:
            err(f"{rid}: дубликат")
        seen.add(rid)
        if r.get("status") != "предложено":
            err(f"{rid}: статус должен быть «предложено»")
        for t in r.get("basis", []):
            if t not in TAGS:
                err(f"{rid}: неизвестный тег {t}")
        for s in r.get("src", []):
            if s not in source_ids:
                err(f"{rid}: источник {s} не описан в 14-sources.md")
        for a in r.get("afabrik", []) or []:
            if not afabrik_ok(a):
                err(f"{rid}: неизвестная ссылка AFABRIK {a}")
        for ref in re.findall(r"\b((?:X|D|Q)-\d\d)\b", " ".join(str(r.get(k, "")) for k in ("rule", "note", "needs"))):
            if ref not in defined_refs:
                err(f"{rid}: ссылка {ref} не определена в 13-conflicts-and-open-data.md")
        for c in r.get("calc", []) or []:
            try:
                val = eval(c["expr"], {"__builtins__": {}}, {**c.get("vars", {}), "sin": math.sin, "radians": math.radians, "floor": math.floor})
            except Exception as e:  # noqa: BLE001
                err(f"{rid}: ошибка расчёта «{c.get('name')}»: {e}")
                continue
            if abs(val - c["expect"]) > 0.01:
                err(f"{rid}: расчёт «{c.get('name')}» дал {val}, ожидалось {c['expect']}")

    # Markdown
    md_files = sorted(p for p in ROOT.glob("*.md"))
    mentioned = set()
    for p in md_files:
        text = p.read_text(encoding="utf-8")
        for rid in re.findall(r"\bR-[A-Z]{3}-\d\d\b", text):
            mentioned.add(rid)
            if rid not in seen:
                err(f"{p.name}: упомянуто несуществующее правило {rid}")
        for ref in re.findall(r"\b((?:X|D|Q)-\d\d)\b", text):
            if ref not in defined_refs and p.name != "13-conflicts-and-open-data.md":
                err(f"{p.name}: ссылка {ref} не определена в реестре 13")
        for link in re.findall(r"\]\(([^)]+)\)", text):
            if link.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = (p.parent / link.split("#")[0]).resolve()
            if not target.exists():
                err(f"{p.name}: битая ссылка {link}")
    for rid in sorted(seen - mentioned):
        err(f"{rid}: правило не упомянуто ни в одном Markdown-файле")

    # каталог правил
    sys.path.insert(0, str(ROOT / "tools"))
    import render_catalog  # noqa: E402

    cat = ROOT / "rules-catalog.md"
    if not cat.exists() or cat.read_text(encoding="utf-8") != render_catalog.render(data):
        err("rules-catalog.md отсутствует или устарел (запустите tools/render_catalog.py)")

    # таблица NL
    drawers = (ROOT / "04-drawers.md").read_text(encoding="utf-8")
    m = re.search(r"<!-- nl-table:begin -->\n(.*?)\n<!-- nl-table:end -->", drawers, flags=re.S)
    if not m:
        err("04-drawers.md: нет блока nl-table")
    elif m.group(1).strip() != nl_table().strip():
        err("04-drawers.md: таблица NL не совпадает с расчётом (запустите --print-table)")

    # сводка
    by_dom = {}
    for r in rules:
        by_dom[r["id"].split("-")[1]] = by_dom.get(r["id"].split("-")[1], 0) + 1
    n_calc = sum(len(r.get("calc", []) or []) for r in rules)
    print(f"правил: {len(rules)}; расчётных примеров: {n_calc}; по доменам: {by_dom}")
    if errors:
        print(f"ОШИБКИ ({len(errors)}):")
        for e in errors:
            print(" -", e)
        return 1
    print("OK: ошибок нет")
    return 0


if __name__ == "__main__":
    sys.exit(main())
