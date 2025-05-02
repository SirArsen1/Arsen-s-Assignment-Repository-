import time, sys

def typew(dialogue):
    for char in dialogue:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
        if char !=(" ","\n"):
            time.sleep(0.05)
        else:
            time.sleep(0.01)

if __name__ == '__main__':
    typew()