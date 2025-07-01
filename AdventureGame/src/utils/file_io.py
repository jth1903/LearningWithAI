import json
from typing import Any

def save_game_state(filename: str, data: Any) -> None:
    """Save the game state to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_game_state(filename: str) -> Any:
    """Load the game state from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)
