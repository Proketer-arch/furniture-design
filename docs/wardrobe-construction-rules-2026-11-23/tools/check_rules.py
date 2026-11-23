#!/usr/bin/env python3
"""Проверка базы правил проектирования корпусных шкафов (распашных и купе).

Запуск из каталога docs/wardrobe-construction-rules-2026-11-23:
    python3 -I tools/check_rules.py               # проверка
    python3 -I tools/check_rules.py --print-tables  # печать таблиц для вставки в Markdown

Что проверяется:
  1. rules.yaml читается; поля обязательны; идентификаторы RW-<ДОМЕН>-NN уникальны;
  2. теги достоверности допустимы; статус всегда «предложено»;
  3. все источники (src) описаны в 08-sources.md;
  4. ссылки на AFABRIK (K01–K19, W01–W13, C01–C12, поля ТЗ W-R/W-B/…) существуют;
  5. все примеры расчёта (calc) пересчитываются и совпадают с ожидаемым значением;
  6. все RW-правила, упомянутые в Markdown, есть в rules.yaml, и каждое правило упомянуто;
  7. упомянутые правила кухни R-<ДОМЕН>-NN существуют в базе кухни;
  8. все X-/D-/Q-идентификаторы описаны в 07-conflicts-and-questions.md;
  9. относительные ссылки между Markdown-файлами ведут на существующие файлы;
 10. rules-catalog.md соответствует rules.yaml (формируется tools/render_catalog.py);
 11. таблицы пролёта полок и ширины створок купе в Markdown совпадают с расчётом;
 12. правило с тегом «?» ссылается на вопрос владельцу Q-NN.
"""
import math
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
KITCHEN = ROOT.parent / "kitchen-construction-rules-2026-10-15" / "rules.yaml"
DOMAINS = ["DIM", "CAR", "INT", "SHF", "DRW", "SWG", "SLD", "ANT", "INS", "LAY"]
TAGS = {"Н", "П", "И", "Р", "?"}
REQUIRED = ["id", "title", "rule", "basis", "status", "src", "afabrik", "needs", "note"]
CALC_ENV = {"sqrt": math.sqrt, "ceil": math.ceil, "floor": math.floor, "min": min, "max": max, "round": round}
errors = []


def err(msg):
    errors.append(msg)


def afabrik_ok(ref):
    if re.fullmatch(r"W-[RBSZDIE]\d\d", ref):  # поля ТЗ шкафа (wardrobe-brief.md)
        return True
    m = re.fullmatch(r"([KWC])(\d\d)", ref)
    if not m:
        return False
    n = int(m.group(2))
    return {"K": 1 <= n <= 19, "W": 1 <= n <= 13, "C": 1 <= n <= 12}[m.group(1)]


# ---------- прогиб полки (RW-SHF-02) ----------
# Свободно лежащая полка под равномерной нагрузкой: f = 5·q·L⁴ / (384·E·I), I = b·t³/12, q = q_F·b.
# Предел прогиба ГОСТ 16371-2014, табл. 3: 5 мм на 1 м длины, то есть L/200 (RW-SHF-01).
# Нагрузки q_F — ГОСТ 19882-91, п. 1.6 (даН/м²). Глубина полки b сокращается: пролёт от неё не зависит.
E_LDSP = 2500        # МПа = Н/мм², консервативное значение модуля упругости ДСП (D-03)
DEPTH_SHELF = 500    # мм, ширина сечения полки (на результат не влияет)
LOADS = [("лёгкие вещи, головные уборы — 20 даН/м²", 20),
         ("бельё, одежда стопками, посуда — 60 даН/м²", 60),
         ("книги — 120 даН/м²", 120)]
THICK = [16, 18, 22, 25]
SPAN_STEP = 50


def deflection(L, t, q_daN_m2, b=DEPTH_SHELF, E=E_LDSP):
    """Прогиб в середине, мм. q — даН/м², переводится в Н/мм погонной нагрузки по ширине b."""
    q = q_daN_m2 * 10 * 1e-6 * b  # Н/мм
    I = b * t ** 3 / 12
    return 5 * q * L ** 4 / (384 * E * I)


def span_max(t, q):
    best = None
    for L in range(300, 2001, SPAN_STEP):
        if deflection(L, t, q) <= L / 200:
            best = L
    return best


def shelf_table():
    head = "| Нагрузка (ГОСТ 19882) \\ толщина ЛДСП | " + " | ".join(f"{t} мм" for t in THICK) + " |"
    sep = "|---|" + "---|" * len(THICK)
    rows = [f"| {label} | " + " | ".join(str(span_max(t, q)) for t in THICK) + " |" for label, q in LOADS]
    return "\n".join([head, sep] + rows)


# ---------- створки купе (RW-SLD-03) ----------
# Ширина створки: W_дв = (L_пр + k·p) / n, k — число перекрытий; пример — Aristo «Стандарт», профили C/O/I
# без шлегеля, p = 25 (AR-01). Высота створки при проёме 2600: H_дв = 2600 − 40 = 2560.
# Проверки: ширина 500–1500 (Aristo «Стандарт») и H:W не более 4:1 (рекомендуемо 3:1).
P_ARISTO = 25
H_DOOR = 2600 - 40
SLD_CASES = [(1200, 2, 1), (1600, 2, 1), (2000, 2, 1), (2400, 3, 2), (3000, 3, 2), (3600, 4, 2)]


def sliding_width(L, n, k, p=P_ARISTO):
    return (L + k * p) / n


def sliding_table():
    head = "| Проём L, мм | Створок n | Перекрытий k | Ширина створки, мм | H:W при H 2560 | 500–1500 и H:W ≤ 4 | H:W ≤ 3 |"
    sep = "|---|---|---|---|---|---|---|"
    rows = []
    for L, n, k in SLD_CASES:
        w = sliding_width(L, n, k)
        r = H_DOOR / w
        ok = "да" if 500 <= w <= 1500 and r <= 4 else "нет"
        rec = "да" if r <= 3 else "нет"
        rows.append(f"| {L} | {n} | {k} | {w:.1f} | {r:.2f} | {ok} | {rec} |")
    return "\n".join([head, sep] + rows)


TABLES = [
    ("03-interior.md", "shelf-table", shelf_table),
    ("05-sliding-doors.md", "sliding-table", sliding_table),
]


# ---------- основная проверка ----------
def main():
    if "--print-tables" in sys.argv:
        for name, tag, fn in TABLES:
            print(f"<!-- {tag}:begin --> ({name})\n{fn()}\n<!-- {tag}:end -->\n")
        return 0

    data = yaml.safe_load((ROOT / "rules.yaml").read_text(encoding="utf-8"))
    rules = data["rules"]

    sources_md = (ROOT / "08-sources.md").read_text(encoding="utf-8")
    source_ids = set(re.findall(r"^\|\s*([A-Z]{2}-\d\d)\s*\|", sources_md, flags=re.M))

    conflicts_md = (ROOT / "07-conflicts-and-questions.md").read_text(encoding="utf-8")
    defined_refs = set(re.findall(r"^\|\s*((?:X|D|Q)-\d\d)\s*\|", conflicts_md, flags=re.M))

    kitchen_ids = set()
    if KITCHEN.exists():
        kitchen_ids = {r["id"] for r in yaml.safe_load(KITCHEN.read_text(encoding="utf-8"))["rules"]}
    else:
        err(f"нет базы кухни {KITCHEN}")

    seen = set()
    for r in rules:
        rid = r.get("id", "?")
        for f in REQUIRED:
            if f not in r:
                err(f"{rid}: нет поля {f}")
        m = re.fullmatch(r"RW-([A-Z]{3})-(\d\d)", rid)
        if not m or m.group(1) not in DOMAINS:
            err(f"{rid}: неверный формат идентификатора")
        if rid in seen:
            err(f"{rid}: дубликат")
        seen.add(rid)
        if r.get("status") != "предложено":
            err(f"{rid}: статус должен быть «предложено»")
        if not r.get("basis"):
            err(f"{rid}: нет тегов достоверности")
        for t in r.get("basis", []):
            if t not in TAGS:
                err(f"{rid}: неизвестный тег {t}")
        if not r.get("src"):
            err(f"{rid}: нет источников")
        for s in r.get("src", []):
            if s not in source_ids:
                err(f"{rid}: источник {s} не описан в 08-sources.md")
        for a in r.get("afabrik", []) or []:
            if not afabrik_ok(a):
                err(f"{rid}: неизвестная ссылка AFABRIK {a}")
        text = " ".join(str(r.get(k, "")) for k in ("rule", "note", "needs"))
        for ref in re.findall(r"\b((?:X|D|Q)-\d\d)\b", text):
            if ref not in defined_refs:
                err(f"{rid}: ссылка {ref} не определена в 07-conflicts-and-questions.md")
        for kid in re.findall(r"(?<![\w-])(R-[A-Z]{3}-\d\d)\b", text):
            if kitchen_ids and kid not in kitchen_ids:
                err(f"{rid}: правило кухни {kid} не найдено")
        if "?" in r.get("basis", []) and not re.search(r"\bQ-\d\d\b", text):
            err(f"{rid}: тег «?» без вопроса владельцу Q-NN")
        for c in r.get("calc", []) or []:
            try:
                val = eval(c["expr"], {"__builtins__": {}}, {**CALC_ENV, **(c.get("vars") or {})})
            except Exception as e:  # noqa: BLE001
                err(f"{rid}: ошибка расчёта «{c.get('name')}»: {e}")
                continue
            if abs(val - c["expect"]) > 0.05:
                err(f"{rid}: расчёт «{c.get('name')}» дал {val}, ожидалось {c['expect']}")

    # Markdown
    mentioned = set()
    for p in sorted(ROOT.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        for rid in re.findall(r"\bRW-[A-Z]{3}-\d\d\b", text):
            mentioned.add(rid)
            if rid not in seen:
                err(f"{p.name}: упомянуто несуществующее правило {rid}")
        for kid in re.findall(r"(?<![\w-])(R-[A-Z]{3}-\d\d)\b", text):
            if kitchen_ids and kid not in kitchen_ids:
                err(f"{p.name}: правило кухни {kid} не найдено")
        for ref in re.findall(r"\b((?:X|D|Q)-\d\d)\b", text):
            if ref not in defined_refs:
                err(f"{p.name}: ссылка {ref} не определена в реестре 07")
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

    # расчётные таблицы
    for name, tag, fn in TABLES:
        md = (ROOT / name).read_text(encoding="utf-8")
        m = re.search(rf"<!-- {tag}:begin -->\n(.*?)\n<!-- {tag}:end -->", md, flags=re.S)
        if not m:
            err(f"{name}: нет блока {tag}")
        elif m.group(1).strip() != fn().strip():
            err(f"{name}: таблица {tag} не совпадает с расчётом (запустите --print-tables)")

    # сводка
    by_dom = {}
    for r in rules:
        d = r["id"].split("-")[1]
        by_dom[d] = by_dom.get(d, 0) + 1
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
