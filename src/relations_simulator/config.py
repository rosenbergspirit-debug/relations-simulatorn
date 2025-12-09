from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SCENARIO_FILE = BASE_DIR / "scenarios.json"

DEFAULT_STATE = {
    "trust": 70,
    "stress": 20,
    "weeds": 10,
    "misinterpretation": 20,
    "repair_points": 0
}

MAX_REPAIR_POINTS = 3
MIN_VALUE = 0
MAX_VALUE = 100
