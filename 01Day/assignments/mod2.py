import mod1

while True:
    print("1. all nums  2. even nums  3. odd nums  4. exit")
    c = int(input("choice: "))
    if c not in (1, 2, 3):
        break
    r = int(input("range: "))
    if c == 1:
        mod1.print_all(r) # will not work because calling through import and not in module scope
        print()
    elif c == 2:
        mod1.print_even(r)
        print()
    elif c == 3:
        mod1.print_odd(r)
        print()
    else:
        print("invalid input")
        