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
 10. таблица максимального NL в 04-drawers.md совпадает с расчётом;
 11. таблицы LT_min Atira в rules.yaml и в скрипте совпадают.
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
STD_NL = [270, 300, 350, 400, 450, 500, 550, 600, 650]
# Минимальная глубина корпуса Atira по каталогу (R-DRW-05): NL -> LT_min
ATIRA_BOX = {260: 279, 300: 315, 350: 365, 420: 435, 470: 485, 520: 535, 620: 635}
ATIRA_INNER = {260: 288, 300: 324, 350: 374, 420: 444, 470: 494, 520: 544, 620: 644}


def plus(delta):
    return lambda nl: nl + delta


# (подпись, ряд NL, функция LT_min(NL)); ряд NL у Blum, Atira, ArciTech и DB9891 дан документами,
# у MERIVOBOX, Grass и Unihopper шаги внутри диапазона приняты стандартными (проверять по таблице производителя)
SYSTEMS = [
    ("Blum LEGRABOX (Δ=3)", STD_NL, plus(3)),
    ("Blum TANDEMBOX antaro (Δ=3)", STD_NL, plus(3)),
    ("Blum MERIVOBOX, M (Δ=3)", [270, 300, 350, 400, 450, 500, 550, 600], plus(3)),
    ("Hettich Atira, ящик (таблица каталога)", sorted(ATIRA_BOX), lambda nl: ATIRA_BOX[nl]),
    ("Hettich Atira, внутр. ящик (таблица каталога)", sorted(ATIRA_INNER), lambda nl: ATIRA_INNER[nl]),
    ("Hettich ArciTech, ящик (Δ=3)", [270, 300, 350, 400, 450, 500, 550, 650], plus(3)),
    ("Hettich ArciTech, внутр. ящик (Δ=12)", [270, 300, 350, 400, 450, 500, 550, 650], plus(12)),
    ("Hettich ArciTech, внутр. Push to open Silent (Δ=21)", [270, 300, 350, 400, 450, 500, 550, 650], plus(21)),
    ("Grass Nova Pro Scala (Δ=3)", STD_NL, plus(3)),
    ("Grass Nova Pro Scala, внутр. ящик (Δ=12)", STD_NL, plus(12)),
    ("Unihopper Magic Box / POBOX (Δ=5)", [270, 300, 350, 400, 450, 500, 550], plus(5)),
    ("Boyard DB9891 (Δ=3)", [400, 450, 500], plus(3)),
]
DELTA_G = 27  # профиль Gola: ширина 26 + выступ 1 (R-GLA-03)
# D_полн нижнего модуля = 550 (столешница 600, 50 до стены, свес 0; R-DIM-02);
# D_корп = 550 − t_фасада (− выступ профиля 1 для GOL); таблица считается для фасада 18
D_HND = 550 - 18       # 532
D_GOL = 550 - 18 - 1   # 531
# (подпись, D_корп, k_зад, δ_G)
SCENARIOS = [
    ("нижний HND, задняя накладная", D_HND, 0, 0),
    ("нижний HND, задняя в пазу", D_HND, 20, 0),
    ("нижний GOL, задняя накладная", D_GOL, 0, DELTA_G),
    ("нижний GOL, задняя в пазу", D_GOL, 20, DELTA_G),
    ("верхний 320, задняя накладная", 320, 0, 0),
    ("верхний 320, задняя в пазу", 320, 20, 0),
]


def nl_max(nl_list, lt_func, lt):
    ok = [n for n in nl_list if lt_func(n) <= lt]
    return max(ok) if ok else None


def nl_table():
    def head_cell(label, d, k, g):
        lt = d - k - g
        note = f"LT {d - k}" if not g else f"LT {d - k} − δ_G {g} = {lt}"
        return f"{label} ({note})"

    head = "| Система \\ Корпус | " + " | ".join(head_cell(*s) for s in SCENARIOS) + " |"
    sep = "|---|" + "---|" * len(SCENARIOS)
    rows = []
    for label, nl_list, lt_func in SYSTEMS:
        cells = []
        for _, d, k, g in SCENARIOS:
            v = nl_max(nl_list, lt_func, d - k - g)
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

    # таблицы LT_min Atira в rules.yaml и в скрипте совпадают
    atira = next((r for r in rules if r["id"] == "R-DRW-05"), None)
    if atira:
        pr = atira.get("params", {})
        for key, ref in (("LT_min_ящик", ATIRA_BOX), ("LT_min_внутр", ATIRA_INNER)):
            got = {int(k): v for k, v in (pr.get(key) or {}).items()}
            if got != ref:
                err(f"R-DRW-05: {key} в rules.yaml не совпадает с таблицей скрипта")

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
