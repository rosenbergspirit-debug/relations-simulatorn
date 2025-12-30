from .config import DEFAULT_STATE, SCENARIO_FILE
from .engine import GameState, apply_choice, apply_repair
from .module_io import load_json
from .utils import safe_input, log_info

print("Relations Simulator startar...")

def main():
    log_info("Relations Simulator startar")

    scenarios = load_json(SCENARIO_FILE)
    state = GameState(**DEFAULT_STATE)

    for scenario in scenarios:
        print("\n" + scenario["text"])
        for key, choice in scenario["choices"].items():
            print(f"{key}: {choice['label']}")

        print("r: Försök reparera relationen")

        choice = safe_input("Välj: ", allowed=list(scenario["choices"].keys()) + ["r"])

        if choice == "r":
            apply_repair(state)
        else:
            apply_choice(state, scenario["choices"][choice]["effects"])

        print(f"Tillit: {state.trust}, Stress: {state.stress}, Ogräs: {state.weeds}")

    print("\nSpelet är slut. Tack för att du spelade!")

if __name__ == "__main__":
    main()
