"""Extract fields from text with a specified response format."""

from ollama import chat
from pydantic import BaseModel


class Receipt(BaseModel):
    store: str
    date: str
    total: float


text = """
Maple Market
09/08/2026
Bottled Water $1.99
Tuna Sandwich $6.49
Drip Coffee $2.79
TOTAL $11.27
"""

response = chat(
    model="gemma4:e2b",
    messages=[{"role": "user", "content": f"Extract the store, date, and total from this receipt. Return the total as a number of US dollars without the dollar sign.\n\n{text}"}],
    format=Receipt.model_json_schema(),
    options={"temperature": 0},
)

receipt = Receipt.model_validate_json(response.message.content)
print(receipt.store)
print(receipt.date)
print(receipt.total)
