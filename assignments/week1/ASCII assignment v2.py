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