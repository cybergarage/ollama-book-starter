"""フォルダ内の画像にタイトルを付け、CSVへ保存する。

02_folder.py に、1件ごとの書き込みと処理済みの飛ばしを加えた版です。
"""

import csv
from pathlib import Path

from ollama import chat

MODEL = "gemma4:e2b"
IMAGE_DIR = Path("vision/images")
OUTPUT_FILE = Path("titles.csv")
SUFFIXES = {".jpg", ".jpeg", ".png"}
PROMPT = "この画像の内容を、20文字程度の日本語のタイトルにしてください。説明は不要です。"


def load_done(path: Path) -> set[str]:
    """すでに処理したファイル名を読み込む。"""
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
        writer.writerow(["ファイル名", "タイトル"])

    for path in sorted(IMAGE_DIR.iterdir()):
        if path.suffix.lower() not in SUFFIXES:
            continue
        if path.name in done:
            print(f"{path.name}\t(処理済みのため飛ばします)")
            continue

        title = make_title(path)
        print(f"{path.name}\t{title}")
        writer.writerow([path.name, title])
        file.flush()

print(f"\n{OUTPUT_FILE} に保存しました。")
