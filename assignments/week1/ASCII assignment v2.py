import time,sys

art = ('''
          /\____/\ 
        _(@ ).(@ )|_
         \   ^    /_______
          |               \ 
          |  n  r-----|    \ 
          |  || |   | |  |\ \ ''')

explainer = ('''\nMy attempt at creating a cat,\nwithout using online ascii-art generators''')

def typew(art):
    for char in art:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
        if char !=(" ","\n"):
            time.sleep(0.0001)
        else:
            time.sleep(0.05)

def typew2(explainer):
    for char in explainer:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
        if char !="\n":
            time.sleep(0.0001)
        else:
            time.sleep(0.1)

typew(art)
typew2(explainer)

#tutorial used: https://youtu.be/2h8e0tXHfk0?si=LQCgwk4QisDNc50y