import time,sys

art = ('''
          /\____/\ 
        _(@ ).(@ )|_
         \   ^    /_______ 
          |               \ 
          |  n  r-----|    \ 
          |  || |   | |  |\ \ 
          
          My attempt at creating a cat, 
          without using online ascii-art generators
          ''')

def typew(art):
    for char in art:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

typew(art)

#tutorial used: https://youtu.be/2h8e0tXHfk0?si=LQCgwk4QisDNc50y