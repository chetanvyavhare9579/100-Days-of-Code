#Number Guessing Game
"""
🎯 Number Guessing Game
Author: Chetan Vyavhare
# Day 1/100  #100DaysOfCode

Description:
A simple Python game where the user tries to guess
a randomly generated number within a given range.
"""

import random

def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number
    secret_number = random.randint(1, 100)

    attempts = 0
    guess = None

    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again ⬆️")
            elif guess > secret_number:
                print("Too high! Try again ⬇️")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()
