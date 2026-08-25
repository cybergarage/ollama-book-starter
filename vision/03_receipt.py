"""第6章 レシートの画像から項目を読み取る。"""

from ollama import chat
from pydantic import BaseModel


class Receipt(BaseModel):
    store: str
    date: str
    total: int


response = chat(
    model="gemma4:e2b",
    messages=[
        {
            "role": "user",
            "content": "このレシートの画像から、店名、日付、合計金額を読み取ってください。",
            "images": ["ch06_vision/images/receipt.jpg"],
        }
    ],
    format=Receipt.model_json_schema(),
    options={"temperature": 0},
)

receipt = Receipt.model_validate_json(response.message.content)
print(receipt.store)
print(receipt.date)
print(receipt.total)
