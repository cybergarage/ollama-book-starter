"""道具を1つ持たせて、モデルに使わせる。"""

from datetime import date

from ollama import chat

MODEL = "gemma4:e2b"


def get_today() -> str:
    """今日の日付を調べる

    Returns:
        YYYY-MM-DD形式の文字列
    """
    return date.today().isoformat()


messages = [{"role": "user", "content": "今日は何月何日ですか。"}]

response = chat(model=MODEL, messages=messages, tools=[get_today])
messages.append(response.message)

if response.message.tool_calls:
    for call in response.message.tool_calls:
        print(f"道具を使いました: {call.function.name}")
        result = get_today(**call.function.arguments)
        messages.append(
            {"role": "tool", "tool_name": call.function.name, "content": str(result)}
        )

    response = chat(model=MODEL, messages=messages, tools=[get_today])

print(response.message.content)
