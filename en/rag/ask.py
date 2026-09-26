"""Retrieve relevant passages and answer using them as evidence."""

import json
from pathlib import Path

import ollama

EMBED_MODEL = "embeddinggemma"
CHAT_MODEL = "gemma4:e2b"
INDEX_FILE = Path("rag/index.json")
TOP_K = 3

records = json.loads(INDEX_FILE.read_text(encoding="utf-8"))

question = input("Question: ")

result = ollama.embed(model=EMBED_MODEL, input=question)
question_vector = result["embeddings"][0]


def similarity(a, b):
    return sum(x * y for x, y in zip(a, b))


records.sort(key=lambda r: similarity(question_vector, r["vector"]), reverse=True)
found = records[:TOP_K]

context = "\n\n".join(f"[{r['source']}]\n{r['text']}" for r in found)

prompt = f"""Answer the question using only the following documents.
If the documents do not contain the answer, say "The documents do not say."

# Documents
{context}

# Question
{question}
"""

response = ollama.chat(model=CHAT_MODEL, messages=[{"role": "user", "content": prompt}])
print(response.message.content)

print("\n--- Referenced documents ---")
for record in found:
    print(f"{record['source']}: {record['text'][:40]}...")
