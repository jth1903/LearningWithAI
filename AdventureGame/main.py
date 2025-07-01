import time
import random
import json
import os
from typing import Dict, List, Optional, Any
from src.core import Item, Enemy, Player, Room
from src.world import GameWorld
from src.engine import GameEngine

# Start the game
if __name__ == "__main__":
    game = GameEngine()
    game.play() 