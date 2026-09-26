"""Title every image in a folder (display only)."""

from pathlib import Path

from ollama import chat

MODEL = "gemma4:e2b"
IMAGE_DIR = Path("vision/images")
SUFFIXES = {".jpg", ".jpeg", ".png"}

for path in sorted(IMAGE_DIR.iterdir()):
    if path.suffix.lower() not in SUFFIXES:
        continue

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": "Give this image a short English title of about five words. Do not explain it.",
                "images": [str(path)],
            }
        ],
        options={"temperature": 0},
    )

    title = response.message.content.strip()
    print(f"{path.name}\t{title}")
