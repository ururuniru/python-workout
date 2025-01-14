import random

def guessing_game():
    x = random.randint(1, 100)
    attempts = 0

    while True:
        y = input("Try guessing the number, pick a number from 1 to 100: ")
        attempts += 1
        try:
            y = int(y)
        except ValueError:
            print("That's not a number!")
            continue

        if y < 1 or y > 100:
            print("Hey, I said a number from 1 to 100!")
        elif y > x:
            print("Too high!")
        elif y < x:
            print("Too low!")
        else:
            print(f"Just right! It took you {attempts} attempts.")
            break

guessing_game()
