import random

word_list = ["aardvark", "baboon", "camel"]

random_word = random.choice(word_list)
word_length = len(random_word)

display = ["_"] * word_length

user_health = 6


def update_display(user_guess):
    global user_health
    if user_guess in random_word:
        for index, letter in enumerate(random_word):
            if letter == user_guess:
                display[index] = user_guess
    else:
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        user_health -= 1
        
    
        
        
        # if user_guess in random_word:
        #     if user_guess in display:
        #         print(f"You've already guessed {user_guess}")
        #     else:
        #         display[random_word.index(user_guess)] = user_guess
        #         print(f"{' '.join(display)}")


def game_loop():
    while "_" in display:
        print(f"{' '.join(display)}")

        user_guess = input("Guess a letter: ").lower()
        update_display(user_guess)

        if "_" not in display:
            print(f"{' '.join(display)}")
            print("You win!")
            break
        if user_health == 0:
            print("You lose!")
            break
game_loop()



