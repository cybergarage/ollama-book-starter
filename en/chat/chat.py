"""A conversation program that preserves history and streams the answer."""

from ollama import chat

MODEL = "gemma4:e2b"

messages = [
    {
        "role": "system",
        "content": "You explain technical topics to beginners. Always answer in English.",
    },
]

print("Enter a question. Press Enter on an empty line to quit.")

while True:
    text = input("\nYou: ").strip()
    if text == "":
        break

    messages.append({"role": "user", "content": text})

    print("AI: ", end="", flush=True)
    answer = ""
    for chunk in chat(model=MODEL, messages=messages, stream=True):
        piece = chunk.message.content
        print(piece, end="", flush=True)
        answer += piece
    print()

    messages.append({"role": "assistant", "content": answer})
