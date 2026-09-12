"""本書のサンプルを動かす準備ができているかを確認します。"""

import json
import sys
import urllib.error
import urllib.request

OLLAMA_URL = "http://localhost:11434"
REQUIRED_MODELS = ["gemma4:e2b", "embeddinggemma"]


def check_python():
    version = sys.version_info
    ok = version >= (3, 9)
    print(f"[{'OK' if ok else 'NG'}] Python {version.major}.{version.minor}.{version.micro}")
    if not ok:
        print("     Python 3.9以降が必要です。")
    return ok


def check_library():
    try:
        import ollama  # noqa: F401
    except ImportError:
        print("[NG] ollamaライブラリが見つかりません")
        print("     pip install -r requirements.txt を実行してください。")
        return False
    print("[OK] ollamaライブラリ")
    return True


def fetch_models():
    try:
        with urllib.request.urlopen(f"{OLLAMA_URL}/api/tags", timeout=5) as response:
            data = json.load(response)
    except (urllib.error.URLError, OSError):
        print(f"[NG] Ollamaサーバーに接続できません({OLLAMA_URL})")
        print("     Ollamaが起動しているか確認してください。")
        return None

    print(f"[OK] Ollamaサーバー({OLLAMA_URL})")
    return [item.get("model") or item.get("name", "") for item in data.get("models", [])]


def check_models(installed):
    ok = True
    for name in REQUIRED_MODELS:
        if any(item == name or item.startswith(f"{name}:") for item in installed):
            print(f"[OK] モデル {name}")
        else:
            print(f"[NG] モデル {name} がありません")
            print(f"     ollama pull {name} を実行してください。")
            ok = False
    return ok


def main():
    results = [check_python(), check_library()]

    installed = fetch_models()
    results.append(installed is not None)
    if installed is not None:
        results.append(check_models(installed))

    print()
    if all(results):
        print("準備は完了しています。")
    else:
        print("上のNGを解消してから、もう一度実行してください。")


if __name__ == "__main__":
    main()
