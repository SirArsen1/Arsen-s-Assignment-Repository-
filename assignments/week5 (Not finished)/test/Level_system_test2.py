# --- Game State ---
inventory = []
lvls = {
    "halls": {
        "description": "ddd",
        "items_in_room": [
            {"name": "Torch", "type": "tool", "description": "Lights up dark places."},
            {"name": "Apple", "type": "food", "description": "Restores a small amount of health."},
            {"name": "key", "type": "tool", "description": "Opens a locked door."},
        ],
        "exits": {"east": "kitchen"}
    },
    "kitchen": {
        "description": "ffff",
        "items_in_room": [
            {"name": "Torch", "type": "tool", "description": "Lights up dark places."},
            {"name": "Apple", "type": "food", "description": "Restores a small amount of health."},
            {"name": "key", "type": "tool", "description": "Opens a locked door."},
        ],
        "exits": {"west": "halls"}
    }
}

MAX_INVENTORY_SIZE = 5

# Current room
current_room = "halls"
if input() == "use torch":
    current_room = "kitchen"
else: current_room = "halls"
# --- Functions ---

def show_inventory():
    # list all names of items in the inventory, consider the case when the list is empty
    if len(inventory) == 0:
        print("Your inventory is empty.")
    elif len(inventory) == MAX_INVENTORY_SIZE:
        print("Your inventory is full.")
        for items in inventory:
            print(f'{items["name"]} - {items["description"]}')
    else:
        for items in inventory:
            print(f'{items["name"]} - {items["description"]}')
    #pass

def show_room_items():
    # list all items in current room
    items = lvls[current_room]["items_in_room"]
    if len(items) > 0:
        for items in items:
            print(f'{items["name"]} - {items["description"]}')
    else:
        print("There are nothing of use in there.")
    #pass

def pick_up(item_name):
    # pick up an item from the room if inventory limit is not met yet
    items = lvls[current_room]["items_in_room"]
    for item in items:
        if item["name"].lower() == item_name:
            inventory.append(item)
            items.remove(item)
            print(f"You picked up {item['name']}")
            return
    else:
        print("You can't see this item in the room")
    # pass

def drop(item_name):
    # drop an item from your inventory, at the same time append it back to the list of items for the room
    for item in inventory:
        if item["name"].lower() == item_name:
            ["items_in_room"].append(item)
            inventory.remove(item)
            print(f"You dropped {item['name']}")
            return
    else:
        print("You have nothing to drop")
    #pass

def use(item_name):
    # Ex: use the item differently depends on the type
    pass

def examine(item_name):
    # you can only examine an item if it's in your inventory or if it is in the room
    items = lvls[current_room]["items_in_room"]
    for item in items:
        if item["name"].lower() == item_name.lower():
            print(f'You examined: {item["name"]} - {item["type"]}, {item["description"]}')
            return
    else:
        print("There are nothing to examine")
    #pass

#def go_nlvl():

# --- Game Loop ---

def inv():
    print("Welcome to the Inventory Game!")
    print("Type 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            # You can also rename the commands according to your own needs
            print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], quit")
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            item_name = command[7:]
            pick_up(item_name)
        elif command.startswith("drop "):
            item_name = command[5:]
            drop(item_name)
        elif command.startswith("use "):
            item_name = command[4:]
            use(item_name)
        elif command.startswith("examine "):
            item_name = command[8:]
            examine(item_name)
        #elif command.startswith("go to "):
            #go_nlvl(lvls[current_room])
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    inv()

