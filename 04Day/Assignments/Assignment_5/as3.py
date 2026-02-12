import random

def guessing_game():
    num = random.randint(1, 100)
    guessed = False
    tries = 1
    while not guessed and tries <= 7:
        guess = int(input("guess: "))
        if guess == num:
            print(f"you won! number was {num} [tries left: {7-tries}]")
            guessed = True
        elif guess < num:
            print(f"lower [tries left: {7-tries}]")
        else:
            print(f"higher [tries left: {7-tries}]")
        tries += 1
    if tries == 8:
        print(f"you lose! number was {num}")

guessing_game()