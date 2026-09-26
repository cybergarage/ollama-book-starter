"""Measure generated tokens per second."""

import ollama

MODEL = "gemma4:e2b"

response = ollama.chat(
    model=MODEL,
    messages=[{"role": "user", "content": "Describe the four seasons in Japan in about 100 English words."}],
)

count = response.eval_count
seconds = response.eval_duration / 1_000_000_000

print(f"Generated: {count} tokens")
print(f"Elapsed time: {seconds:.1f} seconds")
print(f"Per second: {count / seconds:.1f} tokens")
