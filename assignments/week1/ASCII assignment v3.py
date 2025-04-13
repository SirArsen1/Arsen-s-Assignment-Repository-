import time,os
def clr_scr():
    print("\n" * 100)

frame3 = ('''
             o/
            /|      HI!
            / \ 
            ''')
frame2 = ('''
             o
            /|‾‾
            / \ 
            ''')
frame1 = ('''
             o
            /|\ 
            / \ 
            ''')
frames = [frame1, frame2, frame3, frame2]

for i in range(100):
    for item in frames:
        print(item)
        time.sleep(0.3)
        clr_scr()

# tutorial used: #https://www.youtube.com/watch?v=JavJqJHLo_M
# ChatGPT prompt1: "what should i do if i want to print an object from
#                   a list and then clean the screen,
#                   after which print next list object in python"
# ChatGPT prompt2: "the problem is in terminal it doesn't clear the screen, it just types the next line"
# ChatGPT prompt3: "I use Pycharm"