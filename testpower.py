import random
import math

start = input("Start Game? (Y/N): ").upper() == 'Y'

while start:
    power = random.randint(2, 10)
    # number = random.randint(2, 9)
    number = 5


    ans = int(input(f"Enter value of {number}^{power}\n"))

    result = int(number**power)  # Corrected the calculation here

    print(f"You were within {(result - ans) * 100 / result} %.\n=============\nCorrect answer = {result}")

    # Ask if the user wants to continue
    continue_game = input("Do you want to continue? (Y/N): ").upper()
    if continue_game != "Y":
        start = False
