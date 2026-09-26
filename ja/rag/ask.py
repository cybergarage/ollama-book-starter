"""質問に関係する部分を取り出し、それを根拠に答えさせる。"""

import json
from pathlib import Path

import ollama

EMBED_MODEL = "embeddinggemma"
CHAT_MODEL = "gemma4:e2b"
INDEX_FILE = Path("rag/index.json")
TOP_K = 3

records = json.loads(INDEX_FILE.read_text(encoding="utf-8"))

question = input("質問: ")

result = ollama.embed(model=EMBED_MODEL, input=question)
question_vector = result["embeddings"][0]


def similarity(a, b):
    return sum(x * y for x, y in zip(a, b))


records.sort(key=lambda r: similarity(question_vector, r["vector"]), reverse=True)
found = records[:TOP_K]

context = "\n\n".join(f"[{r['source']}]\n{r['text']}" for r in found)

prompt = f"""次の資料だけを根拠にして、質問に答えてください。
資料に書かれていないことは「資料には書かれていません」と答えてください。

# 資料
{context}

# 質問
{question}
"""

response = ollama.chat(model=CHAT_MODEL, messages=[{"role": "user", "content": prompt}])
print(response.message.content)

print("\n--- 参照した資料 ---")
for record in found:
    print(f"{record['source']}: {record['text'][:40]}...")
