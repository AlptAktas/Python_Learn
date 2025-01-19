import random


def number_guessing_game(difficulty):
    number = random.randint(1, 100)
    attempts = 0
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print("Invalid difficulty. Please try again.")
        return

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print(f"You got it! The answer was {number}.")
            return
        attempts -= 1
    print(f"You've run out of guesses. The answer was {number}.")


print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
number_guessing_game(difficulty)