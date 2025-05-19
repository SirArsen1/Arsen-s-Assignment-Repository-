# --- Imports ---
from Actions import inv, player_icon
from ASCII_arts_col import ascii #ASCII art and maps dictionary
from type_writing_script import typew #Typewriting machine effect
from Locations import lvls, item_key

# --- Title & intro ---
print (ascii.get('title')) #game title

# -- Story backstory --
typew ("---\nIt's been more than a year since Demonic Plague emerged in west Vateria. Demon Warlords \nmarched their armies through Null Point, what most call Hell's Gates. Under the patronage of \nLucius of Underworld, they rapidly advanced into Talayir, shocking nearby nations. \nHaphazardly they formed an alliance, once opponents became allies against the biggest \nthreat Talayir has ever seen.\n---")

# -- Character creation --
# - Player name phase -
print ("\nWhat is your name?")
name = input('> ')
pname = "Private " + name
# - Player icon phase -
player_icon()

# -- Story setup --
typew(f"---\nYou're a scout soldier from Kingdom of Alverland. Your task is to deliver a valuable intel to \nunited command. Reading the intel is prohibited. The route will start from east front, near the \nriver Khurik, after which you have to move north, through trenches of Blauvald, mountains \nand forests of Äscalia, until you reach north front command center in Amania. May the God \nhelp you in this mission, {pname}.\n---")
# --- Chapter 1 ---
print (ascii.get('ch1')) #ch1 ascii
typew(f"---\nKhurik post, this is where you were given your order. North path goes through a dark tunnel, \nit is dangerous to go blind. North-east path leads to ammo warehouse, blocked by rubble and rocks, better not touch it.\nEast is where open battlefield is,chances of dying are very high.\n---")

inv()
