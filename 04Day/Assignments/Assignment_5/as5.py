import random

def captcha_generator():

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = lower_case.upper()
    digits = "0123456789"
    characters = "!@#$%^&*"

    captcha  = []

    temp = lower_case + upper_case + digits + characters

    for i in range(5):
        captcha.append(random.choice(temp))

    return "".join(captcha)

while True:
    captcha = captcha_generator()
    x = input(f"{captcha}: ")
    if x.lower() == captcha.lower():
        print("successful")
        flag = False
        break
    else:
        print("try again")