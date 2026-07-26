import os
import glob

SQUIDS_DIR = "squids"
README_PATH = "README.md"

def get_specimens():
    specimens = []
    if not os.path.exists(SQUIDS_DIR):
        return specimens

    # Iterate through folders inside /squids
    for item in sorted(os.listdir(SQUIDS_DIR)):
        item_path = os.path.join(SQUIDS_DIR, item)
        if os.path.isdir(item_path):
            # Check for inner contents (like zip files or sub-files)
            zip_files = glob.glob(os.path.join(item_path, "*.zip"))
            specimens.append({
                "name": item,
                "has_zip": len(zip_files) > 0,
                "path": f"{SQUIDS_DIR}/{item}"
            })
    return specimens

def generate_markdown(specimens):
    content = ["# Squid Exchange\n", "Welcome to the Squid Exchange repository.\n"]
    content.append("## Specimens\n")

    if not specimens:
        content.append("_No specimens currently available in the catalogue._\n")
    else:
        content.append("| Specimen | Path | Archive Included |")
        content.append("| :--- | :--- | :---: |")
        for spec in specimens:
            has_zip_str = "Yes" if spec["has_zip"] else "No"
            content.append(f"| **{spec['name']}** | [`{spec['path']}`]({spec['path']}) | {has_zip_str} |")
        content.append("")

    return "\n".join(content)

def main():
    specimens = get_specimens()
    readme_content = generate_markdown(specimens)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme_content)

    print(f"Successfully updated {README_PATH} with {len(specimens)} specimen(s).")

if __name__ == "__main__":
    main()
