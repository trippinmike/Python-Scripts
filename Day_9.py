#author: N3m0m3N
#date: 10/24/2024
#description: Guessing Game (Day 9)

import random
value = random.randint(0, 10)
chances = 5

while chances > 0:
    print(f"You have {chances} left.")
    guess = int(input("Guess a number 0-10: \n"))
    if guess == value:
        print("Your guess is correct!")
    else:
        chances -= 1
        print("Incorrect, try again.")
        if chances == 0:
            print("Game over.")
            exit()

