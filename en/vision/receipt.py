"""Read fields from a receipt image."""

from ollama import chat
from pydantic import BaseModel


class Receipt(BaseModel):
    store: str
    date: str
    total: float


response = chat(
    model="gemma4:e2b",
    messages=[
        {
            "role": "user",
            "content": "Read the store name, date, and total from this receipt image. Return the total as a number of US dollars without the dollar sign.",
            "images": ["vision/images/receipt.jpg"],
        }
    ],
    format=Receipt.model_json_schema(),
    options={"temperature": 0},
)

receipt = Receipt.model_validate_json(response.message.content)
print(receipt.store)
print(receipt.date)
print(receipt.total)
