import time
import random

class AdventureGame:
    def __init__(self):
        self.player_name = ""
        self.player_coin = 0
        self.player_health = 100  # Add player health
        self.equipped_weapon = {
            "name": "none",
            "damage": 0,
            "durability": 0,
            "type": "weapon",
            "rarity": "none",
        }
        self.current_room = "entrance"
        self.inventory = {}
        self.game_over = False
        
        self.items = {
            "legendary_sword": {
                "name": "Legendary Sword",
                "description": "A gleaming sword with ancient runews etched into its blade",
                "damage": 25,
                "durability": 100,
                "type": "weapon",
                "rarity": "Epic",
                "value": 100,
                "combinable": False
            },
            "gold_coin": {
                "name": "gold coin",
                "description": "A small gold coin used for currency and rituals",
                "type": "item",
                "rarity": "uncommon",
                "value": 1,
                "combinable": True
            },
            "ancient_key": {
                "name": "ancient key",
                "description": "a strange key with no head, and what looks like groves on the top",
                "type": "item",
                "rarity": "uncommon",
                "combinable": True
            },
            "gemstone": {
                "name": "gemstone",
                "description": "A beautiful but unassuming clear gem",
                "type": "item",
                "rarity": "rare",
                "reflective_quality": 50,
                "value": 25,
                "combinable": True
            },
            "torch": {
                "name": "torch",
                "description": "A wooden torch with a metal handle",
                "type": "item",
                "rarity": "common",
                "combinable": True,
                "light_radius": 3,
                "value": 5
            },
            "mysterious_artifact": {
                "name": "mysterious artifact",
                "description": "A strange artifact with a glowing core",
                "type": "item",
                "rarity": "rare",
                "combinable": True
            },
            "staff_of_light": {
                "name": "staff of light",
                "description": "A staff with a glowing core",
                "light_radius": 5,
                "damage": 15,
                "durability": 100,
                "type": "weapon",
                "rarity": "legendary",
                "combinable": True
            },
            "enchanted_coin": {
                "name": "enchanted coin",
                "description": "A coin that seems to have been imbued with magical energy",
                "type": "item",
                "rarity": "rare",
                "combinable": True
            },
            "luminary": {
                "name": "luminary",
                "description": "A glowing abnormality that seems to emit a soft, warm light, it seems to be a glowing orb that shifts between solid and trasparent",
                "type": "item",
                "rarity": "rare",
                "combinable": True,
                "light_radius": 5,
                "damage": 15,
                "durability": 100,
                "type": "weapon",
                "rarity": "legendary",
                "combinable": True
            },
            "luminary_key": {
                "name": "luminary key",
                "description": "A key that seems to be made of a strange metal, it has a strange symbol on it",
                "type": "item",
                "rarity": "rare",
                "combinable": True
            },
            "luminary_glow": {
                "name": "luminary glow",
                "description": "A glowing orb that seems to emit a soft, warm light, it seems to be a glowing orb that shifts between solid and trasparent",
                "type": "item",
                "rarity": "rare",
                "combinable": True
            },
            "staff_of_the_light_mage": {
                "name": "staff of the light mage",
                "description": "A staff with a glowing core. It seems to radiate light and energy",
                "light_radius": 5,
                "damage": 15,
                "durability": 100,
                "reflective_quality": 100,
                "type": "weapon",
                "rarity": "legendary",
                "value": 1000,
                "combinable": False
            },
            "iron_sword": {
                "name": "iron sword",
                "description": "A sturdy iron sword with a sharp blade",
                "damage": 15,
                "durability": 80,
                "type": "weapon",
                "rarity": "common",
                "value": 50,
                "combinable": False
            },
            "steel_axe": {
                "name": "steel axe",
                "description": "A heavy steel axe that packs a powerful punch",
                "damage": 20,
                "durability": 90,
                "type": "weapon",
                "rarity": "uncommon",
                "value": 75,
                "combinable": False
            },
            "magic_dagger": {
                "name": "magic dagger",
                "description": "A mystical dagger that glows with magical energy",
                "damage": 18,
                "durability": 70,
                "type": "weapon",
                "rarity": "rare",
                "value": 120,
                "combinable": False
            }
        }

        # Define the game world
        self.rooms = {
            "entrance": {
                "description": "You stand at the entrance of a mysterious cave. The air is cool and damp. You can see two paths ahead.",
                "exits": {"north": "main_cavern", "east": "treasure_room"},
                "items": ["torch"]
            },
            "main_cavern": {
                "description": "You're in a large cavern with stalactites hanging from the ceiling. Water drips somewhere in the darkness.",
                "exits": {"south": "entrance", "west": "dark_tunnel"},
                "items": ["gold_coin"]
            },
            "treasure_room": {
                "description": "A small chamber with ancient markings on the walls. There's a chest in the corner!",
                "exits": {"west": "entrance"},
                "items": ["ancient_key", "gemstone"]
            },
            "hidden_passage": {
                "description": "As you enter the doorway, you hear a faint growl.",
                "exits": {},
                "enemys": { "orc":{
                    "name": "orc",
                    "health": 100,
                    "damage": 10,
                    "description": "A large orc with a large axe"
                }},
                "items": ["torch"]
            },
            "dark_tunnel": {
                "description": "A narrow, dark tunnel. You can barely see your hand in front of your face.",
                "exits": {"east": "main_cavern", "west": "cave_clearing"},
                "items": ["mysterious_artifact"]
            },
            "cave_clearing": {
                "description": "A large opening in the cave there are random things strowed all over. You see a glowing staff on the ground with the words 'staff_of_light' engraved on the hilt",
                "exits": {"east": "dark_tunnel"},
                "items": ["staff_of_light"]
            },
            "field": {
                "description": "You are in a field.",
                "exits": {"south": "hidden_passage", "north": "village_entrence"},
                "items": []
            },
            "village_entrence": {
                "description": "You are standing in front of a large archway that seems to have a trail leading into a village.",
                "exits": {"south": "field", "north": "village_courtyard"},
                "items": []
            },
            "village_courtyard": {
                "description": "You are standing in a large courtyard with a three-tier fountain in the middle with shops to the east and west.",
                "exits": {"east": "general_goods", "west": "weapons_shop", "south": "village_entrence"},
                "items": []
            },
            "weapons_shop": {
                "descripton": "You walk into a well furnished shop with several weapons on display. The shopkeeper is excited to meet a new customer.",
                "exits": {"east": "village_courtyard"},
                "shop_items": {
                    "iron_sword": {"price": 50, "quantity": 3},
                    "steel_axe": {"price": 75, "quantity": 2},
                    "magic_dagger": {"price": 120, "quantity": 1}
                }
            }
        }
    
    def print_slow(self, text, delay=0.03):
        """Print text with a typewriter effect"""
        is_typing = True
        if is_typing:
            for char in text:
                print(char, end='', flush=True)
                time.sleep(delay)
            print()
            is_typing = False
    
    def get_player_name(self):
        """Get the player's name"""
        self.print_slow("Welcome to the Cave of Mysteries!")
        self.print_slow("What is your name, brave adventurer?")
        self.player_name = input("> ").strip()
        if not self.player_name:
            self.player_name = "Adventurer"
        self.print_slow(f"Welcome, {self.player_name}! Your adventure begins...")
    
    def show_room(self):
        """Display current room information"""
        room = self.rooms[self.current_room]
        print("\n" + "="*50)
        self.print_slow(room["description"])
        
        # Show player status
        self.print_slow(f"Health: {self.player_health} | Coins: {self.player_coin}")
        
        # Show available exits
        exits = list(room["exits"].keys())
        self.print_slow(f"Exits: {', '.join(exits)}")
        
        # Show items in room
        if room["items"]:
            self.print_slow(f"You see: {', '.join(room['items'])}")
        
        # Show inventory
        if self.inventory:
            self.print_slow(f"Your inventory: {', '.join(self.inventory)}")
    
    def get_command(self):
        """Get and process player command"""
        self.print_slow("\nWhat would you like to do?")
        command = input("> ").lower().strip()
        return command
    
    def combine_items(self, first_item, second_item):
        """Combine two items to create a new item"""
        # Define possible combinations
        combinations = {
            ("gold_coin", "gemstone"): "enchanted_coin",
            ("enchanted_coin", "mysterious_artifact"): "luminary",
            ("luminary", "ancient_key"): "luminary_key",
            ("luminary_key", "torch"): "luminary_glow",
            ("luminary_glow", "staff_of_light"): "staff_of_the_light_mage"
        }

        # Check both orders (item1+item2 and item2+item1)
        if(first_item, second_item) in combinations:
            return combinations[(first_item, second_item)]
        elif (second_item, first_item) in combinations:
            return combinations[(second_item, first_item)]
        else:
            return None

    def attack_enemy(self, enemy):
        self.equipped_weapon = self.items["legendary_sword"]
        if self.equipped_weapon:
            damage = self.equipped_weapon["damage"]
            self.print_slow(f"you attack the {enemy['name']} with your {self.equipped_weapon['name']}")
            self.print_slow(f"You deal {damage} damage!")
            enemy["health"] -= damage
            self.print_slow(f"The {enemy['name']} has {enemy['health']} health remaining.")
            if enemy["name"] == "orc" and enemy["health"] <= 0:
                self.print_slow("You have defeated the orc!")
                self.rooms[self.current_room]["enemys"].pop("orc")
                self.rooms[self.current_room]["exits"]["north"] = "field"
                return True
            # Orc retaliates if still alive
            if enemy["name"] == "orc" and enemy["health"] > 0:
                self.orc_attack(enemy)
            return False

    def orc_attack(self, enemy):
        # Orc has a 70% chance to hit
        hit_chance = random.random()
        if hit_chance < 0.7:
            damage = enemy.get("damage", 10)
            self.player_health -= damage
            self.print_slow(f"The {enemy['name']} attacks you and deals {damage} damage!")
            self.print_slow(f"You have {self.player_health} health remaining.")
            if self.player_health <= 0:
                self.print_slow("You have been defeated by the orc! Game over.")
                self.game_over = True
        else:
            self.print_slow(f"The {enemy['name']} swings at you but misses!")

    def process_command(self, command):
        """Process player commands"""
        room = self.rooms[self.current_room]
        
        # Movement commands
        if command in room["exits"]:
            self.current_room = room["exits"][command]
            self.print_slow(f"You move {command}...")
            return True
        
        # Combine Items
        elif command.startswith("combine "):
            # Parse he command: "combine item1 with item2"
            parts = command.split()
            if len(parts) >= 4 and parts[2] == "with":
                item1 = parts[1]
                item2 = " ".join(parts[3:]) # Handle multi-word items

                if item1 in self.inventory and item2 in self.inventory:
                    new_item = self.combine_items(item1, item2)
                    if new_item:
                        del self.inventory[item1]
                        del self.inventory[item2]
                        self.inventory[new_item] = True
                        self.print_slow(f"You successfully combine {item1} and {item2} to create {new_item}")
                    else:
                        self.print_slow(f"you can't combine {item1} and {item2}.")
                else:
                    self.print_slow(f"You don't have both items in your inventory.")
            else:
                self.print_slow("Usage:combine [item1] with [item2].")
            return True


        # Take item command
        elif command.startswith("take "):
            item = command[5:]
            if item in room["items"]:
                room["items"].remove(item)
                self.inventory[item] = True
                if item in self.items:
                    item_info = self.items[item]
                    self.print_slow(f"You picked up the {item_info['name']}!")
                    self.print_slow(f"Description: {item_info['description']}")
                    self.print_slow(f"Combinable: {item_info['combinable']}")
                    
                    # Give coins for gold coins
                    if item == "gold_coin":
                        self.player_coin += item_info.get("value", 1)
                        self.print_slow(f"You gained {item_info.get('value', 1)} coin!")
                else:
                    self.print_slow(f"You picked up the {item}.")
            else:
                self.print_slow("You don't see that here.")
            return True

        elif command.startswith("attack "):
            enemy_name = command[7:]  # Extract enemy name from "attack [enemy]"
            if "enemys" in self.rooms[self.current_room] and enemy_name in self.rooms[self.current_room]["enemys"]:
                self.attack_enemy(self.rooms[self.current_room]["enemys"][enemy_name])
            else:
                self.print_slow(f"There's no {enemy_name} here to attack.")
            return True
        
        # Use item command
        elif command.startswith("use "):
            item = command[4:]
            if item in self.inventory:
                self.print_slow(f"You use the {item}...")
                # Add special item interactions here
                if item == "torch" and self.current_room == "dark_tunnel":
                    self.print_slow("The torch illuminates the tunnel! You can see ancient writings on the walls.")
                elif item == "torch" and self.current_room == "hidden_passage":
                    self.print_slow("The hidden room lights up from the torch and you see a giant orc blocking the north exit")
                elif item == "ancient_key" and self.current_room == "treasure_room":
                    self.print_slow("The key fits perfectly in the chest! You found a legendary sword!")
                    self.inventory["legendary_sword"] = True
                elif item == "staff_of_the_light_mage" and self.current_room == "treasure_room":
                    self.print_slow("You raise the Staff of the Light Mage. A beam of light shoots from its tip, illuminating a hidden panel in the wall.")
                    self.print_slow("With a rumble, the panel slides open, revealing a hidden passage leading deeper into the unknown...")
                    # Optionally, you could unlock a new room or set a flag here
                    self.rooms["treasure_room"]["exits"]["ancient_door"] = "hidden_passage"
                else:
                    self.print_slow("Nothing special happens.")
            else:
                self.print_slow("You don't have that item.")
            return True
        
        # Look command
        elif command == "look":
            self.show_room()
            return True
        

        # Inventory command
        elif command == "inventory":
            if self.inventory:
                self.print_slow(f"Your inventory: {', '.join(self.inventory)}")
            else:
                self.print_slow("Your inventory is empty.")
            return True
        
        # Status command
        elif command == "status":
            self.print_slow(f"Health: {self.player_health}")
            self.print_slow(f"Coins: {self.player_coin}")
            if self.inventory:
                self.print_slow(f"Inventory: {', '.join(self.inventory)}")
            else:
                self.print_slow("Inventory: Empty")
            return True
        
        # Shop command
        elif command == "shop":
            if "shop_items" in room:
                self.print_slow("Welcome to the shop! Here's what we have for sale:")
                self.print_slow(f"Your coins: {self.player_coin}")
                for item_id, shop_data in room["shop_items"].items():
                    if item_id in self.items:
                        item_info = self.items[item_id]
                        self.print_slow(f"- {item_info['name']}: {shop_data['price']} coins (Quantity: {shop_data['quantity']})")
                        self.print_slow(f"  Description: {item_info['description']}")
                        self.print_slow(f"  Damage: {item_info.get('damage', 0)}")
                self.print_slow("Use 'buy [item_name]' to purchase an item.")
            else:
                self.print_slow("There's no shop here.")
            return True
        
        # Buy command
        elif command.startswith("buy "):
            if "shop_items" in room:
                item_name = command[4:].lower()
                # Find the item in shop_items
                item_found = None
                for item_id, shop_data in room["shop_items"].items():
                    if self.items[item_id]["name"].lower() == item_name:
                        item_found = (item_id, shop_data)
                        break
                
                if item_found:
                    item_id, shop_data = item_found
                    if shop_data["quantity"] > 0:
                        if self.player_coin >= shop_data["price"]:
                            self.player_coin -= shop_data["price"]
                            shop_data["quantity"] -= 1
                            self.inventory[item_id] = True
                            self.print_slow(f"You bought {self.items[item_id]['name']} for {shop_data['price']} coins!")
                            self.print_slow(f"You have {self.player_coin} coins remaining.")
                        else:
                            self.print_slow(f"You don't have enough coins. You need {shop_data['price']} coins but have {self.player_coin}.")
                    else:
                        self.print_slow("Sorry, that item is out of stock.")
                else:
                    self.print_slow("That item is not available in this shop.")
            else:
                self.print_slow("There's no shop here.")
            return True
        
        # Help command
        elif command == "help":
            self.print_slow("Available commands:")
            self.print_slow("- north, south, east, west: Move in that direction")
            self.print_slow("- take [item]: Pick up an item")
            self.print_slow("- use [item]: Use an item from your inventory")
            self.print_slow("- combine [item1] with [item2]: Combine two items")
            self.print_slow("- attack [enemy]: Attack an enemy")
            self.print_slow("- look: Look around the current room")
            self.print_slow("- inventory: Check your inventory")
            self.print_slow("- status: Check your health, coins, and inventory")
            self.print_slow("- shop: Check the shop inventory")
            self.print_slow("- buy [item_name]: Buy an item from the shop")
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
    
    def play(self):
        """Main game loop"""
        self.get_player_name()
        
        while not self.game_over:
            self.show_room()
            command = self.get_command()
            self.process_command(command)
            
            # Add some delay for better pacing
            time.sleep(0.5)

# Start the game
if __name__ == "__main__":
    game = AdventureGame()
    game.play() 