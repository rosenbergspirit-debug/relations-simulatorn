Relations Simulator är tänkt att vara ett turbaserat textspel som simulerar relationsdynamik
genom val och konsekvenser. 

Detta är bara en prototyp med förhoppning om att längre fram kunna skapa en simulering som faktiskt kan hjälpa par simulera hur olika val får olika konsekvenser. 

I denna prototyp ställs man inför olika vardagliga konfliktscenarier där varje val påverkar relationens tillstånd över tid.

---

Installation

1. Klona repot:
```bash
git clone https://github.com/rosenbergspirit-debug/relations-simulatorn.git


---

Project-struktur

src/
└── relations_simulator/
    ├── engine.py        # Spelmotorn och klass
    ├── main.py          # CLI
    ├── __main__.py      # Python -m relations_simulator
    ├── config.py        # Konfiguration och pathing (Pathlib)
    ├── utils.py         # Logger och säker input-hantering
    ├── module_io.py     # JSON-inläsning
    ├── scenarios.json   # Spelets scenarier och val
    └── tests/
        └── test_engine.py  # Enhetstester för spelmotorn
