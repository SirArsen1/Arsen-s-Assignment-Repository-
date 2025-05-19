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
            {"name": "Torch2", "type": "tool", "description": "Lights up dark places."},
            {"name": "Apple2", "type": "food", "description": "Restores a small amount of health."},
            {"name": "key2", "type": "tool", "description": "Opens a locked door."},
        ],
        "exits": {"west": "halls"}
    }
}

MAX_INVENTORY_SIZE = 5

# Current room
current_room = "halls"

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
    # So this function should work with a dictionary that lists item's effects, while also working with move function
    # Why am I complicating my homework everytime dude...

    pass

def examine(item_name):
    # you can only examine an item if it's in your inventory or if it is in the room
    room_items = lvls[current_room]["items_in_room"]
    items = room_items + inventory
    for item in items:
        if item["name"].lower() == item_name.lower():
            print(f'You examined: {item["name"]} - {item["type"]}, {item["description"]}')
            return
        elif item["name"].lower() != item_name.lower():
            print(f'You have to examine an item in a room or the ones you have')
            return
    else:
        print("There are nothing to examine")
    #pass

def move_to_room(direction): # this function was written with use of chatgpt, although I made an effort to understand it before implementing it, as seen by my comments. this decision was followed by my countless attempts at writing this function myself
    global current_room # allows to change global variable and change the room, otherwise it would work only locally and wouldn't actually change the room
    exits = lvls[current_room]["exits"] # allows to grab exits dictionaries from bigger level dictionary
    if direction in exits: # checks if player goes to exits
        new_room = exits[direction] # so new_room basically looks which exit we chose and makes it a new room
        current_room = new_room # since we got a new room we tell a function to put new room inside current room variable
        print(f"You move {direction} to the {current_room}.") # we put current room here because it comes after we changed it
        print(f"{lvls[current_room]['description']}")
    else:
        print("You can't go that way.")

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
        elif command.startswith("go "): #by ChatGPT too.
            direction = command[3:] # so the number slices off the trigger word we created to extract the data we need, and the data function understands
            move_to_room(direction) # calls the function defined above.
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    inv()

