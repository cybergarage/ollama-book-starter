"""第9章 道具を使い終わるまで繰り返すエージェント。"""

from datetime import date
from pathlib import Path

from ollama import chat

MODEL = "gemma4:e2b"
MAX_STEPS = 5


def get_today() -> str:
    """今日の日付を調べる

    Returns:
        YYYY-MM-DD形式の文字列
    """
    return date.today().isoformat()


def count_files(folder: str) -> str:
    """指定したフォルダにあるファイルの数を数える

    Args:
        folder: 調べたいフォルダへの道筋

    Returns:
        ファイルの数を表す文字列
    """
    target = Path(folder)
    if not target.is_dir():
        return "そのフォルダは見つかりません"
    return str(sum(1 for item in target.iterdir() if item.is_file()))


TOOLS = {"get_today": get_today, "count_files": count_files}

messages = [
    {
        "role": "user",
        "content": "今日の日付と、ch07_rag/documents にあるファイルの数を調べて、1行にまとめてください。",
    }
]

for step in range(MAX_STEPS):
    response = chat(model=MODEL, messages=messages, tools=list(TOOLS.values()))
    messages.append(response.message)

    if not response.message.tool_calls:
        print(response.message.content)
        break

    for call in response.message.tool_calls:
        name = call.function.name
        print(f"[{step + 1}] {name}({call.function.arguments})")
        if name in TOOLS:
            result = TOOLS[name](**call.function.arguments)
        else:
            result = "その道具はありません"
        messages.append({"role": "tool", "tool_name": name, "content": str(result)})
else:
    print("上限の回数に達したため中断しました。")
