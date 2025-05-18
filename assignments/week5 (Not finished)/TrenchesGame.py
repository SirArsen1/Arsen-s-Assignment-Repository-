# --- Imports ---
from ASCII_arts_col import ascii
from type_writing_script import typew #Typewriting machine effect

# ---- Game Mechanics ----
# --- Support functions---
# -- Health --
hp = ['❤','❤','❤']
h_point = '❤'
max_hp = 5

# -- Inventory --
inventory = []
MAX_INVENTORY_SIZE = 5

# -- Current cell --
current_cell = "khurik post"
# -- Cells visited --
cells_seen = []
# -- Function to print exits in a current room, used inside "look" function --
def show_exits():
    exits = lvls[current_cell]["exits"]
    for exit in exits:
        print(f"You can go to {exit['direction']} which leads to {exit['name']}")

def show_cell():
    print(lvls[current_cell]["cell"])

# -- Damage --
def damage_event():
    for h_point in hp:
        if len(hp) > 0:
            hp.remove(h_point)
            print(f'You lost one {h_point}!')
            return
        else:
            if len(hp) == 0:
                print('You died, restarting the game.')
                return

# -- Cheats --
def damage_me():
    for h_point in hp:
        if len(hp) > 0:
            hp.remove(h_point)
            print(f'You lost one {h_point}!')
            return
    else:
        if len(hp) == 0:
            print('You died, restarting the game.')
            return

# -- Prints chapters and story expositions when certain locations are reached --
def chapter_progression():
    global current_cell

    ch1 = f"\n{ascii.get('ch1')}\n---\nYou start your challenging mission in the Khurik post, a significant part of alliance army defence.\n---\n"
    ch2 = f"\n{ascii.get('ch2')}\n---\nFoests of Blauvald are populated by green immovable giants. These trees have a distinct color, \nsomething between blue and green."
    ch3 = f"hi"

    triggers = {
        "khurik post":f"{ch1}",
        "forests of blauvald":f"{ch2}",
        "mountain road":f"{ch3}",
    }

    chapter_trigger = triggers.get(current_cell)
    if current_cell not in cells_seen and current_cell in triggers:
        print (triggers[current_cell])

# --- Main Functions ---
# --- Actions ---
def show_health():
    global hp
    for h_point in hp:
        print(' '.join(hp))
        return
    else:
        if len(hp) == 0:
            print('You have no health left, you are dead!')

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
    items = lvls[current_cell]["items_in_room"]
    if len(items) > 0:
        print("You notice items:")
        for items in items:
            print(f'{items["name"]}') #{items["description"]}
        print("---") #break between items and exits
        show_exits()
        show_cell()
    else:
        print("There are nothing of use in there.")
        print("---") #break between items and exits
        show_exits()
        show_cell()
    #pass

def pick_up(item_name):
    # pick up an item from the room if inventory limit is not met yet
    items = lvls[current_cell]["items_in_room"]
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
    items = lvls[current_cell]["items_in_room"]
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
    items_in_room = lvls[current_cell]["items_in_room"]
    items = items_in_room + inventory
    for item in items:  # Had to rewrite this chain a bit, because I tried to add another item type behavior but first time I did it rather bad, by running into for else limitation
        if item['name'].lower() == item_name.lower():
            if item["type"] == "tool":
                if item in inventory:
                    if (current_cell, item_name) in item_key:  # compares if current room and item name, which we used are the same as in item_unlocks
                        unlock_direction = item_key[(current_cell, item_name)]  # making a variable from a code above(?)
                        for exit in lvls[current_cell]["exits"]:  # loop that looks for matching data to unlock the direction
                            if exit["direction"] == unlock_direction:
                                exit["locked"] = False  # if it matches it unlocks direction by turning "locked": True to False
                                inventory.remove(item) # removes key from inventory after use, to prevent infinite use of key and reduce inventory clutter
                                print(f"You used {item_name} to unlock the path to {unlock_direction}")
                                print(f"{item_name} has been removed from your inventory")
                                return
                            else:
                                print("You can't go there")
                                return #important, because it stops loop when we get the result we need, relates to all returns in this function
                    else:
                        print(f"Nothing happened after you used {item_name}")
                        return
                else:
                    print(f"You need to pick up {item_name} to use it")
                    return
            elif item["type"] == "food":
                if item in inventory:
                    if len(hp) < max_hp:
                        hp.append(h_point)
                        inventory.remove(item)
                        print(f'You gained one {h_point}!')
                        print(f"{item_name} has been removed from your inventory")
                        return
                    elif len(hp) == max_hp:
                        print('You reached max health.')
                        return
                else:
                    print(f"You need to pick up {item_name} to use it")
                    return
            elif item["type"] != ["tool", "food"]:
                print(f"Nothing happened after you used {item_name}")
                return
    else:
        print(f"There is no item in your inventory, called {item_name}")
        return

def examine(item_name):
    # you can only examine an item if it's in your inventory or if it is in the room
    items_in_room = lvls[current_cell]["items_in_room"]
    items = items_in_room + inventory
    for item in items:
        if item["name"].lower() == item_name.lower():
            print(f'You examined: {item["name"]} - {item["type"]}, {item["description"]} \n{item["art"]}')
            return
    else:
        print("There are nothing to examine")

def move_to_cell(direction): # this function was written with use of chatgpt, although I made an effort to understand it before implementing it, as seen by my comments. this decision was followed by my countless attempts at writing this function myself
    global current_cell # allows to change global variable and change the room, otherwise it would work only locally and wouldn't actually change the room
    exits = lvls[current_cell]["exits"] # allows to grab exits dictionaries from bigger level dictionary
    for exit in exits:
        if exit["direction"] == direction:
            if exit.get("locked", False):
                print(f"The {exit['name']} path to the {exit['direction']} is locked.")
                return
            else:
                current_cell = exit["name"]
                print(f"You move {direction} to the {current_cell}.")
                print(lvls[current_cell]["description"])
                if exit.get("damage", False):
                    damage_event()
                    return
                chapter_progression()
                return
    else:
        print("You can't go that way.")
        return

# --- Game Loop ---
def inv():
    chapter_progression()
    print("\nType 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            # You can also rename the commands according to your own needs
            print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], go [direction] (i.e. go south), health, quit")

        elif command == "health":
            show_health()

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
            move_to_cell(direction) # calls the function defined above.

        elif command == "quit":
            print("Thanks for playing!")
            break

        # --- Cheats ---
        elif command == "cheats":
            print("dmgme: to inflict damage on yourself")

        elif command == "dmgme":
            damage_me()
        # ------
        else:
            print("Unknown command. Type 'help' to see available commands.")

# ---- Game ----
# --- Title & intro ---
print (ascii.get('title')) #game titleJ

# -- Story backstory --
typew ("---\nIt's been more than a year since Demonic Plague emerged in west Vateria. Demon Warlords \nmarched their armies through Null Point, what most call Hell's Gates. Under the patronage of \nLucius of Underworld, they rapidly advanced into Talayir, shocking nearby nations. \nHaphazardly they formed an alliance, once opponents became allies against the biggest \nthreat Talayir has ever seen.\n---")

# -- Character creation --
# - Player name phase -
print ("\nWhat is your name?")
name = input('> ')
pname = "Private " + name
# - Player icon phase - #also levels and levels info, with maps. My perfectionism is killing me
from Locations import lvls, item_key, cells #Had to move it here because couldn't come up with a better way of implementing this

# -- Story setup --
typew(f"---\nYou're a scout soldier from Kingdom of Alverland. Your task is to deliver a valuable intel to \nunited command. Reading the intel is prohibited. The route will start from east front, near the \nriver Khurik, after which you have to move north, through forests of Blauvald and mountains \nof Äscalia, until you reach north front command center in Amania. May the God \nhelp you in this mission, {pname}.\n---")

inv()