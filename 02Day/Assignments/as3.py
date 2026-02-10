num = input("enter 4 digit number: ")

print(f"a. {' '.join(num)}")

print(f"b. {num} = {int(num[0]) * 1000} + {int(num[1]) * 100} + {int(num[2]) * 10} + {num[3]}")

print(f"c. {num[::-1]}")