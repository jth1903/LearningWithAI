from typing import Dict, Any
import random

class Enemy:
    """Represents an enemy in the game"""
    def __init__(self, name: str, health: int, damage: int, description: str, **kwargs):
        self.name = name
        self.max_health = health
        self.health = health
        self.damage = damage
        self.description = description
        self.attack_chance = kwargs.get('attack_chance', 0.7)
        self.critical_chance = kwargs.get('critical_chance', 0.1)
        self.critical_multiplier = kwargs.get('critical_multiplier', 2.0)
        for key, value in kwargs.items():
            if not hasattr(self, key):
                setattr(self, key, value)

    def is_alive(self) -> bool:
        return self.health > 0

    def take_damage(self, damage: int) -> int:
        actual_damage = min(damage, self.health)
        self.health -= actual_damage
        return actual_damage

    def attack(self, target) -> Dict[str, Any]:
        if random.random() < self.attack_chance:
            damage = self.damage
            is_critical = random.random() < self.critical_chance
            if is_critical:
                damage = int(damage * self.critical_multiplier)
            target.take_damage(damage)
            return {
                'hit': True,
                'damage': damage,
                'critical': is_critical,
                'target_health': target.health
            }
        else:
            return {'hit': False, 'damage': 0, 'critical': False} 