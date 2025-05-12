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
    "garden": { # supposedly locked room that must be open with key2 item
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

# health
hp = ['❤','❤','❤']
h_point = '❤'
max_hp = 5

# Current room
current_room = "halls"
# item effects
item_unlocks = {
    ("halls", "key"): "east"
}
# function to print exits in a current room, used inside "look" function
def show_exits():
    exits = lvls[current_room]["exits"]
    for exit in exits:
        print(f"You can go to {exit['direction']} which leads to {exit['name']}")

# Use function
def use(item_name):
    # Ex: use the item differently depends on the type
    # So this function should work with a dictionary that lists item's effects, while also working with move function
    # Why am I complicating my homework everytime dude...
    #items_in_room = lvls[current_room]["items_in_room"]
    #items = items_in_room + inventory
    items = lvls[current_room]["items_in_room"]
    for item in items:
        if item['name'].lower() == item_name.lower():
            if item['type'] == 'tool':
                if (current_room, item_name) in item_unlocks: # compares if current room and item name, which we used are the same as in item_unlocks
                    unlock_direction = item_unlocks[(current_room, item_name)] # making a variable from a code above(?)
                    for exit in lvls[current_room]["exits"]: # loop that looks for matching data to unlock the direction
                        if exit["direction"] == unlock_direction:
                            exit["locked"] = False # if it matches it unlocks direction by turning "locked": True to False
                            print(f"You used {item_name} to unlock the path to {unlock_direction}")
                    #print("That direction doesn't exist")
                else:
                    print(f"Nothing happened after you used {item_name}")
    else:
        for item in items:
            if item['name'].lower() == item_name.lower():
                if item['type'] == 'food':
                    if item["name"].lower() == item_name:
                        hp.append(h_point)
                        items.remove(item)
                        print(f'You gained one {h_point}!')
                    elif len(hp) == max_hp:
                        print('You reached max health.')
                else:
                    print(f"Nothing happened after you used {item_name}")
    #print("You can't use this item.")
    #pass

def show_room_items():
    # list all items in current room
    items = lvls[current_room]["items_in_room"]
    if len(items) > 0:
        print("You notice items:")
        for items in items:
            print(f'{items["name"]} - {items["description"]}')
        print("---") #break between items and exits
        show_exits()
    else:
        print("There are nothing of use in there.")
    #pass

def move_to_room(direction): # this function was written with use of chatgpt, although I made an effort to understand it before implementing it, as seen by my comments. this decision was followed by my countless attempts at writing this function myself
    global current_room # allows to change global variable and change the room, otherwise it would work only locally and wouldn't actually change the room
    exits = lvls[current_room]["exits"] # allows to grab exits dictionaries from bigger level dictionary

    for exit in exits:
        if exit["direction"] == direction:
            if exit.get("locked", False):
                print(f"The {exit['direction']} path is locked.")
                return
            current_room = exit["name"]
            print(f"You move {direction} to the {current_room}.")
            print(lvls[current_room]["description"])
            return
    else:
        print("You can't go that way.")

def inv():
    print("Welcome to the Inventory Game!")
    print("Type 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            # You can also rename the commands according to your own needs
            print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], go [direction: i.e. north], quit")
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