"""Extract fields from text with a specified response format."""

from ollama import chat
from pydantic import BaseModel


class Receipt(BaseModel):
    store: str
    date: str
    total: int


text = """
Aozora Market Kanda
September 8, 2026
Mineral water 120 yen
Tuna sandwich 298 yen
Drip coffee 180 yen
Total 658 yen
"""

response = chat(
    model="gemma4:e2b",
    messages=[{"role": "user", "content": f"Extract the fields from the following receipt.\n\n{text}"}],
    format=Receipt.model_json_schema(),
    options={"temperature": 0},
)

receipt = Receipt.model_validate_json(response.message.content)
print(receipt.store)
print(receipt.date)
print(receipt.total)
