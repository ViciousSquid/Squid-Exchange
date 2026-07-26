from pathlib import Path
import re

ROOT = Path(__file__).parent.parent

README = ROOT / "README.md"
SQUIDS = ROOT / "squids"

START = "<!-- SQUID_CATALOGUE_START -->"
END = "<!-- SQUID_CATALOGUE_END -->"

cards = []

for folder in sorted(SQUIDS.iterdir()):

    if not folder.is_dir():
        continue

    readme = folder / "README.md"

    zip_file = next(folder.glob("*.zip"), None)

    if zip_file is None:
        continue

    description = ""

    if readme.exists():
        lines = readme.read_text(encoding="utf8").splitlines()

        for line in lines:
            line = line.strip()

            if line.startswith("#"):
                continue

            if line:
                description = line
                break

    if not description:
        description = "No description."

    card = f"""### 🦑 {folder.name}

{description}

**Download:** [{zip_file.name}]({zip_file.relative_to(ROOT).as_posix()})

---
"""

    cards.append(card)

catalogue = "\n".join(cards)

text = README.read_text(encoding="utf8")

pattern = re.compile(
    rf"{re.escape(START)}.*?{re.escape(END)}",
    flags=re.S,
)

replacement = f"""{START}

{catalogue}

{END}"""

text = pattern.sub(replacement, text)

README.write_text(text, encoding="utf8")
