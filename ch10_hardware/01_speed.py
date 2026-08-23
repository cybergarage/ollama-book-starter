"""第10章 1秒あたりの生成トークン数を測る。"""

import ollama

MODEL = "gemma4:e2b"

response = ollama.chat(
    model=MODEL,
    messages=[{"role": "user", "content": "日本の四季について200文字程度で説明してください。"}],
)

count = response.eval_count
seconds = response.eval_duration / 1_000_000_000

print(f"生成した量: {count} トークン")
print(f"かかった時間: {seconds:.1f} 秒")
print(f"1秒あたり: {count / seconds:.1f} トークン")
