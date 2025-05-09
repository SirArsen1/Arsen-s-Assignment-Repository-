import time,sys

def typew(dialogue):
    for char in dialogue:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
        if char !=(" ","\n"):
            time.sleep(0.05)
        else:
            time.sleep(0.01)

typew("Prof. Gesundheit: Hello, my name is Professor Gesundheit, glad to meet you.\n")

while True:
    typew('Prof. Gesundheit: Would you mind telling me how old are you?\n')
    PlayerAge = input('> ')
    try:
        age = int(PlayerAge)
        if PlayerAge >= '15':
            typew('Prof. Gesundheit: Welcome aboard to our exciting experiment!\n')
            break
        else:
            typew("Prof. Gesundheit: Seems like you're a little too young to participate, Small One. Next one, please.\n")
    except ValueError:
        typew("Prof. Gesundheit: That doesn't look like a valid number. Try again, please.\n")

typew("Prof. Gesundheit: Now, what is your name?\n")
PlayerName = input('> ')
typew("Prof. Gesundheit: What a great name! I have a good friend with the same name!\n")

typew("Prof. Gesundheit: Anyway, our law department advised me to make sure our participants want \n to be a part of the experiment we are conducting today.\n This is the last moment you can leave, after this point you have to go all the way...\n FOR THE SCIENCE!\n")
while True:
    typew("Anyway, are you sure you want to continue? Yes or No?\n")
    PlayerChoice = input('> ')
    if PlayerChoice == 'Yes':
        typew("Prof. Gesundheit: I knew you had that spark in you\n")
        break
    elif PlayerChoice == 'No':
        typew("Prof. Gesundheit: Well, that's alright too, farewell!.\n")
        break
    else:
        typew("Prof. Gesundheit: Come again?\n")

typew('Now we can finally start. We came up with a technology that would allow us to travel to other dimensions!\n We made five portals and YOU will be going through them, of course with safety measures in place.\n You will spend around a minute of our time in foreign dimensions, after that we will pull you out of there.\n')

Portal1 = "You see grand lizard like creatures, fighting within a jungle. The sky is blood red and the place overall looks hostile.\n"
Portal2 = "White walls tower over the blue sea, behind those walls is a bustling city.\n"
Portal3 = "Darkness and nothingness surfaces this world, yet you feel like you're being watched by a far greater entity.\n Right before you leave it reveals itself, such indescribable abomination,\n that your mind copes by erasing it from your memory altogether\n"
Portal4 = "You witness attack ships on fire off the shoulder of Orion \nand C-beams glitter in the dark near the Tannhäuser Gate\n"
Portal5 = "A distant, loud and terrifying cry shocks you. The world was mostly a sea. Suddenly you see giant serpent \nemerging in a far distance, yet the size of this gargantuan creature scared you.\n"
Portal = [Portal1, Portal2, Portal3, Portal4, Portal5]

visited = []
while len(visited) < len(Portal):
    typew('\nProf. Gesundheit: Choose a portal you haven’t been to yet (1 to 5):\n')
    for i in range(1, 6):
        if i not in visited:
            print(f"Portal {i}\n")

    choice = input('> ')
    if choice.isdigit():
        index = int(choice)
        if 1 <= index <= 5:
            if index in visited:
                typew("Prof. Gesundheit: You've already visited that portal! Pick a different one.\n")
            else:
                visited.append(index)
                typew(f"\nYou step through Portal {index}...\n")
                typew(Portal[index - 1] + "\n")
        else:
            typew("Prof. Gesundheit: That portal doesn't exist! Pick between 1 and 5.\n")
    else:
        typew("Prof. Gesundheit: Numbers only, please!\n")

typew("\nProf. Gesundheit: Amazing work! You've visited all the dimensions. Thank you for your service to science!\n")

# The help of AI was used in a process to clear up questions I had during the coding.
# links used:
# https://stackoverflow.com/questions/41950021/typeerror-not-supported-between-instances-of-str-and-int
# https://stackoverflow.com/questions/33049167/attributeerror-int-object-has-no-attribute-isdigit
# https://stackoverflow.com/questions/43189302/why-does-the-ipython-repl-tell-me-syntaxerror-unexpected-eof-while-parsing-as
