num = int(input("enter a number: "))

match num:
    case 0:
        print("zero")
    case _ if num > 0:
        print("positive")
    case _:
        print("negative")