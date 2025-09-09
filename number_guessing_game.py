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
    print("Choose a difficulty level: Easy (10 attempts), Medium (7 attempts), Hard (5 attempts)")

    # Difficulty selection
    while True:
        difficulty = input("Enter difficulty (easy/medium/hard): ").lower()
        if difficulty == "easy":
            max_attempts = 10
            break
        elif difficulty == "medium":
            max_attempts = 7
            break
        elif difficulty == "hard":
            max_attempts = 5
            break
        else:
            print("⚠️ Invalid choice. Please select Easy, Medium, or Hard.")

    secret_number = random.randint(1, 100)
    attempts = 0
    hint_given = False

    while attempts < max_attempts:
        try:
            guess = int(input(f"({max_attempts - attempts} attempts left) Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again ⬆️")
            elif guess > secret_number:
                print("Too high! Try again ⬇️")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break

            # Give a hint after 3 wrong attempts
            if attempts == 3 and not hint_given:
                hint = "even" if secret_number % 2 == 0 else "odd"
                print(f"💡 Hint: The number is {hint}.")
                hint_given = True

        except ValueError:
            print("⚠️ Please enter a valid number.")

    else:
        print(f"😢 Game Over! The correct number was {secret_number}.")

    # Replay option
    play_again = input("🔁 Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        number_guessing_game()
    else:
        print("👋 Thanks for playing! Goodbye.")

if __name__ == "__main__":
    number_guessing_game()

