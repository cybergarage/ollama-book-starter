"""An agent that keeps running until it finishes using tools."""

from datetime import date
from pathlib import Path

from ollama import chat

MODEL = "gemma4:e2b"
MAX_STEPS = 5


def get_today() -> str:
    """Get today's date

    Returns:
        A string in YYYY-MM-DD format
    """
    return date.today().isoformat()


def count_files(folder: str) -> str:
    """Count files in the specified folder

    Args:
        folder: Path to the folder to inspect

    Returns:
        A string containing the file count
    """
    target = Path(folder)
    if not target.is_dir():
        return "Folder not found"
    return str(sum(1 for item in target.iterdir() if item.is_file()))


TOOLS = {"get_today": get_today, "count_files": count_files}

messages = [
    {
        "role": "user",
        "content": "Get today's date and count the files in rag/documents. Summarize both in one line.",
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
            result = "That tool is unavailable"
        messages.append({"role": "tool", "tool_name": name, "content": str(result)})
else:
    print("Stopped after reaching the step limit.")
