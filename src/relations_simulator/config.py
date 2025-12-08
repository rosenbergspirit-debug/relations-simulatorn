from pathlib import Path

# Projektets root-mapp (src/my_project/..)
ROOT_DIR = Path(__file__).resolve().parent.parent

# Datamappar
DATA_DIR = ROOT_DIR / "data"
OUTPUT_DIR = ROOT_DIR / "output"

# Skapa mappar om de inte finns
DATA_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# Globala variabler
PROJECT_NAME = "Text Analysis Generator"
