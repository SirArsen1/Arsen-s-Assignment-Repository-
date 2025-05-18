# ---- Locations ----
# --- Character Creation Function ---
from ASCII_arts_col import ascii
from Icon_Picker import p_icon
# --- Cells ---
p_icon = p_icon()
# -- Ch1 --
cell1 = f'''
|   |    /    /
| N |___/ NE /
|   .   .   |______
|   . {p_icon} .   _E_____
|___.,=,.__/'''

cell2 = f'''
| N |___/ NE /
|   .   .   |
| {p_icon}  _______|
/ S /'''

cell3 = f'''
        |   |
    ,___| N |___,
____|   .   .   |____
__W_.   . {p_icon} .   ._E__
    |___.   .___|
        | S |
'''

cells = [cell1, cell2]

# --- Levels ---
lvls = { # Dictionaries are case sensetive, DO NOT USE CAPITAL LETTERS
    "khurik post": { #cell1 # -- Ch1 --
        "description": f"---\nKhurik post, this is where you were given your order. North path goes through a dark tunnel, \nit is dangerous to go in blind. North-east path leads to ammo warehouse, blocked by rubble and rocks, better not waste time on it.\nEast is where battlefield is.\n",
        "items_in_room": [
            {"name": "Lantern", "type": "tool", "art": f"{ascii.get('lantern')}", "description": "Lights up dark places."},
            {"name": "Ration", "type": "food", "art": f" ", "description": "Restores health point."},
        ],
        "cell": cell1,
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
        "cell": " ",
        "damage": True,
        "exits": [
            {"direction": "south-west", "name": "khurik post", "locked": False, "damage": False},
        ]
    },
    "open battlefield": { #cell1.2
        "description": "---\nIt's a dangerous area, easy to catch a stray bullet.\n---",
        "items_in_room": [],
        "cell": " ",
        "damage": True,
        "exits": [
            {"direction": "west", "name": "khurik post", "locked": False, "damage": False},
        ]
    },
    "north trenches": { #cell2
        "description": "---\nNorth trenches is a long system of trenches and bases around it. \nGoing further north will lead you to Blauvald trenches of east front.\n---",
        "items_in_room": [
            {"name": "Shovel", "type": "tool", "art": f"{ascii.get('shovel')}", "description": "Helps to get rid of dirt and rubble."},
            {"name": "Meds", "type": "food", "art": f" ", "description": "Restores health point."},
        ],
        "cell": cell2,
        "damage": False,
        "exits": [
            {"direction": "north", "name": "road to blauvald", "locked": True, "damage": False},
            {"direction": "north-east", "name": "battlefield", "locked": False, "damage": True},
            {"direction": "south", "name": "khurik post", "locked": False, "damage": False},
        ]
    },
    "road to blauvald": { #cell3
        "description": "Trenched checkpoint, that includes underground horse stables. \nYou can take a horse if you find a stable, look for it.",
        "items_in_room": [
            {"name": "Map", "type": "tool", "art": f"{ascii.get('map')}", "description": f"\nMap of eastern north-west Vateria. On the bottom left you see Khurik river, \non the top right mountains of Äscalia and small parts of Bergardia, and Amania.\n"},
            {"name": "Meds", "type": "food", "art": f" ", "description": "Restores health point."},
        ],
        "cell": cell3,
        "damage": False,
        "exits": [
            {"direction": "north", "name": "forests of blauvald", "locked": True, "damage": False},
            {"direction": "east", "name": "battlefield", "locked": False, "damage": True},
            {"direction": "south", "name": "north trenches", "locked": False, "damage": False},
            {"direction": "west", "name": "cannon station", "locked": False, "damage": False}
        ]
    },
    "cannon station": { #cell3.1
        "description": "---\nCannon station helps to defend near bases from enemy flying ships \nor provides support to army on a battlefield.\n---",
        "items_in_room": [
            {"name": "horse saddle", "type": "tool", "art": f" ", "description": "allows to ride a horse."},
        ],
        "cell": " ",
        "damage": True,
        "exits": [
            {"direction": "east", "name": "road to blauvald", "locked": False, "damage": False},
        ]
    },
    "forests of blauvald": { #cell4 # -- ch2 --
        "description": "---\n HI \n---",
        "items_in_room": [
            {"name": "sniper rifle", "type": "tool", "art": f" ", "description": "Rifle that can shoot long distance targets."},
        ],
        "cell": " ",
        "damage": True,
        "exits": [
            {"direction": "east", "name": "road to blauvald", "locked": False, "damage": False},
        ]
    },
}

# --- Item_Key ---
item_key = {
  # cell name;  item   locked cell direction
    ("khurik post", "lantern"): "north",
    ("north trenches", "shovel"): "north",
    ("road to blauvald", "horse saddle"): "north"
}

