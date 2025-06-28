from typing import Dict, Any, Optional
from item import Item

class Player:
    """Represents the player character"""
    def __init__(self, name: str):
        self.name = name
        self.max_health = 100
        self.health = 100
        self.coins = 0
        self.experience = 0
        self.level = 1
        self.equipped_weapon: Optional[Item] = None
        self.equipped_armor: Optional[Item] = None
        self.inventory: Dict[str, Item] = {}
        self.base_damage = 5

    def take_damage(self, damage: int) -> int:
        actual_damage = min(damage, self.health)
        self.health -= actual_damage
        return actual_damage

    def heal(self, amount: int) -> int:
        actual_healing = min(amount, self.max_health - self.health)
        self.health += actual_healing
        return actual_healing

    def add_item(self, item: Item) -> None:
        if item.item_id in self.inventory:
            self.inventory[item.item_id].quantity += item.quantity
        else:
            self.inventory[item.item_id] = item

    def remove_item(self, item_id: str, quantity: int = 1) -> bool:
        if item_id in self.inventory:
            if self.inventory[item_id].quantity <= quantity:
                del self.inventory[item_id]
            else:
                self.inventory[item_id].quantity -= quantity
            return True
        return False

    def has_item(self, item_id: str) -> bool:
        return item_id in self.inventory

    def get_attack_damage(self) -> int:
        damage = self.base_damage
        if self.equipped_weapon:
            damage += self.equipped_weapon.damage
        return damage

    def equip_item(self, item_id: str) -> bool:
        if not self.has_item(item_id):
            return False
        item = self.inventory[item_id]
        if item.item_type == "weapon":
            self.equipped_weapon = item
            return True
        elif item.item_type == "armor":
            self.equipped_armor = item
            return True
        return False

    def unequip_item(self, item_type: str) -> bool:
        if item_type == "weapon" and self.equipped_weapon:
            self.equipped_weapon = None
            return True
        elif item_type == "armor" and self.equipped_armor:
            self.equipped_armor = None
            return True
        return False

    def add_experience(self, amount: int) -> None:
        self.experience += amount
        new_level = (self.experience // 100) + 1
        if new_level > self.level:
            self.level = new_level
            self.max_health += 10
            self.health = self.max_health
            self.base_damage += 2

    def to_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'max_health': self.max_health,
            'health': self.health,
            'coins': self.coins,
            'experience': self.experience,
            'level': self.level,
            'equipped_weapon': self.equipped_weapon.item_id if self.equipped_weapon else None,
            'equipped_armor': self.equipped_armor.item_id if self.equipped_armor else None,
            'inventory': {item_id: item.to_dict() for item_id, item in self.inventory.items()}
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any], item_database: Dict[str, Item]) -> 'Player':
        player = cls(data['name'])
        player.max_health = data['max_health']
        player.health = data['health']
        player.coins = data['coins']
        player.experience = data['experience']
        player.level = data['level']
        if data['equipped_weapon']:
            player.equipped_weapon = item_database[data['equipped_weapon']]
        if data['equipped_armor']:
            player.equipped_armor = item_database[data['equipped_armor']]
        for item_id, item_data in data['inventory'].items():
            player.inventory[item_id] = Item.from_dict(item_data)
        return player 