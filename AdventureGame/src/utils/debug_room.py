#!/usr/bin/env python3

from game_world import GameWorld
from game_engine import GameEngine
from player import Player

def debug_rooms():
    """Debug all rooms to see what's available"""
    game = GameEngine()
    
    print("=== DEBUGGING ALL ROOMS ===")
    
    # List all available rooms
    print(f"Total rooms: {len(game.world.rooms)}")
    print(f"Room IDs: {list(game.world.rooms.keys())}")
    
    # Check each room
    for room_id, room in game.world.rooms.items():
        print(f"\nRoom: {room_id}")
        print(f"  Description: {room.description}")
        print(f"  Exits: {room.exits}")
        print(f"  Items: {room.items}")
        print(f"  Has enemies: {room.has_enemies()}")
        if room.has_enemies():
            print(f"  Enemies: {list(room.enemies.keys())}")
    
    # Specifically check for ancient_door
    print(f"\n=== SPECIFIC CHECK FOR ANCIENT_DOOR ===")
    ancient_door = game.world.get_room("ancient_door")
    if ancient_door:
        print("ancient_door room found!")
        print(f"Description: {ancient_door.description}")
        print(f"Items: {ancient_door.items}")
        print(f"Enemies: {list(ancient_door.enemies.keys()) if ancient_door.has_enemies() else 'None'}")
    else:
        print("ancient_door room NOT found!")
        
        # Check if it's in the rooms_data but not created
        print("\nChecking if it's in the rooms_data...")
        # We can't access the private method directly, but let's check what we have

if __name__ == "__main__":
    debug_rooms() 