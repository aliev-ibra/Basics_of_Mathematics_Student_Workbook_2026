"""Generate docs/data.js for the workbook dashboard from exercises/ and solutions/.

Run from the repository root:  python3 tools/build_site.py
Reads exercises/ and solutions/; writes docs/data.js and stamps its version into docs/index.html.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "data.js"

GROUP_NAMES = {"1_Algebra": "Algebra", "2_Geometry": "Geometry", "3_Calculus": "Calculus"}
HEADING = re.compile(r"^###\s+(?:Exercise|Problem)\s+(\d+)\.\s*(.*)$", re.M)


def set_title(text, fallback):
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else fallback


def parse_exercises(text):
    """Split an exercise file into intro + one entry per '### Exercise N.' block."""
    matches = list(HEADING.finditer(text))
    intro = text[: matches[0].start()] if matches else text
    items = []
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[m.end():end]
        # Drop section headings (e.g. "## More Challenging Exercises") that trail a block.
        level = "challenging" if re.search(r"^##\s+More (?:Challenging|Difficult)", text[: m.start()], re.M) else "basic"
        body = re.split(r"^##\s+", body, flags=re.M)[0].strip().rstrip("-").strip()
        items.append({"n": int(m.group(1)), "title": m.group(2).strip(), "body": body, "level": level})
    return intro.strip(), items


def main():
    sets = []
    for group_dir in sorted((ROOT / "exercises").iterdir()):
        if not group_dir.is_dir():
            continue
        for f in sorted(group_dir.glob("*_en.md")):
            slug = f.name[: -len("_en.md")]
            text = f.read_text(encoding="utf-8")
            intro, items = parse_exercises(text)
            sol_dir = ROOT / "solutions" / group_dir.name / slug
            for it in items:
                sol = sol_dir / f"problem_{it['n']:02d}_solution.md"
                content = sol.read_text(encoding="utf-8") if sol.exists() else ""
                it["solution"] = content.strip()
                it["written"] = bool(content.strip())
                it["solution_path"] = f"solutions/{group_dir.name}/{slug}/{sol.name}"
            sets.append({
                "id": f"{group_dir.name}/{slug}",
                "group": GROUP_NAMES.get(group_dir.name, group_dir.name),
                "slug": slug,
                "title": set_title(text, slug),
                "intro": intro,
                "problems": items,
            })
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("window.WORKBOOK = " + json.dumps(sets, ensure_ascii=False) + ";\n", encoding="utf-8")
    # Stamp a content hash on the data.js link so browsers and the Pages cache fetch fresh data after every rebuild.
    version = hashlib.sha1(OUT.read_bytes()).hexdigest()[:10]
    page = OUT.parent / "index.html"
    html = page.read_text(encoding="utf-8")
    page.write_text(re.sub(r'<script src="data\.js[^"]*">', f'<script src="data.js?v={version}">', html), encoding="utf-8")
    total = sum(len(s["problems"]) for s in sets)
    written = sum(p["written"] for s in sets for p in s["problems"])
    print(f"{len(sets)} sets, {total} problems, {written} written -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
