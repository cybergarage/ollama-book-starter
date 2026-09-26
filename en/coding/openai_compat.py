"""Use a local model through an OpenAI-compatible endpoint."""

from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="ollama",
)

completion = client.chat.completions.create(
    model="gemma4:e2b",
    messages=[{"role": "user", "content": "Introduce yourself."}],
)

print(completion.choices[0].message.content)
