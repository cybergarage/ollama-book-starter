"""Check whether the book samples are ready to run."""

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
        print("     Python 3.9 or later is required.")
    return ok


def check_library():
    try:
        import ollama  # noqa: F401
    except ImportError:
        print("[NG] The ollama library was not found")
        print("     Run pip install -r requirements.txt.")
        return False
    print("[OK] ollama library")
    return True


def fetch_models():
    try:
        with urllib.request.urlopen(f"{OLLAMA_URL}/api/tags", timeout=5) as response:
            data = json.load(response)
    except (urllib.error.URLError, OSError):
        print(f"[NG] Cannot connect to the Ollama server({OLLAMA_URL})")
        print("     Check that Ollama is running.")
        return None

    print(f"[OK] Ollama server({OLLAMA_URL})")
    return [item.get("model") or item.get("name", "") for item in data.get("models", [])]


def check_models(installed):
    ok = True
    for name in REQUIRED_MODELS:
        if any(item == name or item.startswith(f"{name}:") for item in installed):
            print(f"[OK] Model {name}")
        else:
            print(f"[NG] Model {name} is missing")
            print(f"     Run ollama pull {name}.")
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
        print("Setup is complete.")
    else:
        print("Resolve the NG items above, then run this check again.")


if __name__ == "__main__":
    main()
