# ローカルLLMをはじめよう サンプルコード

書籍『ローカルLLMをはじめよう ― Ollamaで動かす自分専用のAI』のサンプルコードです。

## 書籍との対応

| 書籍の版 | 対応する内容 |
| --- | --- |
| 初版 | `main`（最新） |

現時点では、最新の内容が書籍の記述に対応しています。書籍のとおりに動かない場合は、この表と下の「更新の記録」を確認してください。

## 取得

```
git clone --depth 1 https://github.com/cybergarage/ollama-book-starter.git
cd ollama-book-starter
```

`--depth 1` は履歴を取り込まず最新の内容だけを取得する指定です。内容を新しくするときは `git pull` を実行してください。

## 準備

1. Ollamaをインストールして起動する — https://ollama.com/download
2. 本書で使うモデルを取得する

```
ollama pull gemma4:e2b
ollama pull embeddinggemma
```

3. Pythonの環境を用意して、必要な道具を入れる

```
python -m venv .venv
source .venv/bin/activate     # Windows は .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

4. 準備ができたか確認する

```
python check_env.py
```

## 実行のしかた

**このフォルダ（リポジトリの一番上）から**実行してください。

```
python ch05_chat/01_hello.py
```

フォルダの中へ移動してから実行すると、サンプルの画像や文書への道筋が合わなくなります。

## 章とフォルダの対応

| フォルダ | 章 |
| --- | --- |
| `ch05_chat` | 第5章 PythonからOllamaを使おう |
| `ch06_vision` | 第6章 画像を読ませよう |
| `ch07_rag` | 第7章 手元の文書に答えさせよう |
| `ch08_coding` | 第8章 プログラミングを手伝わせよう |
| `ch09_agent` | 第9章 AIエージェントを体験しよう |
| `ch10_hardware` | 第10章 快適に動かすパソコンを選ぼう |

## 動かないときは

まず `python check_env.py` を実行してください。原因の多くはここに表示されます。

## 更新の記録

書籍の刊行後に加えた変更を記録します。

| 日付 | 変更内容 |
| --- | --- |
| - | - |
