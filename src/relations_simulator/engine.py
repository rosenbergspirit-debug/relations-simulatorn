from dataclasses import dataclass
from typing import Dict

from .config import MIN_VALUE, MAX_VALUE, MAX_REPAIR_POINTS
from .utils import log_info, log_warning


@dataclass
class GameState:
    trust: int
    stress: int
    weeds: int
    misinterpretation: int
    repair_points: int = 0

    def clamp(self):
        """Alla värden hålls inom 0–100."""
        self.trust = max(MIN_VALUE, min(MAX_VALUE, self.trust))
        self.stress = max(MIN_VALUE, min(MAX_VALUE, self.stress))
        self.weeds = max(MIN_VALUE, min(MAX_VALUE, self.weeds))
        self.misinterpretation = max(MIN_VALUE, min(MAX_VALUE, self.misinterpretation))


def apply_choice(state: GameState, effects: Dict[str, int]) -> GameState:
    """
    Applicerar ett val.
    """
    log_info("Applicerar valets konsekvenser")

    for key, value in effects.items():
        if hasattr(state, key):
            old = getattr(state, key)
            setattr(state, key, old + value)
            log_info(f"{key}: {old} → {getattr(state, key)}")

    state.clamp()
    return state


def apply_repair(state: GameState) -> GameState:
   
    if state.repair_points >= MAX_REPAIR_POINTS:
        log_warning("Inga repair-points kvar")
        return state

    log_info("Repair används")
    state.weeds -= 5
    state.trust += 3
    state.repair_points += 1

    state.clamp()
    return state
