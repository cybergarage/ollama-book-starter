"""フォルダ内の画像にまとめてタイトルを付ける（表示のみ）。"""

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
                "content": "この画像の内容を、20文字程度の日本語のタイトルにしてください。説明は不要です。",
                "images": [str(path)],
            }
        ],
        options={"temperature": 0},
    )

    title = response.message.content.strip()
    print(f"{path.name}\t{title}")
