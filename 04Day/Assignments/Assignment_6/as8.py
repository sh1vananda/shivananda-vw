print("1. circle  2. square  3. rectangle")

choice = int(input())

match choice:
    case 1:
        r = int(input("enter radius: "))
        print(f"circumference = {2*3.14*r}\narea = {3.14*r*r}")
    case 2:
        s = int(input("enter length of side: "))
        print(f"perimeter = {4*s}\narea = {s*s}")
    case 3:
        l, b = list(map(int, input("enter length and breadth: ").split()))
        print(f"perimeter = {2*(l+b)}\narea = {l*b}")
    case _:
        print("invalid choice")