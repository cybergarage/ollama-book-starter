"""The shortest sample program."""

from ollama import chat

response = chat(
    model="gemma4:e2b",
    messages=[
        {"role": "user", "content": "What is a local LLM? Explain in three lines."},
    ],
)

print(response.message.content)
