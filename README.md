Relations Simulator

Relations Simulator är ett turbaserat textspel som simulerar relationsdynamik genom val och konsekvenser.
Detta är en prototyp där spelaren ställs inför vardagliga konfliktscenarier och varje val påverkar relationens
tillit, stress och “ogräs” (olösta konflikter) över tid.

---

Installation
```bash
git clone https://github.com/rosenbergspirit-debug/relations-simulatorn.git
cd relations-simulatorn

python -m venv .venv
source .venv/Scripts/activate
pip install -e .

Kör spelet
python -m relations_simulator

Kör tester
python -m unittest discover src
