import json
from pathlib import Path

def save_json(path: Path, data: dict):
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def load_json(path: Path):
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)
