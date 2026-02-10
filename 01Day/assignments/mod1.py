def print_all(x):
    if __name__ == "mod1": # should hide print_all functionality from files using this module
        print("not callable here") 
        return
    for a in range(0, x + 1):
        print(a, end=" ")

def print_even(x):
    for e in range(0, x + 1, 2):
        print(e, end=" ")

def print_odd(x):
    for o in range(1, x + 1, 2):
        print(o, end=" ")

if __name__ == "__main__":
    while True:
        print("1. all nums  2. even nums  3. odd nums  4. exit")
        c = int(input("choice: "))
        if c not in (1, 2, 3):
            break
        r = int(input("range: "))
        if c == 1:
            print_all(r) # works because calling in module scope
            print()
        elif c == 2:
            print_even(r)
            print()
        elif c == 3:
            print_odd(r)
            print()
        else:
            print("invalid input")