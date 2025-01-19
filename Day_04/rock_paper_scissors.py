import random

choice_list = [["0", "Rock"], ["1", "Paper"], ["2", "Scissors"]]


user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

print(f"You chose {choice_list[user_choice][1]}.")
print(f"Computer chose {choice_list[computer_choice][1]}.")

if user_choice == computer_choice:
    print("It's a draw.")

elif user_choice == 2 and computer_choice == 0:
    print("You lose.")

elif user_choice == 0 and computer_choice == 2:
    print("You win.")

elif computer_choice > user_choice:
    print("You lose.")

elif user_choice > computer_choice:
    print("You win.")

else:
    print("Invalid input.")
