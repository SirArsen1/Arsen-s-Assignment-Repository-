lvls = {
    "halls": {
        "description": "ddd",
        "items_in_room": [
            {"name": "Torch", "type": "tool", "description": "Lights up dark places."},
            {"name": "Apple", "type": "food", "description": "Restores a small amount of health."},
            {"name": "key", "type": "tool", "description": "Opens a locked door."},
        ],
        "exits": {
            {
                "direction": "east",
                "name": "kitchen",
                "locked": True
            }
        }
    },
    "kitchen": {
        "description": "ffff",
        "items_in_room": [
            {"name": "Torch2", "type": "tool", "description": "Lights up dark places."},
            {"name": "Apple2", "type": "food", "description": "Restores a small amount of health."},
            {"name": "key2", "type": "tool", "description": "Opens a locked door."},
        ],
        "exits": {
                    {
                        "direction": "west",
                        "name": "halls",
                        "locked": False
                    },
                    {
                        "direction": "north",
                        "name": "garden",
                        "locked": False
                    }
        }
    },
    "garden": { # supposedly locked room that must be open with key2 item
            "description": "gggg",
            "items_in_room": [
                {"name": "Torch3", "type": "tool", "description": "Lights up dark places."},
                {"name": "Apple3", "type": "food", "description": "Restores a small amount of health."},
                {"name": "key3", "type": "tool", "description": "Opens a locked door."},
            ],
            "exits": {
                    "direction": "south",
                    "name": "kitchen",
                    "locked": False
                }
            }
}

# Current room
current_room = "halls"

# exits
exits = lvls[current_room]['exits']

# item effects
item_unlocks = {
    ("halls", "key"): "east"
}
# direction
direction = lvls[current_room]["direction"]

def use(item_name):
    # Ex: use the item differently depends on the type
    # So this function should work with a dictionary that lists item's effects, while also working with move function
    # Why am I complicating my homework everytime dude...
    if (current_room, item_name) in item_unlocks:
        direction = item_unlocks[(current_room, item_name)]
        lvls[current_room]["exits"][direction]["locked"] = False
    #pass

def show_room_items():
    # list all items in current room
    items = lvls[current_room]["items_in_room"]
    if len(items) > 0:
        for items in items:
            print(f'{items["name"]} - {items["description"]}')
            print(f"{exits['name']}")
    else:
        print("There are nothing of use in there.")
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

def inv():
    print("Welcome to the Inventory Game!")
    print("Type 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            # You can also rename the commands according to your own needs
            print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], quit")
        elif command == "look":
            show_room_items()
        elif command.startswith("use "):
            item_name = command[4:]
            use(item_name)
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