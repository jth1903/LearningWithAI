from typing import Dict, Any

class Item:
    """Represents an item in the game"""
    def __init__(self, item_id: str, name: str, description: str, item_type: str, 
                 rarity: str, combinable: bool = False, **kwargs):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.item_type = item_type
        self.rarity = rarity
        self.combinable = combinable
        self.quantity = 1
        self.durability = kwargs.get('durability', 100)
        self.max_durability = kwargs.get('durability', 100)
        self.damage = kwargs.get('damage', 0)
        self.value = kwargs.get('value', 0)
        self.healing = kwargs.get('healing', 0)
        for key, value in kwargs.items():
            if not hasattr(self, key):
                setattr(self, key, value)

    def to_dict(self) -> Dict[str, Any]:
        return {
            'item_id': self.item_id,
            'name': self.name,
            'description': self.description,
            'item_type': self.item_type,
            'rarity': self.rarity,
            'combinable': self.combinable,
            'quantity': self.quantity,
            'durability': self.durability,
            'max_durability': self.max_durability,
            **{k: v for k, v in self.__dict__.items() 
               if k not in ['item_id', 'name', 'description', 'item_type', 'rarity', 'combinable', 'quantity', 'durability', 'max_durability']}
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Item':
        item = cls(
            item_id=data['item_id'],
            name=data['name'],
            description=data['description'],
            item_type=data['item_type'],
            rarity=data['rarity'],
            combinable=data['combinable']
        )
        item.quantity = data.get('quantity', 1)
        item.durability = data.get('durability', 100)
        item.max_durability = data.get('max_durability', 100)
        for key, value in data.items():
            if key not in ['item_id', 'name', 'description', 'item_type', 'rarity', 'combinable', 'quantity', 'durability', 'max_durability']:
                setattr(item, key, value)
        return item 