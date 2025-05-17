# --- Imports ---
from ASCII_arts_col import cells
# --- Levels ---
# -- Ch1 --
lvls = { # Dictionaries are case sensetive, DO NOT USE CAPITAL LETTERS
    "khurik post": { #cell1
        "description": f"---\n{cells.get('khurik post')}\n---\nKhurik post, this is where you were given your order. North path goes through a dark tunnel, \nit is dangerous to go in blind. North-east path leads to ammo warehouse, blocked by rubble and rocks, better not waste time on it.\nEast is where battlefield is.\n",
        "items_in_room": [
            {"name": "Torch", "type": "tool", "description": "Lights up dark places."},
            {"name": "Ration", "type": "food", "description": "Restores health point."},
        ],
        "damage": False,
        "exits": [
            {"direction": "north", "name": "north trenches", "locked": True, "damage": False},
            {"direction": "north-east", "name": "ammo warehouse", "locked": True, "damage": True},
            {"direction": "east", "name": "open battlefield", "locked": False, "damage": True},
        ]
    },
    "ammo warehouse": { #cell1.1
        "description": " ",
        "items_in_room": [],
        "damage": True,
        "exits": [
            {"direction": "south-west", "name": "khurik post", "locked": False, "damage": False},
        ]
    },
    "open battlefield": { #cell1.2
        "description": "It's a dangerous area, easy to catch a stray bullet.",
        "items_in_room": [],
        "damage": True,
        "exits": [
            {"direction": "west", "name": "khurik post", "locked": False, "damage": False},
        ]
    },
    "north trenches": { #cell2
        "description": "North trenches is a long system of trenches and bases around it. \nGoing further north will lead you to Blauvald trenches of east front.",
        "items_in_room": [
            {"name": "Shovel", "type": "tool", "description": "Helps to get rid of dirt and rubble."},
            {"name": "Meds", "type": "food", "description": "Restores health point."},
        ],
        "damage": False,
        "exits": [
            {"direction": "north", "name": "north trenches", "locked": True, "damage": False},
            {"direction": "north-east", "name": "battlefield", "locked": False, "damage": True},
            {"direction": "south", "name": "khurik post", "locked": False, "damage": False}
        ]
    }
}

# --- Item_Key ---
item_key = {
  # cell name;  item   locked cell direction
    ("khurik post", "torch"): "north",
    ("north trenches", "shovel"): "north"
}

