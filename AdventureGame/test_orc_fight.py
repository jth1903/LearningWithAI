#!/usr/bin/env python3

from game_world import GameWorld
from game_engine import GameEngine
from player import Player

def setup_orc_fight():
    """Set up the game state to fight the orc"""
    game = GameEngine()
    
    # Create a player with good stats and equipment
    game.player = Player("Test Fighter")
    game.player.health = 100
    game.player.max_health = 100
    game.player.level = 5
    game.player.experience = 200
    
    # Give the player some good equipment
    legendary_sword = game.world.get_item("legendary_sword")
    if legendary_sword:
        game.player.add_item(legendary_sword)
        game.player.equip_item("legendary_sword")
        print(f"Equipped {legendary_sword.name}")
    
    # Give the player some health potions
    health_potion = game.world.get_item("health_potion")
    if health_potion:
        game.player.add_item(health_potion)
        game.player.add_item(health_potion)  # Give 2 potions
        print(f"Added {health_potion.name} x2")
    
    # Set current room to ancient_door where the orc is
    game.current_room_id = "ancient_door"
    
    print(f"\n=== ORC FIGHT TEST ===")
    print(f"Player: {game.player.name}")
    print(f"Health: {game.player.health}/{game.player.max_health}")
    print(f"Level: {game.player.level}")
    if game.player.equipped_weapon:
        print(f"Weapon: {game.player.equipped_weapon.name} (Damage: {game.player.equipped_weapon.damage})")
    
    # Show the room
    room = game.world.get_room("ancient_door")
    if room:
        print(f"\nRoom: {room.room_id}")
        print(f"Description: {room.description}")
        if room.has_enemies():
            print(f"Enemies: {list(room.enemies.keys())}")
            for enemy_name, enemy in room.enemies.items():
                print(f"  {enemy_name}: Health {enemy.health}, Damage {enemy.damage}")
    
    print(f"\nAvailable commands:")
    print(f"- attack orc")
    print(f"- use health potion")
    print(f"- status")
    print(f"- inventory")
    print(f"- quit")
    
    return game

def play_orc_fight():
    """Play the orc fight interactively"""
    game = setup_orc_fight()
    
    while not game.game_over:
        game.show_room()
        command = game.get_command()
        game.process_command(command)
        
        # Add some delay for better pacing
        import time
        time.sleep(0.5)

def quick_orc_test():
    """Quick test of the orc fight without interactive input"""
    game = setup_orc_fight()
    
    print(f"\n=== QUICK ORC FIGHT TEST ===")
    
    # Show the room first
    game.show_room()
    
    # Simulate a few attacks
    for i in range(5):
        print(f"\n--- Round {i+1} ---")
        result = game.process_attack("orc")
        if not result:
            print("Attack failed or orc defeated")
            break
        
        # Show status
        game.process_status()
        
        # Use potion if health is low
        if game.player and game.player.health < 50:
            print("Health low, using potion...")
            game.process_use("health potion")
    
    print(f"\n=== FIGHT COMPLETE ===")
    game.process_status()

if __name__ == "__main__":
    # Uncomment the line below for interactive play
    play_orc_fight()
    
    # Or run the quick test instead
    # quick_orc_test() 