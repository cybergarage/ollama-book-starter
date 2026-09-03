"""文書を分割し、埋め込みにして保存する。"""

import json
from pathlib import Path

import ollama

EMBED_MODEL = "embeddinggemma"
DOC_DIR = Path("rag/documents")
INDEX_FILE = Path("rag/index.json")
CHUNK_SIZE = 400
OVERLAP = 100


def split(text):
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start : start + CHUNK_SIZE])
        if start + CHUNK_SIZE >= len(text):
            break
        start += CHUNK_SIZE - OVERLAP
    return chunks


records = []
for path in sorted(DOC_DIR.glob("*.txt")):
    text = path.read_text(encoding="utf-8")
    for chunk in split(text):
        records.append({"source": path.name, "text": chunk})

result = ollama.embed(model=EMBED_MODEL, input=[r["text"] for r in records])

for record, vector in zip(records, result["embeddings"]):
    record["vector"] = vector

INDEX_FILE.write_text(json.dumps(records, ensure_ascii=False), encoding="utf-8")
print(f"{len(records)}件を保存しました。")
