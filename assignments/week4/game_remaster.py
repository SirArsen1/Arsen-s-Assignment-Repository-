import time,sys

# Typewriting machine effect
from type_writing_script import typew

# Characters name variables
prof_g = ('Prof. Gesundheit: ')

typew(f"{prof_g}Hello, my name is Professor Gesundheit, glad to meet you.\n")

# Intro
while True:
    typew(f"{prof_g}Would you mind telling me how old are you?\n")
    PlayerAge = input('> ')
    try:
        age = int(PlayerAge)
        if PlayerAge >= '15':
            typew(f"{prof_g}Welcome aboard to our exciting experiment!\n")
            break
        else:
            typew(f"{prof_g}Seems like you're a little too young to participate, Small One. Next one, please.\n")
    except ValueError:
        typew(f"{prof_g}That doesn't look like a valid number. Try again, please.\n")

typew(f"{prof_g}Now, what is your name?\n")

# player name variable
pname = input('> ')

typew(f"{prof_g}What a great name! I have a good friend with the same name!\n")

# Second ending sections
typew(f"{prof_g}Anyway, our law department advised me to make sure our participants want \n to be a part of the experiment we are conducting today.\n This is the last moment you can leave, after this point you have to go all the way...\n FOR THE SCIENCE!\n")
while True:
    typew(f"But I digress,{pname} are you sure you want to continue? Yes or No?\n")
    PlayerChoice = input('> ')
    if PlayerChoice == 'Yes':
        typew(f"{prof_g}I knew you had that spark in you\n")
        break
    elif PlayerChoice == 'No':
        typew(f"{prof_g}Well, that's alright too, farewell! {pname}.\n")
        break
    else:
        typew(f"{prof_g}Come again?\n")

# The main segment
typew(f"Now we can finally start, {pname}. We came up with a technology that would allow us to travel to other dimensions!\n We made five portals and YOU will be going through them, of course with safety measures in place.\n You will spend around a minute of our time in foreign dimensions, after that we will pull you out of there.\n")

# portal def function
def explore_portals(portal_descriptions):
    visited = []
    while len(visited) < len(portal_descriptions):
        typew(f"\n{prof_g}Choose a portal you haven’t been to yet (1 to 5):\n")
        for i in range(1, len(portal_descriptions) + 1):
            if i not in visited:
                print(f"Portal {i}")

        choice = input('> ')
        if choice.isdigit():
            index = int(choice)
            if 1 <= index <= len(portal_descriptions):
                if index in visited:
                    typew(f"{prof_g}You've already visited that portal! Pick a different one.\n")
                else:
                    visited.append(index)
                    print(f"\nYou step through Portal {index}...\n")
                    print(portal_descriptions[index - 1])
            else:
                typew(f"{prof_g}That portal doesn't exist! Pick between 1 and 5.\n")
        else:
            typew(f"{prof_g}Numbers only, please!\n")

# Portal list
portal1 = '''
██████▒                                                                         ░▓████████████████▓▒
███████░                                                                     ░▓█████████████▓░     ▓
███████▓░                                                                    ▓██████▓▒░░         ▓██
████▓▒▒▒░                                                          ▒▒░      ░▓▒░               ▓████
██████▓▒░                                                      ░▓▓▒███▒                      ▒██████
███▓████▓▓░                                              ░█████▓░▒█████▓                    ▒███████
█▓▓▓▓▓▒▓█▓▓▒░                                          ░▒██▓▓█▓▒▓██████▒                   ░▓▒▒█████
████▓▒░░░░░░                                          ▒▒▓▓▓▓██████████▒                       ▒█████
███████▓▒░                                          ░▒▒▓▒███████████▓                         ▒█████
▓██▓▓▓▓█▓▓▓▓▒░░                           ░░░▒▓▒░  ░▒████████████░                           ░▓█████
▓█▓▓▓▓▒▒▓▒▒▒░                            ▒▓▓██████▒▓▓█▓█▓▓██████████▒                        ▓██████
█▓▓▓▓▒░░░░░                           ░▒▓▓▓▓█▓███▓▓██▓███▓████████████▓░                    ░▓██████
▓▓▓▓▓▒░░                             ░░▒▒▒▓▓▓▓██████▓██████████████████░                    ▒▓██████
███▓▓▓▒░                            ░░▒▒▓▓▓▒▓▓████████████████▓▒░░▒▓▓▓▒           ░        ░▓▓▓█████
█████▓▒▒▒░                        ░▓█▒▒▒█▓▒▓████████████████▒░                   ░▓▒        ▒███████
█████▓▓▓█▓░                      ▒▓██▒▓▓█▓▓███████████████▓                      ░██░       ░███████
█████▓███▓▒                    ░▒▓████████████████████████▓                      ▒██▓     ░▒▒███████
█████████▓▓░                 ░▓▓▓██████████████████████████░                     ▓███▓█░  ▓█▓███████
██████████▓▒               ░▒▓▓▓███████▓███████████████▓███▓░  ▒▒░              ▒██████▓ ▒██████████
███████████▓░            ░▒▓▓▓▓▓████████████████████████░█████▓░░░              ▓███████▒▒██████████
████████████▒ ░▓█▓▓▒▒▒▒▓▓▓▓██████████████████████████████░ ░░▒▓█░          ▒   ░█████████▒██████████
████████████▒    ░▓██████████▓▓███████░▓████▒▓▒ ░████████▓   ░░ ▓    ▓▓▒  ░█▓░ ▓████████████████████
████████████▓▓░               ▒█████   ░█████▒░     ▒█████▓░▒▓▓▓▓▓▓▓▓▓███▓▓███▒▓████████████████████
████████████▓▒░▒░▓░░      ▒▒  ░████▓░   ██████░░▒░  ▒█████▓▓▓▓▓▓▓▓▓▓▓▓▓█████████████████████████████
███████████████████▓▓▓▓░▒▓▓▓▓▓▓███▓███▓███████████▓▓▓▓██████████████████████████▓▓▓█████████████████
█████████████████████▓▓▓▓▓▓▓▓███████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████
\nYou see grand lizard-like creatures fighting in a jungle with a blood-red sky.\n'''
portal2 = '''
                                                                                                    
                                                                                                    
                                                                                                    
                                               ░░                                                   
                                               ░░                                                   
                                               ▒▒                                                   
                                               ▓▒                                                   
                                               █▒                                                   
                                              ░█▓░                                                  
                                             ░▓██░                                                  
                                            ░░███░                                                  
                                           ░░▓████░░                                                
                                           ▓░██████▓░                                               
                                       ░ ░ █▓███████▒        ░░                                     
                                       ░░░░█████████▒░░      ░░░                                    
                                       ░█████████████▒▒ ░   ░▒▒░                                    
                                       ▒██████████████▓░▒   ░▓█▓      ░▓▓▓▒░                        
                                       ▒█████████████████   ░███░     ████▓░                        
                                       ▓█████████████████▒▒▒▒███░    ▒████▓░                        
        ░▒▒▒▒▒▒▒░                  ▒░░▓█████████████████████████▒   ░█████▓░            ░▒▒▒▒▒▒▒░   
        ▒██████▓░                 ░█▒▒▓█████████████████████████▒   ▒█████▓░            ░███████░   
░░░░░░░░▒██████▓░░░░░░░░░░░░░░░░░░▒█████████████████████████████▒░░░██████▓░░░░░░░░░░░░░░███████░░░░
████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████████████████████
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
\nWhite walls tower over the blue sea, hiding a bustling city behind.\n'''
portal3 = '''

Darkness surrounds you. You feel watched... then you see an unthinkable creature, and forget it instantly.'''
portal4 = '''

Attack ships on fire off the shoulder of Orion... C-beams glitter in the dark near the Tannhäuser Gate.'''
portal5 = '''

A sea world. A giant serpent rises in the distance, its size terrifies you.'''

portals = [portal1, portal2, portal3, portal4, portal5]
explore_portals(portals)

# Ending
typew(f"\n{prof_g}Amazing work, {pname}! You've visited all the dimensions. Thank you for your service to science!\n")

# The help of AI was used in a process to clear up questions I had during the coding process.
# links used:
# https://stackoverflow.com/questions/41950021/typeerror-not-supported-between-instances-of-str-and-int
# https://stackoverflow.com/questions/33049167/attributeerror-int-object-has-no-attribute-isdigit
# https://stackoverflow.com/questions/43189302/why-does-the-ipython-repl-tell-me-syntaxerror-unexpected-eof-while-parsing-as
# https://www.youtube.com/watch?v=o4XveLyI6YU
# https://www.youtube.com/watch?v=38uGbVYICwg
# https://www.youtube.com/watch?v=O8xlxE9sBmo
