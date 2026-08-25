"""第5章 いちばん短いプログラム。"""

from ollama import chat

response = chat(
    model="gemma4:e2b",
    messages=[
        {"role": "user", "content": "ローカルLLMとは何ですか。3行で説明してください。"},
    ],
)

print(response.message.content)
