"""OpenAI互換の窓口から、手元のモデルを使う。"""

from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="ollama",
)

completion = client.chat.completions.create(
    model="gemma4:e2b",
    messages=[{"role": "user", "content": "自己紹介してください。"}],
)

print(completion.choices[0].message.content)
