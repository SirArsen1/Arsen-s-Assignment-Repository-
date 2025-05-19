import time, sys

def typew(dialogue):
    for char in dialogue:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
        if char !=(" ","\n"):
            time.sleep(0.01)
        else:
            time.sleep(0.001)

if __name__ == '__main__':
    typew()