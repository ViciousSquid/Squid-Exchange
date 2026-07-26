import os
import glob

SQUIDS_DIR = "squids"
README_PATH = "README.md"

def get_specimens():
    specimens = []
    if not os.path.exists(SQUIDS_DIR):
        return specimens

    for item in sorted(os.listdir(SQUIDS_DIR)):
        item_path = os.path.join(SQUIDS_DIR, item)
        if os.path.isdir(item_path):
            zip_files = glob.glob(os.path.join(item_path, "*.zip"))
            specimens.append({
                "name": item,
                "has_zip": len(zip_files) > 0,
                "path": f"{SQUIDS_DIR}/{item}"
            })
    return specimens

def generate_markdown(specimens):
    lines = [
        "# 🦑 Squid Exchange\n",
        "Welcome to the public ocean.\n",
        "Every specimen in this repository is a complete exported [Dosidicus](https://github.com/ViciousSquid/Dosidicus) mind.\n",
        "Browse them.\n",
        "Adopt them.\n",
        "Continue their stories.\n",
        "## Specimens\n"
    ]

    if not specimens:
        lines.append("_No specimens currently available in the catalogue._\n")
    else:
        lines.append("| Specimen | Path | Archive |")
        lines.append("| :--- | :--- | :---: |")
        for spec in specimens:
            has_zip_str = "Yes" if spec["has_zip"] else "No"
            lines.append(f"| **{spec['name']}** | [`{spec['path']}`]({spec['path']}) | {has_zip_str} |")
        lines.append("")

    return "\n".join(lines)

def main():
    specimens = get_specimens()
    readme_content = generate_markdown(specimens)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme_content)

    print(f"Successfully updated {README_PATH} with {len(specimens)} specimen(s).")

if __name__ == "__main__":
    main()
