"""Title images in a folder and save the results to CSV.

This version of folder.py writes each result and skips images already processed.
"""

import csv
from pathlib import Path

from ollama import chat

MODEL = "gemma4:e2b"
IMAGE_DIR = Path("vision/images")
OUTPUT_FILE = Path("titles.csv")
SUFFIXES = {".jpg", ".jpeg", ".png"}
PROMPT = "Give this image a short English title of about five words. Do not explain it."


def load_done(path: Path) -> set[str]:
    """Read the names of images already processed."""
    if not path.exists():
        return set()
    with open(path, encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)
        return {row[0] for row in reader if row}


def make_title(path: Path) -> str:
    response = chat(
        model=MODEL,
        messages=[{"role": "user", "content": PROMPT, "images": [str(path)]}],
        options={"temperature": 0},
    )
    return response.message.content.strip()


done = load_done(OUTPUT_FILE)
is_new = not OUTPUT_FILE.exists()

with open(OUTPUT_FILE, "a", encoding="utf-8-sig", newline="") as file:
    writer = csv.writer(file)
    if is_new:
        writer.writerow(["File name", "Title"])

    for path in sorted(IMAGE_DIR.iterdir()):
        if path.suffix.lower() not in SUFFIXES:
            continue
        if path.name in done:
            print(f"{path.name}\t(skipped because it was already processed)")
            continue

        title = make_title(path)
        print(f"{path.name}\t{title}")
        writer.writerow([path.name, title])
        file.flush()

print(f"\nSaved to {OUTPUT_FILE}.")
