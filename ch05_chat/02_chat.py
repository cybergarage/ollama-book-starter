"""第5章 履歴を保ちながら少しずつ表示する対話プログラム。"""

from ollama import chat

MODEL = "gemma4:e2b"

messages = [
    {
        "role": "system",
        "content": "あなたは初心者向けの技術解説者です。必ず日本語で答えてください。",
    },
]

print("質問を入力してください。終了するには何も入力せずEnterを押します。")

while True:
    text = input("\nあなた: ").strip()
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
