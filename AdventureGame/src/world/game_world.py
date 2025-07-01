from typing import Dict, Optional
from ..core import Item, Enemy, Room

class GameWorld:
    """Manages the game world and data"""
    def __init__(self):
        self.items_database = self._create_items_database()
        self.rooms = self._create_rooms()
        self.combinations = self._create_combinations()
    
    def _create_items_database(self) -> Dict[str, Item]:
        """Create the items database"""
        items_data = {
            "legendary_sword": {
                "name": "Legendary Sword",
                "description": "A gleaming sword with ancient runes etched into its blade",
                "damage": 25,
                "durability": 100,
                "type": "weapon",
                "rarity": "Epic",
                "value": 100,
                "combinable": False
            },
            "Coin_Pouch": {
                "name": "Coin Pouch",
                "description": "A small pouch for storing coins",
                "type": "item",
                "rarity": "common",
                "value": 1,
                "combinable": True,
                "coins_in_pouch": 0,
                "max_coins_in_pouch": 100
            },
            "gold_coin": {
                "name": "Gold Coin",
                "description": "A small gold coin used for currency and rituals",
                "type": "item",
                "rarity": "uncommon",
                "value": 1,
                "combinable": True
            },
            "ancient_key": {
                "name": "Ancient Key",
                "description": "A strange key with no head, and what looks like grooves on the top",
                "type": "item",
                "rarity": "uncommon",
                "combinable": True
            },
            "gemstone": {
                "name": "Gemstone",
                "description": "A beautiful but unassuming clear gem",
                "type": "item",
                "rarity": "rare",
                "reflective_quality": 50,
                "value": 25,
                "combinable": True
            },
            "torch": {
                "name": "Torch",
                "description": "A wooden torch with a metal handle",
                "type": "item",
                "rarity": "common",
                "combinable": True,
                "light_radius": 3,
                "value": 5
            },
            "mysterious_artifact": {
                "name": "Mysterious Artifact",
                "description": "A strange artifact with a glowing core",
                "type": "item",
                "rarity": "rare",
                "combinable": True
            },
            "staff_of_light": {
                "name": "Staff of Light",
                "description": "A staff with a glowing core",
                "light_radius": 5,
                "damage": 15,
                "durability": 100,
                "type": "weapon",
                "rarity": "legendary",
                "combinable": True
            },
            "enchanted_coin": {
                "name": "Enchanted Coin",
                "description": "A coin that seems to have been imbued with magical energy",
                "type": "item",
                "rarity": "rare",
                "combinable": True
            },
            "luminary": {
                "name": "Luminary",
                "description": "A glowing abnormality that seems to emit a soft, warm light, it looks like a glowing orb that shifts between solid and transparent",
                "type": "item",
                "rarity": "rare",
                "light_radius": 5,
                "damage": 15,
                "durability": 100,
                "combinable": True
            },
            "luminary_key": {
                "name": "Luminary Key",
                "description": "A key that seems to be made of a strange metal, it has a strange symbol on it",
                "type": "item",
                "rarity": "rare",
                "combinable": True
            },
            "luminary_glow": {
                "name": "Luminary Glow",
                "description": "A glowing orb that seems to emit a soft, warm light, it seems to be a glowing orb that shifts between solid and transparent",
                "type": "item",
                "rarity": "rare",
                "combinable": True
            },
            "staff_of_the_light_mage": {
                "name": "Staff of the Light Mage",
                "description": "A staff with a glowing core. It seems to radiate light and energy",
                "light_radius": 5,
                "damage": 50,
                "durability": 100,
                "reflective_quality": 100,
                "type": "weapon",
                "rarity": "legendary",
                "value": 100,
                "combinable": False
            },
            "iron_sword": {
                "name": "Iron Sword",
                "description": "A sturdy iron sword with a sharp blade",
                "damage": 15,
                "durability": 80,
                "type": "weapon",
                "rarity": "common",
                "value": 50,
                "combinable": False
            },
            "steel_axe": {
                "name": "Steel Axe",
                "description": "A heavy steel axe that packs a powerful punch",
                "damage": 20,
                "durability": 90,
                "type": "weapon",
                "rarity": "uncommon",
                "value": 75,
                "combinable": False
            },
            "magic_dagger": {
                "name": "Magic Dagger",
                "description": "A mystical dagger that glows with magical energy",
                "damage": 18,
                "durability": 70,
                "type": "weapon",
                "rarity": "rare",
                "value": 120,
                "combinable": False
            },
            "health_potion": {
                "name": "Health Potion",
                "description": "A red potion that restores health",
                "type": "consumable",
                "rarity": "common",
                "value": 10,
                "healing": 30,
                "combinable": False
            },
            "torn_page_1": {
                "name": "Tattered Page",
                "description": "It reads: 'A coin and a gemstone, together, may reveal something magical...'",
                "type": "item",
                "rarity": "common",
                "combinable": True
            },
            "torn_page_2": {
                "name": "Tattered Page",
                "description": "It reads: 'The enchanted coin and a mysterious artifact shine with a new light.'",
                "type": "item",
                "rarity": "common",
                "combinable": True
            },
            "torn_page_3": {
                "name": "Tattered Page",
                "description": "It reads: 'The luminary is but a piece of the key.'",
                "type": "item",
                "rarity": "common",
                "combinable": True
            },
            "torn_page_4": {
                "name": "Tatered Page",
                "description": "It reads: 'A key in the darkness that reflects, seems to need aditional light.",
                "type": "item",
                "rarity": "common",
                "combinable": True
            },
            "torn_page_5": {
                "name": "Tattered Page",
                "description": "It reads: 'An ancient staff..., seems dim, perhaps the glow will help",
                "type": "item",
                "rarity": "common",
                "combinable": True
            }
        }   
        
        items = {}
        for item_id, data in items_data.items():
            # Fix the type mapping
            item_data = data.copy()
            if "type" in item_data:
                item_data["item_type"] = item_data.pop("type")
            items[item_id] = Item(item_id, **item_data)
        
        return items
    
    def _create_rooms(self) -> Dict[str, Room]:
        """Create the game rooms"""
        rooms_data = {
            "entrance": {
                "name": "Entrance",
                "description": "You stand at the entrance of a mysterious cave. The air is cool and damp. You can see two paths ahead.",
                "exits": {"north": "main_cavern", "east": "treasure_room"},
                "items": ["torch", "torn_page_1"],
                "visited": False
            },
            "main_cavern": {
                "name": "Main Cavern",
                "description": "You're in a large cavern with stalactites hanging from the ceiling. Water drips somewhere in the darkness.",
                "exits": {"south": "entrance", "west": "dark_tunnel"},
                "items": ["gold_coin", "torn_page_2"],
                "visited": False
            },
            "treasure_room": { 
                "name": "Treasure Room",
                "description": "A small chamber with ancient markings on the walls. There's a chest in the corner!",
                "exits": {"west": "entrance"},
                "items": ["ancient_key", "gemstone", "torn_page_3"],
                "visited": False
            },
            # Change this name to something more fitting for the room. this is not a door it is a room after the door
            "ancient_door": {
                "name": "Ancient Door",
                "description": "As you enter the doorway, you hear a faint growl.",
                "exits": {},
                "enemies": {"orc": Enemy("orc", 100, 10, "A large orc with a large axe")},
                "items": ["torch"],
                "visited": False
            },
            "dark_tunnel": {
                "name": "Dark Tunnel",
                "description": "A narrow, dark tunnel. You can barely see your hand in front of your face.",
                "exits": {"east": "main_cavern", "west": "cave_clearing"},
                "items": ["mysterious_artifact", "torn_page_4"],
                "visited": False
            },
            "cave_clearing": {
                "name": "Cave Clearing",
                "description": "A large opening in the cave there are random things strewn all over. You see a glowing staff on the ground with the words 'staff_of_light' engraved on the hilt",
                "exits": {"east": "dark_tunnel"},
                "items": ["staff_of_light", "torn_page_5"],
                "visited": False
            },
            "field": {
                "name": "Field",
                "description": "You are in a field.",
                "exits": {"south": "ancient_door", "north": "village_entrance"},
                "items": [],
                "visited": False
            },
            "village_entrance": {
                "name": "Village Entrance",
                "description": "You are standing in front of a large archway that seems to have a trail leading into a village.",
                "exits": {"south": "field", "north": "village_courtyard"},
                "items": [],
                "visited": False
            },
            "village_courtyard": {
                "name": "Village Courtyard",
                "description": "You are standing in a large courtyard with a three-tier fountain in the middle with shops to the east and west.",
                "exits": {"east": "general_goods", "west": "weapons_shop", "south": "village_entrance"},
                "items": [],
                "visited": False
            },
            "weapons_shop": {
                "name": "Weapons Shop",
                "description": "You walk into a well furnished shop with several weapons on display. The shopkeeper is excited to meet a new customer.",
                "exits": {"east": "village_courtyard"},
                "shop_items": {
                    "iron_sword": {"price": 50, "quantity": 3},
                    "steel_axe": {"price": 75, "quantity": 2},
                    "magic_dagger": {"price": 120, "quantity": 1}
                },
                "visited": False
            },
            "general_goods": {
                "name": "General Goods",
                "description": "You are in a general goods shop. The shopkeeper is excited to meet a new customer.",
                "exits": {"west": "village_courtyard"},
                "shop_items": {
                    "torch": {"price": 5, "quantity": 3},
                    "health_potion": {"price": 10, "quantity": 5}
                },
                "visited": False
            }
        }
        
        rooms = {}
        for room_id, data in rooms_data.items():
            rooms[room_id] = Room(room_id, **data)
        
        return rooms
    
    def _create_combinations(self) -> Dict[tuple, str]:
        """Create item combinations"""
        return {
            ("gold_coin", "gemstone"): "enchanted_coin",
            ("enchanted_coin", "mysterious_artifact"): "luminary",
            ("luminary", "ancient_key"): "luminary_key",
            ("luminary_key", "torch"): "luminary_glow",
            ("luminary_glow", "staff_of_light"): "staff_of_the_light_mage"
        }
    
    def get_item(self, item_id: str) -> Optional[Item]:
        """Get item from database"""
        return self.items_database.get(item_id)
    
    def get_room(self, room_id: str) -> Optional[Room]:
        """Get room by ID"""
        return self.rooms.get(room_id)
    
    def combine_items(self, item1_id: str, item2_id: str) -> Optional[str]:
        """Combine two items and return the result item ID"""
        # Check both orders
        if (item1_id, item2_id) in self.combinations:
            return self.combinations[(item1_id, item2_id)]
        elif (item2_id, item1_id) in self.combinations:
            return self.combinations[(item2_id, item1_id)]
        return None 