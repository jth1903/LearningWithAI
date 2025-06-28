from typing import Dict, List, Optional
from enemy import Enemy

class Room:
    """Represents a room in the game world"""
    def __init__(self, room_id: str, description: str, exits: Dict[str, str], 
                 items: Optional[List[str]] = None, enemies: Optional[Dict[str, Enemy]] = None, 
                 shop_items: Optional[Dict[str, Dict[str, int]]] = None):
        self.room_id = room_id
        self.description = description
        self.exits = exits
        self.items = items or []
        self.enemies = enemies or {}
        self.shop_items = shop_items or {}
        self.visited = False

    def add_item(self, item_id: str) -> None:
        if item_id not in self.items:
            self.items.append(item_id)

    def remove_item(self, item_id: str) -> bool:
        if item_id in self.items:
            self.items.remove(item_id)
            return True
        return False

    def add_enemy(self, enemy: Enemy) -> None:
        self.enemies[enemy.name] = enemy

    def remove_enemy(self, enemy_name: str) -> bool:
        if enemy_name in self.enemies:
            del self.enemies[enemy_name]
            return True
        return False

    def get_enemy(self, enemy_name: str) -> Optional[Enemy]:
        return self.enemies.get(enemy_name)

    def has_enemies(self) -> bool:
        return len(self.enemies) > 0

    def is_shop(self) -> bool:
        return len(self.shop_items) > 0 