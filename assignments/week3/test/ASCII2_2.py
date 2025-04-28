import os, sys, random

while True: #allows to restart the program later

    Num1 = None
    while Num1 is None:
        try:
            Num1 = int(input("please, write a number\n"))
        except ValueError:
            print ("We're doing math here! Write a number, please.\n")

    Num2 = None
    while Num2 is None:
        try:
            Num2 = int(input("please, write a second number\n"))
        except ValueError:
            print ("We're doing math here! Write a number, please.\n")

    Num1, Num2 = int(Num1), int(Num2)

    Answer = Num1 * Num2
    Equation = f"{Num1} * {Num2} = {Answer}"

    print(f'''                                                                                                                                                                                                                                                             
          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     
         ▒███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▒     
         ▒█▓                                                                                                                       ▒█▒     
         ▒█▓                                                                                                                       ▒█▒     
         ▒█▓                                                                                                                       ▒█▒     
         ▒█▓                    ░░░░                                                                                               ▒█▒     
         ▒█▓                ░████████▓                                                                                             ▒█▒     
         ▒█▓              ▓████████████▓                                                                                           ▒█▒     
         ▒█▓             ▓████████▓█▓███▓                           ░░░{Equation:^60}▒█▒     
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

# Restart code option
    while True:
        answer = input('Want to do another equation? (y/n): ')
        if answer in ('y', 'n'):
            break
        print("come again?")

    if answer == 'y':
        continue
    else:
        print("See you later!")
        break


# Links used while working on this assignment:
# A small support of ChatGPT was used in this project, to resolve errors (of course after the attempts to find the solution by myself were unsuccessful)
# https://stackoverflow.com/questions/68629361/how-do-i-convert-a-string-from-an-input-into-an-integer-python-3-9
# https://stackoverflow.com/questions/5424716/how-can-i-check-if-string-input-is-a-number
# https://www.reddit.com/r/learnpython/comments/7i1wel/whats_the_easiest_way_to_check_if_an_input_is_an/
# https://stackoverflow.com/questions/14907067/how-do-i-restart-a-program-based-on-user-input