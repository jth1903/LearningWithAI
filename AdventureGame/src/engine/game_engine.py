import time
import json
import os

from src.core import room
from src.core.room import Room
from ..core import Player
from ..world import GameWorld

class GameEngine:
    """Main game engine that handles game logic"""
    def __init__(self):
        self.world = GameWorld()
        self.player = None
        self.current_room_id = "entrance"
        self.game_over = False
        self.save_file = "save_game.json"
    
    def print_slow(self, text: str, delay: float = 0.03) -> None:
        """Print text with a typewriter effect"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def get_player_name(self) -> None:
        """Get the player's name"""
        self.print_slow("Welcome to the Cave of Mysteries!")
        self.print_slow("What is your name, brave adventurer?")
        name = input("> ").strip()
        if not name:
            name = "Adventurer"
        self.player = Player(name)
        self.print_slow(f"Welcome, {name}! Your adventure begins...")
    
    def show_room(self) -> None:
        """Display current room information"""
        room = self.world.get_room(self.current_room_id)
        print(room.visited(room))
        if not room:
            return
        
        print("\n" + "="*50)
        self.print_slow(room.description)
        
        # Show player status
        if self.player:
            self.print_slow(f"Health: {self.player.health}/{self.player.max_health} | Coins: {self.player.coins} | Level: {self.player.level}")
        
        # Show available exits
        exits = list(room.exits.keys())
        if exits:
            self.print_slow(f"Exits: {', '.join(exits)}")
        
        # Show items in room
        if room.items:
            item_names = []
            for item_id in room.items:
                item = self.world.get_item(item_id)
                if item:
                    item_names.append(item.name)
            if item_names:
                self.print_slow(f"You see: {', '.join(item_names)}")
        
        # Show enemies
        if room.has_enemies():
            enemy_names = list(room.enemies.keys())
            self.print_slow(f"Enemies: {', '.join(enemy_names)}")
        
        # Show equipped items
        if self.player and self.player.equipped_weapon:
            self.print_slow(f"Equipped weapon: {self.player.equipped_weapon.name}")
        if self.player and self.player.equipped_armor:
            self.print_slow(f"Equipped armor: {self.player.equipped_armor.name}")
    
    def get_command(self) -> str:
        """Get and process player command"""
        self.print_slow("\nWhat would you like to do?")
        command = input("> ").lower().strip()
        return command
    
    def process_movement(self, direction: str) -> bool:
        """Process movement command"""
        room = self.world.get_room(self.current_room_id)
        if not room:
            self.print_slow("Error: Room not found.")
            return False
            
        if direction in room.exits:
            self.current_room_id = room.exits[direction]
            room = self.world.get_room(self.current_room_id)
            if room:
                self.print_slow(f"You move {direction} into the {room.name}...")
                self.process_visit(room)
            else:
                self.print_slow("Error: Destination room not found.")
            return True
        else:
            self.print_slow(f"You can't go {direction} from here.")
            return False
    
    def process_visit(self, room : Room):
        return room.visit_room()

    def process_take(self, item_name: str) -> bool:
        """Process take item command"""
        room = self.world.get_room(self.current_room_id)
        if not room:
            self.print_slow("Error: Room not found.")
            return False
        
        # Find item by name
        item_id = None
        for room_item_id in room.items:
            item = self.world.get_item(room_item_id)
            if item and item.name.lower() == item_name.lower():
                item_id = room_item_id
                break
        
        if item_id and room.remove_item(item_id):
            item = self.world.get_item(item_id)
            if item and self.player:
                self.player.add_item(item)
                self.print_slow(f"You picked up the {item.name}!")
                
                # Handle special items
                if item_id == "gold_coin":
                    self.player.coins += item.value
                    self.print_slow(f"You gained {item.value} coin!")
                
                return True
        
        self.print_slow("You don't see that here.")
        return False
    
    def process_use(self, item_name: str) -> bool:
        """Process use item command"""
        if not self.player:
            return False
            
        # Find item in inventory
        item_id = None
        if self.player and self.player.inventory:
            for inv_item_id, item in self.player.inventory.items():
                if item.name.lower() == item_name.lower():
                    item_id = inv_item_id
                    break
        
        if not item_id:
            self.print_slow("You don't have that item.")
            return False
        
        if not self.player or not self.player.inventory:
            self.print_slow("You don't have that item.")
            return False
        
        item = self.player.inventory[item_id]
        self.print_slow(f"You use the {item.name}...")
        
        # Handle consumable items
        if item.item_type == "consumable":
            if hasattr(item, 'healing'):
                healing = item.healing
                actual_healing = self.player.heal(healing)
                self.print_slow(f"You restore {actual_healing} health!")
                self.player.remove_item(item_id, 1)
                return True
        
        # Handle special item interactions
        if item_id == "torch" and self.current_room_id == "dark_tunnel":
            self.print_slow("The torch illuminates the tunnel! You can see ancient writings on the walls.")
        elif item_id == "torch" and self.current_room_id == "hidden_passage":
            self.print_slow("The hidden room lights up from the torch and you see a giant orc blocking the north exit")
        elif item_id == "ancient_key" and self.current_room_id == "treasure_room":
            self.print_slow("The key fits perfectly in the chest! You found a legendary sword!")
            legendary_sword = self.world.get_item("legendary_sword")
            if legendary_sword:
                self.player.add_item(legendary_sword)
        elif item_id == "staff_of_the_light_mage" and self.current_room_id == "treasure_room":
            self.print_slow("You raise the Staff of the Light Mage. \n A beam of light shoots from its tip, illuminating a hidden panel in the wall.")
            self.print_slow("With a rumble, the panel slides open, \n revealing a hidden passage leading deeper into the unknown...")
            treasure_room = self.world.get_room("treasure_room")
            if treasure_room:
                treasure_room.exits["ancient_door"] = "ancient door"
        else:
            self.print_slow("Nothing special happens.")
        
        return True
    
    def process_combine(self, item1_name: str, item2_name: str) -> bool:
        """Process combine items command"""
        if not self.player:
            return False
            
        # Find items in inventory
        item1_id = None
        item2_id = None
        
        for item_id, item in self.player.inventory.items():
            if item.name.lower() == item1_name.lower():
                item1_id = item_id
            elif item.name.lower() == item2_name.lower():
                item2_id = item_id
        
        if not item1_id or not item2_id:
            self.print_slow("You don't have both items in your inventory.")
            return False
        
        result_item_id = self.world.combine_items(item1_id, item2_id)
        if result_item_id:
            # Remove original items
            self.player.remove_item(item1_id, 1)
            self.player.remove_item(item2_id, 1)
            
            # Add result item
            result_item = self.world.get_item(result_item_id)
            if result_item:
                self.player.add_item(result_item)
                self.print_slow(f"You successfully combine {item1_name} and {item2_name} to create {result_item.name}!")
                return True
        
        self.print_slow(f"You can't combine {item1_name} and {item2_name}.")
        return False
    
    def process_attack(self, enemy_name: str) -> bool:
        """Process attack command"""
        if not self.player:
            return False
            
        room = self.world.get_room(self.current_room_id)
        if not room:
            return False
            
        enemy = room.get_enemy(enemy_name)
        
        if not enemy:
            self.print_slow(f"There's no {enemy_name} here to attack.")
            return False
        
        if not enemy.is_alive():
            self.print_slow(f"The {enemy_name} is already defeated.")
            return False
        
        # Player attacks
        damage = self.player.get_attack_damage()
        actual_damage = enemy.take_damage(damage)
        
        weapon_name = self.player.equipped_weapon.name if self.player.equipped_weapon else "fists"
        self.print_slow(f"You attack the {enemy.name} with your {weapon_name}")
        self.print_slow(f"You deal {actual_damage} damage!")
        
        # Check if enemy is defeated
        if not enemy.is_alive():
            self.print_slow(f"You have defeated the {enemy.name}!")
            room.remove_enemy(enemy.name)
            
            # Give experience
            exp_gain = 50
            self.player.add_experience(exp_gain)
            self.print_slow(f"You gained {exp_gain} experience!")
            
            # Special handling for orc
            if enemy.name == "orc":
                room.exits["north"] = "field"
            
            return True
        
        # Enemy retaliates
        self.print_slow(f"The {enemy.name} has {enemy.health} health remaining.")
        attack_result = enemy.attack(self.player)
        
        if attack_result['hit']:
            if attack_result['critical']:
                self.print_slow(f"The {enemy.name} lands a critical hit and deals {attack_result['damage']} damage!")
            else:
                self.print_slow(f"The {enemy.name} attacks you and deals {attack_result['damage']} damage!")
            
            self.print_slow(f"You have {self.player.health} health remaining.")
            
            if self.player.health <= 0:
                self.print_slow("You have been defeated! Game over.")
                self.game_over = True
        else:
            self.print_slow(f"The {enemy.name} swings at you but misses!")
        
        return True
    
    def process_equip(self, item_name: str) -> bool:
        """Process equip command"""
        # Find item in inventory
        item_id = None
        if self.player and self.player.inventory:
            for inv_item_id, item in self.player.inventory.items():
                if item.name.lower() == item_name.lower():
                    item_id = inv_item_id
                    break
        
        if not item_id:
            self.print_slow("You don't have that item.")
            return False
        
        if not self.player or not self.player.inventory:
            self.print_slow("You don't have that item.")
            return False
        
        item = self.player.inventory[item_id]
        if item.item_type not in ["weapon", "armor"]:
            self.print_slow("You can't equip that item.")
            return False
        
        if self.player.equip_item(item_id):
            self.print_slow(f"You equip the {item.name}.")
            return True
        else:
            self.print_slow("Failed to equip item.")
            return False
    
    def process_unequip(self, item_type: str) -> bool:
        """Process unequip command"""
        if not self.player:
            self.print_slow("Player not found.")
            return False
            
        if self.player.unequip_item(item_type):
            self.print_slow(f"You unequip your {item_type}.")
            return True
        else:
            self.print_slow(f"You don't have a {item_type} equipped.")
            return False
    
    def process_shop(self) -> bool:
        """Process shop command"""
        room = self.world.get_room(self.current_room_id)
        if not room:
            self.print_slow("Room not found.")
            return False
            
        if not room.is_shop():
            self.print_slow("There's no shop here.")
            return False
        
        self.print_slow("Welcome to the shop! Here's what we have for sale:")
        if self.player:
            self.print_slow(f"Your coins: {self.player.coins}")
        else:
            self.print_slow("Player not found.")
            return False
        
        for item_id, shop_data in room.shop_items.items():
            item = self.world.get_item(item_id)
            if item:
                self.print_slow(f"- {item.name}: {shop_data['price']} coins (Quantity: {shop_data['quantity']})")
                self.print_slow(f"  Description: {item.description}")
                if hasattr(item, 'damage'):
                    self.print_slow(f"  Damage: {item.damage}")
        
        self.print_slow("Use 'buy [item_name]' to purchase an item.")
        return True
    
    def process_sell(self, item_name: str) -> bool:
        """Process sell command"""
        if not self.player:
            return False
        
        # Find item in inventory
        item_id = None
        if self.player and self.player.inventory:
            for inv_item_id, item in self.player.inventory.items():
                if item.name.lower() == item_name.lower():
                    item_id = inv_item_id
                    break
        
        if not item_id:
            self.print_slow("You don't have that item.")
            return False
        
        if not self.player or not self.player.inventory:
            self.print_slow("You don't have that item.")
            return False
        
        # Sell item to shop
        item = self.player.inventory[item_id]
        self.print_slow(f"You sell the {item.name} for {item.value} coins!")
        self.player.coins += item.value
        self.player.remove_item(item_id, 1)
        
        return True

    def process_buy(self, item_name: str) -> bool:
        """Process buy command"""
        room = self.world.get_room(self.current_room_id)
        if not room:
            self.print_slow("Room not found.")
            return False
            
        if not room.is_shop():
            self.print_slow("There's no shop here.")
            return False
        
        # Find item in shop
        item_id = None
        shop_data = None
        if room.shop_items:
            for shop_item_id, data in room.shop_items.items():
                item = self.world.get_item(shop_item_id)
                if item and item.name.lower() == item_name.lower():
                    item_id = shop_item_id
                    shop_data = data
                    break
        
        if not item_id or not shop_data:
            self.print_slow("That item is not available in this shop.")
            return False
        
        if shop_data["quantity"] <= 0:
            self.print_slow("Sorry, that item is out of stock.")
            return False
        
        if not self.player:
            self.print_slow("Player not found.")
            return False
        
        if self.player.coins < shop_data["price"]:
            self.print_slow(f"You don't have enough coins. You need {shop_data['price']} coins but have {self.player.coins}.")
            return False
        
        # Purchase item
        self.player.coins -= shop_data["price"]
        shop_data["quantity"] -= 1
        
        item = self.world.get_item(item_id)
        if not item:
            self.print_slow("Item not found.")
            return False
            
        self.player.add_item(item)
        
        self.print_slow(f"You bought {item.name} for {shop_data['price']} coins!")
        self.print_slow(f"You have {self.player.coins} coins remaining.")
        return True
    
    def process_inventory(self) -> bool:
        """Process inventory command"""
        if not self.player:
            self.print_slow("Player not found.")
            return False
            
        if not self.player.inventory:
            self.print_slow("Your inventory is empty.")
            return True
        
        self.print_slow("Your inventory:")
        if self.player.inventory:
            for item1_id, item in self.player.inventory.items():
                if item.quantity > 1:
                    self.print_slow(f"  {item.name} (x{item.quantity})")
                else:
                    self.print_slow(f"  {item.name}")
        return True
    
    def process_examine(self, item_name: str) -> bool:
        """Process examine command"""
        # Find item in inventory
        item = None
        if self.player and self.player.inventory:
            for inv_item_id, inv_item in self.player.inventory.items():
                if inv_item.name.lower() == item_name.lower():
                    item = inv_item
                    break
        
        if not item:
            self.print_slow("You don't have that item.")
            return False
        
        self.print_slow(f"You examine the {item.name}:")
        self.print_slow(f"  Description: {item.description}")
        self.print_slow(f"  Type: {item.item_type}")
        self.print_slow(f"  Rarity: {item.rarity}")
        
        if hasattr(item, 'damage'):
            self.print_slow(f"  Damage: {item.damage}")
        if hasattr(item, 'durability'):
            self.print_slow(f"  Durability: {item.durability}/{item.max_durability}")
        if hasattr(item, 'value'):
            self.print_slow(f"  Value: {item.value} coins")
        
        return True
    
    def process_status(self) -> bool:
        """Process status command"""
        if not self.player:
            self.print_slow("Player not found.")
            return False
            
        self.print_slow(f"Name: {self.player.name}")
        self.print_slow(f"Health: {self.player.health}/{self.player.max_health}")
        self.print_slow(f"Coins: {self.player.coins}")
        self.print_slow(f"Level: {self.player.level}")
        self.print_slow(f"Experience: {self.player.experience}")
        
        if self.player.equipped_weapon:
            self.print_slow(f"Equipped Weapon: {self.player.equipped_weapon.name}")
        if self.player.equipped_armor:
            self.print_slow(f"Equipped Armor: {self.player.equipped_armor.name}")
        
        return True
    
    def save_game(self) -> bool:
        """Save the current game state"""
        try:
            if not self.player:
                self.print_slow("Player not found.")
                return False
            
            room = self.world.get_room(self.current_room_id) if self.world else None
            save_data = {
                'player': self.player.to_dict(),
                'current_room': self.current_room_id,
                'game_over': self.game_over,
                'rooms_state': {room_id: room.items for room_id, room in self.world.rooms.items()},
            }

            with open(self.save_file, 'w') as f:
                json.dump(save_data, f, indent=2)
            
            self.print_slow("Game saved successfully!")
            return True
        except Exception as e:
            self.print_slow(f"Failed to save game: {e}")
            return False
    
    def load_game(self) -> bool:
        """Load a saved game"""
        try:
            if not self.player:
                self.print_slow("Player not found.")
                return False
            
            if not os.path.exists(self.save_file):
                return False
            
            with open(self.save_file, 'r') as f:
                save_data = json.load(f)
            
            self.player = Player.from_dict(save_data['player'], self.world.items_database)
            self.current_room_id = save_data['current_room']
            self.game_over = save_data['game_over']
            # Restore all rooms' items
            rooms_state = save_data.get('rooms_state', {})
            for room_id, items in rooms_state.items():
                if room_id in self.world.rooms:
                    self.world.rooms[room_id].items = items
            
            self.print_slow("Game loaded successfully!")
            return True
        except Exception as e:
            self.print_slow(f"Failed to load game: {e}")
            return False
    
    def process_command(self, command: str) -> bool:
        """Process player commands"""
        # Movement commands - check if it's a valid exit first
        room = self.world.get_room(self.current_room_id)
        if room and command in room.exits:
            return self.process_movement(command)
        elif command in ["north", "south", "east", "west"]:
            return self.process_movement(command)
        
        # Take item command
        elif command.startswith("take "):
            item_name = command[5:]
            return self.process_take(item_name)
        
        # Use item command
        elif command.startswith("use "):
            item_name = command[4:]
            return self.process_use(item_name)
        
        # Combine items command
        elif command.startswith("combine "):
            parts = command.split()
            if len(parts) >= 4:
                # Find the "with" keyword
                with_index = -1
                for i, part in enumerate(parts):
                    if part == "with":
                        with_index = i
                        break
                
                if with_index > 1 and with_index < len(parts) - 1:
                    item1_name = " ".join(parts[1:with_index])
                    item2_name = " ".join(parts[with_index + 1:])
                    return self.process_combine(item1_name, item2_name)
            
            self.print_slow("Usage: combine [item1] with [item2]")
            return True
        
        # Save command
        elif command == "save":
            return self.save_game()
        
        # Load command
        elif command == "load":
            return self.load_game()
        
        # Attack command
        elif command.startswith("attack "):
            enemy_name = command[7:]
            return self.process_attack(enemy_name)
        
        # Equip command
        elif command.startswith("equip "):
            item_name = command[6:]
            return self.process_equip(item_name)
        
        # Unequip command
        elif command.startswith("unequip "):
            item_type = command[8:]
            return self.process_unequip(item_type)
        
        # Shop command
        elif command == "shop":
            return self.process_shop()
        
        # Buy command
        elif command.startswith("buy "):
            item_name = command[4:]
            return self.process_buy(item_name)
        
        # Sell command
        elif command.startswith("sell "):
            item_name = command[5:]
            return self.process_sell(item_name)
        
        # Inventory command
        elif command == "inventory":
            return self.process_inventory()
        
        # Examine command
        elif command.startswith("examine "):
            item_name = command[8:]
            return self.process_examine(item_name)
        
        # Status command
        elif command == "status":
            return self.process_status()
        
        # Look command
        elif command == "look":
            self.show_room()
            return True
        
        # Save command
        elif command == "save":
            return self.save_game()
        
        # Load command
        elif command == "load":
            return self.load_game()
        
        # Help command
        elif command == "help":
            self.print_slow("Available commands:")
            self.print_slow("- north, south, east, west: Move in that direction")
            self.print_slow("- take [item]: Pick up an item")
            self.print_slow("- use [item]: Use an item from your inventory")
            self.print_slow("- combine [item1] with [item2]: Combine two items")
            self.print_slow("- attack [enemy]: Attack an enemy")
            self.print_slow("- equip [item]: Equip a weapon or armor")
            self.print_slow("- unequip [weapon/armor]: Unequip an item")
            self.print_slow("- examine [item]: Examine an item in detail")
            self.print_slow("- look: Look around the current room")
            self.print_slow("- inventory: Check your inventory")
            self.print_slow("- status: Check your character status")
            self.print_slow("- shop: Check the shop inventory")
            self.print_slow("- buy [item_name]: Buy an item from the shop")
            self.print_slow("- save: Save your game")
            self.print_slow("- load: Load a saved game")
            self.print_slow("- quit: End the game")
            return True
        
        # Quit command
        elif command == "quit":
            self.print_slow("Thanks for playing! Goodbye!")
            self.game_over = True
            return True
        
        else:
            self.print_slow("I don't understand that command. Type 'help' for available commands.")
            return True
    
    def play(self) -> None:
        """Main game loop"""
        # Try to load existing save
        if not self.load_game():
            self.get_player_name()
        
        while not self.game_over:
            self.show_room()
            command = self.get_command()
            self.process_command(command)
            
            # Add some delay for better pacing
            time.sleep(0.5) 