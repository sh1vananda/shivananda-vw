import random

def password_generator(num):
    if num < 8 or num > 12:
        return "password length must be between 8-12"
    
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = lower_case.upper()
    digits = "0123456789"
    characters = "!@#$%^&*"

    password = []

    password.append(random.choice(lower_case))
    password.append(random.choice(upper_case))
    password.append(random.choice(digits))
    password.append(random.choice(characters))

    temp = lower_case + upper_case + digits + characters

    for i in range(num - 4):
        password.append(random.choice(temp))

    random.shuffle(password)

    print("".join(password))

length = int(input("enter password length (8-12): "))

password_generator(length)