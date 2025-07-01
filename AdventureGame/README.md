# Adventure Game

A text-based adventure game built in Python with a modular, well-organized codebase.

## 🏗️ Project Structure

```
AdventureGame/
├── src/                    # Main source code
│   ├── core/              # Core game entities
│   │   ├── __init__.py    # Package initialization
│   │   ├── player.py      # Player character class
│   │   ├── enemy.py       # Enemy class and combat
│   │   ├── item.py        # Item system and inventory
│   │   └── room.py        # Room and world navigation
│   ├── engine/            # Game engine and logic
│   │   ├── __init__.py    # Package initialization
│   │   └── game_engine.py # Main game controller
│   ├── world/             # World data and management
│   │   ├── __init__.py    # Package initialization
│   │   └── game_world.py  # Game world data and setup
│   └── utils/             # Utilities and debug tools
│       ├── __init__.py    # Package initialization
│       └── debug_room.py  # Debug utilities
├── main.py                # Entry point
├── requirements.txt       # Dependencies (if any)
└── README.md             # This file
```

## 🎮 How to Play

1. **Start the game**: Run `python main.py`
2. **Enter your name**: When prompted, type your character's name
3. **Explore the world**: Use commands to navigate and interact

### Available Commands

- **Movement**: `north`, `south`, `east`, `west`, `go north`, etc.
- **Items**: `take [item]`, `use [item]`, `examine [item]`, `inventory`
- **Combat**: `attack [enemy]`
- **Equipment**: `equip [item]`, `unequip [weapon/armor]`
- **Game**: `status`, `save`, `load`, `quit`

## 🏛️ Architecture Overview

### Core Classes (`src/core/`)
- **Player**: Manages character stats, inventory, and equipment
- **Enemy**: Handles enemy behavior and combat mechanics
- **Item**: Defines all game items with properties and effects
- **Room**: Represents locations with items, enemies, and exits

### Game Engine (`src/engine/`)
- **GameEngine**: Main controller that processes commands and manages game flow
- Handles all player interactions and world updates

### World Management (`src/world/`)
- **GameWorld**: Contains all game data (items, rooms, enemies)
- Manages item combinations and world state

### Utilities (`src/utils/`)
- **Debug Tools**: Development and testing utilities

## 🚀 Key Features

- **Modular Design**: Easy to extend with new content
- **Save/Load System**: Persistent game state
- **Combat System**: Turn-based combat with critical hits
- **Inventory Management**: Collect, use, and combine items
- **Equipment System**: Weapons and armor with stats
- **Item Combinations**: Craft new items by combining existing ones

## 🔧 Development

### Adding New Content

1. **New Items**: Add to the items database in `src/world/game_world.py`
2. **New Rooms**: Add to the rooms dictionary in `src/world/game_world.py`
3. **New Commands**: Add a new `process_*()` method in `src/engine/game_engine.py`
4. **New Enemies**: Add to the enemy definitions in `src/world/game_world.py`

### Code Organization Benefits

- **Separation of Concerns**: Each module has a clear responsibility
- **Maintainability**: Easy to find and modify specific functionality
- **Extensibility**: New features can be added without affecting existing code
- **Testability**: Each component can be tested independently

## 🎯 Design Patterns

- **Command Pattern**: All actions go through the command processor
- **Data-Driven Design**: Game content is separated from logic
- **Object-Oriented**: Clean class hierarchy with inheritance
- **Modular Architecture**: Loose coupling between components

## 📝 Requirements

- Python 3.7+
- No external dependencies required

## 🎲 Game Features

- Text-based adventure with typewriter effect
- Multiple rooms to explore
- Combat system with enemies
- Item collection and usage
- Equipment system
- Save/load functionality
- Shop system for buying items
- Experience and leveling system 