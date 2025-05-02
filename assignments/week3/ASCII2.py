import random

while True: # allows to restart the program later
# First equation
    Num1 = None
    while Num1 is None:
        try:
            Num1 = int(input("please, write a number: "))
        except ValueError:
            print ("We're doing math here! Write a number, please.\n")

    Num2 = None
    while Num2 is None:
        try:
            Num2 = int(input("please, write a second number: "))
        except ValueError:
            print ("We're doing math here! Write a number, please.\n")

    Num1, Num2 = int(Num1), int(Num2)

    Answer1 = Num1 * Num2
    Equation1 = f"{Num1} * {Num2} = {Answer1}"

    print(f'''                                                                                                                                                                                                                                                             
          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     
         ▒███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▒     
         ▒█▓                                                                                                                       ▒█▒     
         ▒█▓                                                                                                                       ▒█▒     
         ▒█▓                                                                                                                       ▒█▒     
         ▒█▓                    ░░░░                                                                                               ▒█▒     
         ▒█▓                ░████████▓                                                                                             ▒█▒     
         ▒█▓              ▓████████████▓                                                                                           ▒█▒     
         ▒█▓             ▓████████▓█▓███▓                           ░░░{Equation1:^60}▒█▒     
         ▒█▓             ██████▓░▒▓░ ▒███                        ░░░░░                                                             ▒█▒     
         ▒█▓            ░████░      ░░▒███                       ░ ▒░░                                                             ▒█▒     
         ▒█▓            ▓█▓░░▒░   ░▓▒░░███▓                     ░  ░▒                                                              ▒█▒     
         ▒█▓           ▒█▓░░    ░   ░░▒▒▓██                    ░   ░                                                               ▒█▒     
         ▒█▓           ▒██░░        ░░░▒██▓               ░ ░░   ░░                                                                ▒█▒     
         ▒█▓            ▓██▓░  ░░░░ ░░██▓░     ▒░   ░   ░░     ░░                                                                  ▒█▒     
         ▒█▓              ▒█▓  ▒▒░░░▒▒░░░            ░   ░  ░▒░                                                                    ▒█▒     
         ▒█▓               ▒░░░░ ░░▒░░░░             ░   ░░▒                                                                       ▒█▒     
         ▒█▓          ░░░░ ░  ░    ▒░  ░░ ░ ░       ░░ ░░░                                                                         ▒█▒     
         ▒█▓        ▒░     ░  ░░░   ▒░░░   ░░   ░░░░░░░                                                                            ▒█▒     
         ▒█▓       ▒   ░   ░ ░░  ░░░░ ░    ░░░░░░░░░                                                                               ▒█▒     
         ▒█▓       ░   ░     ░░░░░░░░      ░░░░                                                                                    ▒█▒     
         ▒█▓       ░    ░  ░               ░▒                                                                                      ▒█▒     
         ▒█▓      ▒      ░ ░                ░                                                                                      ▒█▒     
         ▒█▓     ░       ░░                ▒                                                                                       ▒█▒     
         ▒█▓    ░░       ░░            ░░░░                                                                                        ▒█▒     
         ▒█▓   ░░  ░░░░░░▒░       ░░░░░░░▒                                                                                         ▒█▒     
         ▒█▓   ░░  ░░    ░▒░░  ░░░░░░░░░░                                                                                          ▒█▒     
         ▒█▓    ░░░     ░░░░░░░░░░░░░░░░░                                                                                          ▒█▒     
         ▒█▓      ▒ ░ ░    ░▒░░░░▒▒▓▒▓▓░                                                                                           ▒█▒     
         ▒█▓       ░░ ░     ░▒▒▓▓▒▓▓▒▒░░░                                                                                          ▒█▒     
         ▒█▓         ░░░░     ░░░░  ░░░░░░          ░░░▒▒▒░░░░░░▒▒                                                                 ▒█▒     
         ▒███████████░    ░░░░   ░░░▒▒▒▓▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▓▒▓▓▓█▓█████████████████████████████████████████████████████████████████▒     
          ░█████████████▓██████████████████████████████████████████████▒                                                                   
    ''')

# Second equation
    Num3 = None
    while Num3 is None:
        try:
            Num3 = int(input("please, write one number this time: "))
        except ValueError:
            print("We're doing math here! Write a number, please.\n")

    rn = random.randint(1,10)
    Num4 = rn

    Num3, Num4 = int(Num3), int(Num4)

    Answer2 = Num3 * Num4
    Equation2 = f"{Num3} * {Num4} = {Answer2}"

    print(f'''                                                                                                                                                                                                                                                             
          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     
         ▒███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▒     
         ▒█▓                                                                                                                       ▒█▒     
         ▒█▓                                                                                                                       ▒█▒     
         ▒█▓                                                                                                                       ▒█▒     
         ▒█▓                    ░░░░                                                                                               ▒█▒     
         ▒█▓                ░████████▓                                                                                             ▒█▒     
         ▒█▓              ▓████████████▓                                                                                           ▒█▒     
         ▒█▓             ▓████████▓█▓███▓                           ░░░{Equation2:^60}▒█▒     
         ▒█▓             ██████▓░▒▓░ ▒███                        ░░░░░                                                             ▒█▒     
         ▒█▓            ░████░      ░░▒███                       ░ ▒░░                                                             ▒█▒     
         ▒█▓            ▓█▓░░▒░   ░▓▒░░███▓                     ░  ░▒                                                              ▒█▒     
         ▒█▓           ▒█▓░░    ░   ░░▒▒▓██                    ░   ░                                                               ▒█▒     
         ▒█▓           ▒██░░        ░░░▒██▓               ░ ░░   ░░                                                                ▒█▒     
         ▒█▓            ▓██▓░  ░░░░ ░░██▓░     ▒░   ░   ░░     ░░                                                                  ▒█▒     
         ▒█▓              ▒█▓  ▒▒░░░▒▒░░░            ░   ░  ░▒░                                                                    ▒█▒     
         ▒█▓               ▒░░░░ ░░▒░░░░             ░   ░░▒                                                                       ▒█▒     
         ▒█▓          ░░░░ ░  ░    ▒░  ░░ ░ ░       ░░ ░░░                                                                         ▒█▒     
         ▒█▓        ▒░     ░  ░░░   ▒░░░   ░░   ░░░░░░░                                                                            ▒█▒     
         ▒█▓       ▒   ░   ░ ░░  ░░░░ ░    ░░░░░░░░░                                                                               ▒█▒     
         ▒█▓       ░   ░     ░░░░░░░░      ░░░░                                                                                    ▒█▒     
         ▒█▓       ░    ░  ░               ░▒                                                                                      ▒█▒     
         ▒█▓      ▒      ░ ░                ░                                                                                      ▒█▒     
         ▒█▓     ░       ░░                ▒                                                                                       ▒█▒     
         ▒█▓    ░░       ░░            ░░░░                                                                                        ▒█▒     
         ▒█▓   ░░  ░░░░░░▒░       ░░░░░░░▒                                                                                         ▒█▒     
         ▒█▓   ░░  ░░    ░▒░░  ░░░░░░░░░░                                                                                          ▒█▒     
         ▒█▓    ░░░     ░░░░░░░░░░░░░░░░░                                                                                          ▒█▒     
         ▒█▓      ▒ ░ ░    ░▒░░░░▒▒▓▒▓▓░                                                                                           ▒█▒     
         ▒█▓       ░░ ░     ░▒▒▓▓▒▓▓▒▒░░░                                                                                          ▒█▒     
         ▒█▓         ░░░░     ░░░░  ░░░░░░          ░░░▒▒▒░░░░░░▒▒                                                                 ▒█▒     
         ▒███████████░    ░░░░   ░░░▒▒▒▓▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▓▒▓▓▓█▓█████████████████████████████████████████████████████████████████▒     
          ░█████████████▓██████████████████████████████████████████████▒                                                                   
    ''')

# Random list equation3

    fruits = ['Apples', 'Bananas', 'Oranges']
    ran_fruit = random.choice(fruits)
    print(ran_fruit)

    usernum = input("please write a number: ")

    rn = random.randint(2, 10)

    usernum, Num2 = int(usernum), int(rn)
    answer3 = usernum * rn

    Equation3 = f"{usernum} {ran_fruit}, * {rn} {ran_fruit} = {answer3} {ran_fruit}"

    print(f'''                                                                                                                                                                                                                                                             
          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     
         ▒███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▒     
         ▒█▓                                                                                                                       ▒█▒     
         ▒█▓                                                                                                                       ▒█▒     
         ▒█▓                                                                                                                       ▒█▒     
         ▒█▓                    ░░░░                                                                                               ▒█▒     
         ▒█▓                ░████████▓                                                                                             ▒█▒     
         ▒█▓              ▓████████████▓                                                                                           ▒█▒     
         ▒█▓             ▓████████▓█▓███▓                           ░░░{Equation3:^60}▒█▒     
         ▒█▓             ██████▓░▒▓░ ▒███                        ░░░░░                                                             ▒█▒     
         ▒█▓            ░████░      ░░▒███                       ░ ▒░░                                                             ▒█▒     
         ▒█▓            ▓█▓░░▒░   ░▓▒░░███▓                     ░  ░▒                                                              ▒█▒     
         ▒█▓           ▒█▓░░    ░   ░░▒▒▓██                    ░   ░                                                               ▒█▒     
         ▒█▓           ▒██░░        ░░░▒██▓               ░ ░░   ░░                                                                ▒█▒     
         ▒█▓            ▓██▓░  ░░░░ ░░██▓░     ▒░   ░   ░░     ░░                                                                  ▒█▒     
         ▒█▓              ▒█▓  ▒▒░░░▒▒░░░            ░   ░  ░▒░                                                                    ▒█▒     
         ▒█▓               ▒░░░░ ░░▒░░░░             ░   ░░▒                                                                       ▒█▒     
         ▒█▓          ░░░░ ░  ░    ▒░  ░░ ░ ░       ░░ ░░░                                                                         ▒█▒     
         ▒█▓        ▒░     ░  ░░░   ▒░░░   ░░   ░░░░░░░                                                                            ▒█▒     
         ▒█▓       ▒   ░   ░ ░░  ░░░░ ░    ░░░░░░░░░                                                                               ▒█▒     
         ▒█▓       ░   ░     ░░░░░░░░      ░░░░                                                                                    ▒█▒     
         ▒█▓       ░    ░  ░               ░▒                                                                                      ▒█▒     
         ▒█▓      ▒      ░ ░                ░                                                                                      ▒█▒     
         ▒█▓     ░       ░░                ▒                                                                                       ▒█▒     
         ▒█▓    ░░       ░░            ░░░░                                                                                        ▒█▒     
         ▒█▓   ░░  ░░░░░░▒░       ░░░░░░░▒                                                                                         ▒█▒     
         ▒█▓   ░░  ░░    ░▒░░  ░░░░░░░░░░                                                                                          ▒█▒     
         ▒█▓    ░░░     ░░░░░░░░░░░░░░░░░                                                                                          ▒█▒     
         ▒█▓      ▒ ░ ░    ░▒░░░░▒▒▓▒▓▓░                                                                                           ▒█▒     
         ▒█▓       ░░ ░     ░▒▒▓▓▒▓▓▒▒░░░                                                                                          ▒█▒     
         ▒█▓         ░░░░     ░░░░  ░░░░░░          ░░░▒▒▒░░░░░░▒▒                                                                 ▒█▒     
         ▒███████████░    ░░░░   ░░░▒▒▒▓▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▓▒▓▓▓█▓█████████████████████████████████████████████████████████████████▒     
          ░█████████████▓██████████████████████████████████████████████▒                                                                   
    ''')

# String input
    fav_fruit = input ("By the way, what is your favorite fruit?: ")
    print(f"{fav_fruit}, huh? My kids love {fav_fruit} as well!")

# Restart code option
    while True:
        answer1 = input('Want to do another equation? (y/n): ')
        if answer1 in ('y', 'n'):
            break
        print("Come again?")

    if answer1 == 'y':
        print("Very well!")
        # continue doing math (not shown here)
    else:
        while True:
            answer2 = input("You can't do that! (a/b):\n(a) I want to go.\n(b) Alright, I'll do another equation.\n")
            if answer2 in ('a', 'b'):
                break
            print("What?")

        if answer2 == 'a':
            while True:
                answer3 = input(
                    "Hahaha, no, I won't let you go, we WILL do math. (a/b):\n(a) You can't tell me what to do, I am leaving.\n(b) Alright, I'll do another equation.\n")
                if answer3 in ('a', 'b'):
                    break
                print("What?")

            if answer3 == 'a':
                print("Wait, don't do it NOOOO DON-")
                break
            else:
                print("Good choice!")
        else:
            print("Good choice!")


# Links used while working on this assignment:
# A small support of ChatGPT was used in this project, to resolve errors (of course after the attempts to find the solution by myself were unsuccessful)
# and for checking if the code fulfills all the main requirements of the assignment
# https://stackoverflow.com/questions/68629361/how-do-i-convert-a-string-from-an-input-into-an-integer-python-3-9
# https://stackoverflow.com/questions/5424716/how-can-i-check-if-string-input-is-a-number
# https://www.reddit.com/r/learnpython/comments/7i1wel/whats_the_easiest_way_to_check_if_an_input_is_an/
# https://stackoverflow.com/questions/14907067/how-do-i-restart-a-program-based-on-user-input