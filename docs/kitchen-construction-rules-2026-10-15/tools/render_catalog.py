#!/usr/bin/env python3
"""Формирует rules-catalog.md из rules.yaml.

Запуск из каталога docs/kitchen-construction-rules-2026-10-15:
    python3 -I tools/render_catalog.py          # записать rules-catalog.md
    python3 -I tools/render_catalog.py --check  # только проверить, что файл актуален
"""
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def flow(v):
    """Компактная запись параметров в виде YAML-потока."""
    return yaml.safe_dump(v, allow_unicode=True, default_flow_style=True, width=10**6).strip()


def render(data=None):
    if data is None:
        data = yaml.safe_load((ROOT / "rules.yaml").read_text(encoding="utf-8"))
    domains = data["meta"]["domains"]
    out = [
        "# Каталог правил",
        "",
        "Файл сформирован из `rules.yaml` скриптом `tools/render_catalog.py`; вручную не редактируется. "
        "Все правила имеют статус «предложено». Теги достоверности — в [00-method.md](00-method.md), "
        "источники — в [14-sources.md](14-sources.md), конфликты и открытые данные — в "
        "[13-conflicts-and-open-data.md](13-conflicts-and-open-data.md).",
        "",
    ]
    by_dom = {}
    for r in data["rules"]:
        by_dom.setdefault(r["id"].split("-")[1], []).append(r)
    out.append("## Оглавление")
    out.append("")
    for dom, title in domains.items():
        out.append(f"- **{dom}** — {title}: " + ", ".join(r["id"] for r in by_dom.get(dom, [])))
    out.append("")
    for dom, title in domains.items():
        out.append(f"## {dom} — {title}")
        out.append("")
        for r in by_dom.get(dom, []):
            out.append(f"### {r['id']} · {r['title']}")
            out.append("")
            out.append(f"- **Правило:** {r['rule']}")
            out.append(f"- **Достоверность:** {', '.join(r['basis'])} · **Статус:** {r['status']}")
            out.append(f"- **Источники:** {', '.join(r['src']) if r['src'] else '—'}")
            out.append(f"- **AFABRIK:** {', '.join(r['afabrik']) if r['afabrik'] else '—'}")
            out.append(f"- **Нужно для расчёта:** {', '.join(r['needs']) if r['needs'] else '—'}")
            if r.get("params"):
                out.append(f"- **Параметры:** `{flow(r['params'])}`")
            for c in r.get("calc", []) or []:
                vars_txt = ", ".join(f"{k}={v}" for k, v in (c.get("vars") or {}).items())
                out.append(f"- **Расчёт:** {c['name']}: `{c['expr']}`" + (f" при {vars_txt}" if vars_txt else "") + f" = {c['expect']}")
            out.append(f"- **Примечание:** {r['note']}")
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def main():
    text = render()
    path = ROOT / "rules-catalog.md"
    if "--check" in sys.argv:
        if not path.exists() or path.read_text(encoding="utf-8") != text:
            print("rules-catalog.md устарел: запустите tools/render_catalog.py")
            return 1
        print("rules-catalog.md актуален")
        return 0
    path.write_text(text, encoding="utf-8")
    print(f"записано {path.name}: {len(text)} символов")
    return 0


if __name__ == "__main__":
    sys.exit(main())
