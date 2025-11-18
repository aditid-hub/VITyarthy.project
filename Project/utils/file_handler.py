import json
import os
from typing import Any

STORAGE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "storage")
os.makedirs(STORAGE_DIR, exist_ok=True)

def _path(filename: str) -> str:
    return os.path.join(STORAGE_DIR, filename)

def read_json(filename: str, default: Any = None):
    path = _path(filename)
    if not os.path.exists(path):
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def write_json(filename: str, data: Any):
    path = _path(filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
