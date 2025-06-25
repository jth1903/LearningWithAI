import time
import random

class AdventureGame:
    def __init__(self):
        self.player_name = ""
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
            # Item List: gemstone, torch, mysterious_artifact, staff_of_light, staff_of_the_light_mage,
            # enchanted_coin, luminary, luminary_key, luminary_glow

            "legendary_sword": {
                "name": "Legendary Sword",
                "description": "A gleaming sword with ancient runews etched into its blade",
                "damage": 25,
                "durability": 100,
                "type": "weapon",
                "rarity": "Epic",
                "combinable": False
            },
            "gold_coin": {
                "name": "gold coin",
                "description": "A small gold coin used for currency and rituals",
                "type": "item",
                "rarity": "uncommon",
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
                "combinable": True
            },
            "torch": {
                "name": "torch",
                "description": "A wooden torch with a metal handle",
                "type": "item",
                "rarity": "common",
                "combinable": True,
                "light_radius": 3,
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
                "exits": {"south": "hidden_passage", "north": ""},
                "items": []
            }
        }
    
    def print_slow(self, text, delay=0.03):
        """Print text with a typewriter effect"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
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
            self.print_slow("you attack the {enemy} with your {self.equipped_weapon.name}")
            self.print_slow(f"You deal {damage} damage!")
            enemy["health"] -= damage
            self.print_slow(f"The {enemy['name']} has {enemy['health']} health remaining.")
            if enemy["name"] == "orc" and enemy["health"] <= 0:
                self.print_slow("You have defeated the orc!")
                self.rooms[self.current_room]["enemys"].pop("orc")
                self.rooms[self.current_room]["exits"]["north"] = "field"
                return True

            return False

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
                    self.rooms["treasure_room"]["exits"]["secret"] = "hidden_passage"
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
        
        # Help command
        elif command == "help":
            self.print_slow("Available commands:")
            self.print_slow("- north, south, east, west: Move in that direction")
            self.print_slow("- take [item]: Pick up an item")
            self.print_slow("- use [item]: Use an item from your inventory")
            self.print_slow("- combine [item1] with [item2]: Combine two items")
            self.print_slow("- look: Look around the current room")
            self.print_slow("- inventory: Check your inventory")
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