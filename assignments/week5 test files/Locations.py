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

cellbtlfld1 = f'''
. ,:,   , .  .  . / /Ж   , .  .  . ,:,   , .  .
.,  . ± -; .,   /  /o Ж   ±   ,'  ''  .. '   ±           
 .    .,  , ±   |  |0   Ж     .,         \. |  /
.   .,   -_  .,  \  \-["=-+ .   ,,     -- ( O ) --
.,  ±   ,.' '-" , |  |0] Ж   ., ±   ''   /  |  \.  ±
. ,:,   , .  .  . / /Ж  W, .{p_icon} .  . ,:,   , .  . ±
.,  . ± -; .,   /  /o Ж   ;  -  " ±'   ;     _    .   
'''
cellbtlfld2 = f'''
. ,:,   , .  .  . / /Ж   , .  .  . ,:,   , .  .
.,  . ± -; .,   /  /o Ж   ±   ,'  ''  .. '   ±           
 .    .,  , ±   |  |0   Ж     .,         \. |  /
.   .,   -_  .,  \  \-["=-+ SW {p_icon} ,     -- ( O ) --
.,  ±   ,.' '-" , |  |0] Ж   ., ±   ''   /  |  \.  ±
. ,:,   , .  .  . / /Ж   , .  .  . ,:,   , .  . ±
.,  . ± -; .,   /  /o Ж   ;  -  " ±'   ;     _    .   
'''
cellbtlfld3 = f'''
. ,:,   , .  .  . / /Ж   , .  .  . ,:,   , .  .
.,  . ± -; .,   /  /o Ж W ±  {p_icon},'  ''  .. '   ±           
 .    .,  , ±   |  |0   Ж     .,         \. |  /
.   .,   -_  .,  \  \-["=-+ .   ,,     -- ( O ) --
.,  ±   ,.' '-" , |  |0] Ж   ., ±   ''   /  |  \.  ±
. ,:,   , .  .  . / /Ж   , .  .  . ,:,   , .  . ±
.,  . ± -; .,   /  /o Ж   ;  -  " ±'   ;     _    .   
'''
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
        | S |'''

cell3CS = f'''
   __________
  /  ,____,  \.
 /  .|    |.   \.______
|   |      |     E
|   :.    .:    _______
 \.  |____|   ./
  \._________/ 
'''

cell4 = f'''
. ,::,   , .  .|| ,E ,||,::,  .:';. ,
.   . ,::,  .,||   . ,|| .|| , ±,||
.  ,::,   .   .||, {p_icon}  .:;.||
§[==--'  ,   .||, ||,::, || .|| ,  ,||
.   .   ,,,  ,::,  .:';. ,||,::, ||
'''

cell51out3 = f'''

.,_..,_..,_..,_..,_.,
    | |  | |  | |
    | |  | |  | |
____| |__|N|__| |____
,||. NW.  {p_icon}   .,NE  ,::, 
    ,::, ,  ,::,   ,||.
'''
cell52out3 = f'''

.,_..,_..,_..,_..,_.,
    | |  |N|  | |
    | |  |{p_icon}|  | |
____| |__|S|__| |____
,||.  ,.     .,     ,::, 
    ,::, ,  ,::,   ,||.
'''
cell53out3 = f'''
NW        {p_icon}
.,_..,_..,_..,_..,_.,
    | |  | |  | |
    | |  | |  | |
____| |__| |__| |____
,||.  ,.     .,     ,::, 
    ,::, ,  ,::,   ,||.
'''
cell5dot1 = f'''

.,_..,_..,_..,_..,_.,
    | |  | |  | |
    ;{p_icon};  | |  | |
____|S|__| |__| |____
,||.  ,.     .,     ,::, 
    ,::, ,  ,::,   ,||.
'''
cell5dot2 = f'''

.,_..,_..,_..,_..,_.,
    | |  | |  | |
    | |  | |  ;{p_icon};
____| |__| |__|S|____
,||.  ,.     .,     ,::, 
    ,::, ,  ,::,   ,||.
'''
cell6 = f'''
,.     .,     ,::,   N    ,.     .,     ,::,
  ,::,      ,.     .,      ,::,      ,.     .,
,.     .,     ,::,      ,.     .,     ,::,
  ,::,      ,.     .,      ,::,      ,.     .,
,.     .,     ,::,  {p_icon}    ,.     .,     ,::,
  ,::,      ,.     .,      ,::,      ,.     .,
'''
cell7 = f'''
                 /
            ____/
       ____/;._/
    __/'";.._/
  _/.,.,.__/   _/|
 /oOoOo/     _/
/.,E,./ /   /
|.,{p_icon},.|/
|.,.,.|  _/
|.,.,.| /
'''
cell8 = f'''        
                          /'.
                         /  .\,
                      .=' ,'   \.
                     /  ;    =.  \,.
    /\.           .,'     ,.'    '  \   ./|     
   /  |   ,/\.   /   "     _.  '     \./   '.
 /  ., \./  . \,'    '   ____   ;    /   .'  \.
/ . ,  . \,     '. ,,,,/' NE '\,,,,.'  "    ;  \.'\.
_________------"""" §§ § ' §' '§§   """"-----_________   
 ±                                     ±         ±
      {p_icon}      ±               ±                       ±
'''
cell9 = f'''
|]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]|
|     ,.------.,               ,.------.,               ,.------.,               ,.------.,     |
|    ;          ;     [0]     ;          ;     [0]     ;          ;     [0]     ;          ;    |
|  .'            '.         .'            '.         .'            '.         .'            '.  |
| |       {p_icon}        |       |                |       |                |       |         NE     | |
'''

cells = [cell1, cellbtlfld1, cell2, cellbtlfld2, cell3,cell4, cell51out3, cell52out3, cell5dot1, cell5dot2, cell6, cell7, cell8, cell9]

# --- Levels ---
lvls = { # Dictionaries are case sensetive, DO NOT USE CAPITAL LETTERS
    "khurik post": { #cell1 # -- Ch1 --
        "description": f"---\nKhurik post, an important stronghold of alliance army. North path goes through a dark tunnel, \nbetter find a light source to go in.\nEast is where battlefield is.\n",
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
        "cell": cellbtlfld1,
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
            {"direction": "north-east", "name": "central battlefield", "locked": False, "damage": True},
            {"direction": "south", "name": "khurik post", "locked": False, "damage": False},
        ]
    },
    "central battlefield": { #cell2.1
        "description": "---\nIt's a dangerous area, easy to catch a stray bullet.\n---",
        "items_in_room": [],
        "cell": cellbtlfld2,
        "damage": True,
        "exits": [
            {"direction": "south-west", "name": "north trenches", "locked": False, "damage": True}
        ]
    },
    "road to blauvald": { #cell3
        "description": "Trenched checkpoint, that includes underground horse stables. \nYou can take a horse if you find a stable, look for it.",
        "items_in_room": [
            {"name": "Map", "type": "tool", "art": f"{ascii.get('map')}", "description": f"\nMap of north-west Vateria. On the bottom left you see Khurik river, \non the top right mountains of Äscalia and small parts of Bergardia, and Amania.\n"},
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
            {"name": "horse saddle", "type": "tool", "art": f" ", "description": "Allows to ride a horse."},
        ],
        "cell": cell3CS,
        "damage": True,
        "exits": [
            {"direction": "east", "name": "road to blauvald", "locked": False, "damage": False},
        ]
    },
    "battlefield": { #cell3.2
        "description": "---\nIt's a dangerous area, easy to catch a stray bullet.\n---",
        "items_in_room": [],
        "cell": cellbtlfld3,
        "damage": True,
        "exits": [
            {"direction": "west", "name": "road to blauvald", "locked": False, "damage": False}
        ]
    },
    "forests of blauvald": { #cell4 # -- ch2 --
        "description": " ",
        "items_in_room": [
            {"name": "sniper rifle", "type": "tool", "art": f"{ascii.get('snipe')}", "description": "Rifle that can shoot long distance targets. \nHas one bullet and was taken from the dead soldier."},
            {"name": "medkit", "type": "food", "art": f" ", "description": "Restores health point."},
        ],
        "cell": cell4,
        "damage": True,
        "exits": [
            {"direction": "east", "name": "south river shore", "locked": True, "damage": False},
        ]
    },
    "south river shore": { #cell5 1/3
        "description": "---\n A river with a strong stream. You see three ways to cross it, none looks reliable, so you have to guess the right one.\n---",
        "items_in_room": [],
        "cell": cell51out3,
        "damage": True,
        "exits": [
            {"direction": "north-west", "name": "wooden bridge 1", "locked": False, "damage": True},
            {"direction": "north", "name": "wooden bridge 2", "locked": False, "damage": False},
            {"direction": "north-east", "name": "wooden bridge 3", "locked": False, "damage": True},
        ]
    },
    "wooden bridge 2": { #cell5 2/3
        "description": "---\nYou picked the right path and you can safely cross the river.\n---",
        "items_in_room": [],
        "cell": cell52out3,
        "damage": False,
        "exits": [
            {"direction": "north", "name": "north river shore", "locked": False, "damage": False},
            {"direction": "south", "name": "south river shore", "locked": False, "damage": False},
        ]
    },
    "north river shore": {  # cell5 3/3
        "description": "---\n North shore looks completely different, rocky and much higher than the south shore. \nIt would've been very hard to climb here from a river with such strong stream. \n---",
        "items_in_room": [],
        "cell": cell53out3,
        "damage": False,
        "exits": [
            {"direction": "north-west", "name": "valley", "locked": False, "damage": False},
        ]
    },
    "wooden bridge 1": { #cell5.1
        "description": "---\nThe path you picked broke under your weight and you fell into a river, \nfortunately you can swim back to south shore and try again. \n---",
        "items_in_room": [],
        "cell": cell5dot1,
        "damage": True,
        "exits": [
            {"direction": "south", "name": "south river shore", "locked": False, "damage": False},
        ]
    },
    "wooden bridge 3": {  # cell5.2
        "description": "---\nThe path you picked broke under your weight and you fell into a river, \nfortunately you can swim back to south shore and try again. \n---",
        "items_in_room": [],
        "cell": cell5dot2,
        "damage": True,
        "exits": [
            {"direction": "south", "name": "south river shore", "locked": False, "damage": False},
        ]
    },
    "valley": { #cell6
        "description": "---\nAfter advancing through the forests, you find yourself in a valley, after which you will have to cross Äscalian mountains.\n---",
        "items_in_room": [],
        "cell": cell6,
        "damage": False,
        "exits": [
            {"direction": "north", "name": "mountain road", "locked": False, "damage": False},
        ]
    },
    "mountain road": { #cell7
        "description": " ",
        "items_in_room": [
            {"name": "lever", "type": "tool", "art": f" ", "description": "Can help move a boulder."},
            {"name": "grapes", "type": "food", "art": f" ", "description": "Restores health point."},
        ],
        "cell": cell7,
        "damage": False,
        "exits": [
            {"direction": "east", "name": "three peaks road", "locked": True, "damage": False},
        ]
    },
    "three peaks road": {  # cell8
        "description": "---\nAfter overcoming the previous challenge you witness a group of enemy saboteurs,\nsurrouned by many dead bodies. Fortunately they didn't notice you.\nMeybe there are something that can help you get rid of them.\n---",
        "items_in_room": [
            {"name": "grenade", "type": "tool", "art": f" ", "description": "Can take out a group of enemies."},
        ],
        "cell": cell8,
        "damage": False,
        "exits": [
            {"direction": "north-east", "name": "tunnel to bergardia", "locked": False, "damage": False},
        ]
    },
    "tunnel to bergardia": {  # cell9
        "description": " ",
        "items_in_room": [],
        "cell": cell9,
        "damage": False,
        "exits": [
            {"direction": "north-east", "name": "bergardia", "locked": False, "damage": False},
        ]
    },
    "bergardia": {  # cell10 #end
        "description": " ",
        "items_in_room": [],
        "cell": " ",
        "damage": False,
        "exits": []
    },
}

# --- Item_Key ---
item_key = {
  # cell name ↓    item ↓          ↓ locked cell direction
    ("khurik post", "lantern"): "north", #ch1
    ("north trenches", "shovel"): "north",
    ("road to blauvald", "horse saddle"): "north",
    ("forests of blauvald", "sniper rifle"): "east", #ch2
    ("mountain road", "lever"): "east", #ch3
    ("three peaks road", "grenade"): "north-east",
}

