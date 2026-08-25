"""1枚の画像を説明させる。"""

from ollama import chat

MODEL = "gemma4:e2b"
IMAGE = "vision/images/sample.jpg"

response = chat(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": "この画像に何が写っているか、日本語で簡潔に説明してください。",
            "images": [IMAGE],
        }
    ],
)

print(response.message.content)
