# --- Levels ---
lvls = {
    "halls": {
        "description": "ddd",
        "items_in_room": [
            {"name": "Torch", "type": "tool", "description": "Lights up dark places."},
            {"name": "Apple", "type": "food", "description": "Restores a small amount of health."},
            {"name": "key", "type": "tool", "description": "Opens a locked door."},
        ],
        "exits": [
            {"direction": "east", "name": "kitchen", "locked": True}
        ]
    },
    "kitchen": {
        "description": "ffff",
        "items_in_room": [
            {"name": "Torch2", "type": "tool", "description": "Lights up dark places."},
            {"name": "Apple2", "type": "food", "description": "Restores a small amount of health."},
            {"name": "key2", "type": "tool", "description": "Opens a locked door."},
        ],
        "exits": [
            {"direction": "west", "name": "halls", "locked": False},
            {"direction": "north", "name": "garden", "locked": False}
        ]
    },
    "garden": {
            "description": "gggg",
            "items_in_room": [
                {"name": "Torch3", "type": "tool", "description": "Lights up dark places."},
                {"name": "Apple3", "type": "food", "description": "Restores a small amount of health."},
                {"name": "key3", "type": "tool", "description": "Opens a locked door."},
            ],
            "exits": [
                {"direction": "south", "name": "kitchen", "locked": False}
            ]
    }
}

# --- Item_Key ---
item_key = {
    # cell    item    locked cell
    ("halls", "key"): "east"
}