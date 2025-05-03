def explore_portals(portal_descriptions):
    visited = []
    while len(visited) < len(portal_descriptions):
        typew(f"\n{prof_g}Choose a portal you haven’t been to yet (1 to 5):")
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

# Portal descriptions
portal1 = "You see grand lizard-like creatures fighting in a jungle with a blood-red sky."
portal2 = "White walls tower over the blue sea, hiding a bustling city behind."
portal3 = "Darkness surrounds you. You feel watched... then you see an unthinkable creature, and forget it instantly."
portal4 = "Attack ships on fire off the shoulder of Orion... C-beams glitter in the dark near the Tannhäuser Gate."
portal5 = "A sea world. A giant serpent rises in the distance, its size terrifies you."

# Put all portals in a list
portals = [portal1, portal2, portal3, portal4, portal5]

# Call the function
explore_portals(portals)