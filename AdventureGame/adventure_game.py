import time
import random
import json
import os
from typing import Dict, List, Optional, Any
from item import Item
from enemy import Enemy
from player import Player
from room import Room
from game_world import GameWorld
from game_engine import GameEngine

# Start the game
if __name__ == "__main__":
    game = GameEngine()
    game.play() 