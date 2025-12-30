from .engine import GameState
from .module_io import load_scenarios
from .config import DEFAULT_STATE, SCENARIO_FILE


def start():
    print("\n=== Relations Simulator ===\n")
    print("1. Starta spel")
    print("2. Avsluta")

    choice = input("Välj: ").strip()

    if choice == "1":
        run_game()
    else:
        print("Avslutar spelet.")


def run_game():
    state = GameState.from_dict(DEFAULT_STATE)
    scenarios = load_scenarios(SCENARIO_FILE)

    print("\nSpelet startar...\n")

    for scenario in scenarios:
        print(scenario["text"])
        for i, option in enumerate(scenario["options"], start=1):
            print(f"{i}. {option['label']}")

        choice = input("Ditt val: ").strip()

        try:
            selected = scenario["options"][int(choice) - 1]
            state.apply_effects(selected["effects"])
        except Exception:
            print("Ogiltigt val, hoppar vidare.")

        print(f"\nRelation: {state.relationship}\n")

    print("Spelet är slut.")
