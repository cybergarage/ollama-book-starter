"""Describe a single image."""

from ollama import chat

MODEL = "gemma4:e2b"
IMAGE = "vision/images/sample.jpg"

response = chat(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": "Briefly describe what is shown in this image in English.",
            "images": [IMAGE],
        }
    ],
)

print(response.message.content)
