import json
from pathlib import Path

def init_path(filename="data.json"):
    return Path(__file__).parent / filename

def init_storage(path):
    if not path.exists():
        with open(path, "w", encoding="utf-8") as f:
            json.dump([], f)

def get_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(path, operations):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(operations, f, ensure_ascii=False)