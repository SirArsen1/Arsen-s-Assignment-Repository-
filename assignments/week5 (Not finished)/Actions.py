from Locations import lvls, item_unlocks

# --- Inventory ---
inventory = []
MAX_INVENTORY_SIZE = 5

# --- Support functions---
    # Current room
current_room = "halls"

    # function to print exits in a current room, used inside "look" function
def show_exits():
    exits = lvls[current_room]["exits"]
    for exit in exits:
        print(f"You can go to {exit['direction']} which leads to {exit['name']}")

# --- Actions ---
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

def drop(item_name):
    # drop an item from your inventory, at the same time append it back to the list of items for the room
    items = lvls[current_room]["items_in_room"]
    for item in inventory:
        if item["name"].lower() == item_name:
            ["items_in_room"].append(item)
            inventory.remove(item)
            items.append(item)
            print(f"You dropped {item['name']}")
            return
    else:
        print("You have nothing to drop")

def use(item_name): # Use function
    if (current_room, item_name) in item_unlocks: # compares if current room and item name, which we used are the same as in item_unlocks
        unlock_direction = item_unlocks[(current_room, item_name)] # making a variable from a code above(?)
        for exit in lvls[current_room]["exits"]: # loop that looks for matching data to unlock the direction
            if exit["direction"] == unlock_direction:
                exit["locked"] = False # if it matches it unlocks direction by turning "locked": True to False
                print(f"You used {item_name} to unlock the path to {unlock_direction}")
        #print("That direction doesn't exist")
    else:
        print(f"Nothing happened after you used {item_name}")
    #pass

def examine(item_name):
    # you can only examine an item if it's in your inventory or if it is in the room
    items_in_room = lvls[current_room]["items_in_room"]
    items = items_in_room + inventory
    for item in items:
        if item["name"].lower() == item_name.lower():
            print(f'You examined: {item["name"]} - {item["type"]}, {item["description"]}')
            return
    else:
        print("There are nothing to examine")

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

# --- Game Loop ---
def inv():
    print("Welcome to the Inventory Game!")
    print("Type 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            # You can also rename the commands according to your own needs
            print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], go [direction: i.e. north], quit")

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