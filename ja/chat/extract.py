"""応答の形式を指定して、文章から項目を抜き出す。"""

from ollama import chat
from pydantic import BaseModel


class Receipt(BaseModel):
    store: str
    date: str
    total: int


text = """
青空マーケット 神田店
2026年9月8日
ミネラルウォーター 120円
ツナサンド 298円
ドリップコーヒー 180円
合計 658円
"""

response = chat(
    model="gemma4:e2b",
    messages=[{"role": "user", "content": f"次のレシートから項目を抜き出してください。\n\n{text}"}],
    format=Receipt.model_json_schema(),
    options={"temperature": 0},
)

receipt = Receipt.model_validate_json(response.message.content)
print(receipt.store)
print(receipt.date)
print(receipt.total)
