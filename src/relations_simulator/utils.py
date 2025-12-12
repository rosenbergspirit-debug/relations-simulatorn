from datetime import datetime

def _timestamp():
    """Returnerar en tidsstämpel för loggmeddelanden."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_info(message: str):
    print(f"[INFO { _timestamp() }] {message}")

def log_warning(message: str):
    print(f"[WARNING { _timestamp() }] {message}")

def log_error(message: str):
    print(f"[ERROR { _timestamp() }] {message}")

def safe_input(prompt: str, allowed: list[str] = None, max_length: int = 50):
    """
    Säker hantering av input:
    - Kan begränsa vilka ord/tecken som är tillåtna
    - Stoppar tomma inputs
    - Begränsar längd
    """

    while True:
        user_input = input(prompt).strip()

        if not user_input:
            log_warning("Tom input, försök igen.")
            continue

        if len(user_input) > max_length:
            log_warning(f"Inputen är för lång (max {max_length} tecken).")
            continue

        if allowed is not None:
            if user_input.lower() not in allowed:
                log_warning(f"Felaktigt val. Tillåtna val är: {allowed}")
                continue

        return user_input.lower()
