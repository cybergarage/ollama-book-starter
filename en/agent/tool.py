"""Give the model one tool to use."""

from datetime import date

from ollama import chat

MODEL = "gemma4:e2b"


def get_today() -> str:
    """Get today's date

    Returns:
        A string in YYYY-MM-DD format
    """
    return date.today().isoformat()


messages = [{"role": "user", "content": "What is today's date?"}]

response = chat(model=MODEL, messages=messages, tools=[get_today])
messages.append(response.message)

if response.message.tool_calls:
    for call in response.message.tool_calls:
        print(f"Used tool: {call.function.name}")
        result = get_today(**call.function.arguments)
        messages.append(
            {"role": "tool", "tool_name": call.function.name, "content": str(result)}
        )

    response = chat(model=MODEL, messages=messages, tools=[get_today])

print(response.message.content)
