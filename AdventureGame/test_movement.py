#!/usr/bin/env python3

from game_world import GameWorld
from game_engine import GameEngine
from player import Player

def test_movement_commands():
    game = GameEngine()
    game.player = Player("Test")  # Create a test player
    
    # Set current room to treasure_room
    game.current_room_id = "treasure_room"
    
    print("Testing movement commands from treasure_room:")
    room = game.world.get_room("treasure_room")
    if room:
        print(f"Initial exits: {list(room.exits.keys())}")
        
        # Simulate using Staff of the Light Mage to add ancient_door exit
        room.exits["ancient_door"] = "ancient_door"
        print(f"After adding ancient_door: {list(room.exits.keys())}")
    
    # Test commands
    test_commands = [
        "ancient_door",
        "ancient door", 
        "west",
        "north",
        "invalid_exit"
    ]
    
    for command in test_commands:
        print(f"\nTesting command: '{command}'")
        result = game.process_command(command)
        print(f"Result: {result}")

if __name__ == "__main__":
    test_movement_commands() 