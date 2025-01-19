import random
# Dİsplay Art

game_data = [
    {
        "name": "Instagram",
        "follower_count": 346,
        "description": "Social media platform",
        "country": "United States"
    },
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 215,
        "description": "Footballer",
        "country": "Portugal"
    },
    {
        "name": "Ariana Grande",
        "follower_count": 183,
        "description": "Musician and actress",
        "country": "United States"
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 181,
        "description": "Actor and professional wrestler",
        "country": "United States"
    },
    {
        "name": "Selena Gomez",
        "follower_count": 174,
        "description": "Musician and actress",
        "country": "United States"
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 172,
        "description": "Reality TV personality and businesswoman",
        "country": "United States"
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 167,
        "description": "Reality TV personality and businesswoman",
        "country": "United States"
    }
]


def higher_lower_game():
    print("Welcome to Higher Lower Game")
    print("Guess who has more followers")


    score = 0
    first_choice = None

    while True:
        if len(game_data) == 1:
            print("Congratulations! You have won the game")
            break

        if first_choice is None:
            first_choice = random.choice(game_data)
        second_choice = random.choice(game_data)
        while second_choice == first_choice:
            second_choice = random.choice(game_data)

        
        choice_list = {
            "a": first_choice,
            "b": second_choice
        }
        
        print(f"Compare A: {first_choice['name']}, a {first_choice['description']} from {first_choice['country']}")
        print("VS")
        print(f"Compare B: {second_choice['name']}, a {second_choice['description']} from {second_choice['country']}")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        other_choice = "b" if user_choice == "a" else "a"

        if choice_list[user_choice]["follower_count"] > choice_list[other_choice]["follower_count"]:
            score += 1
            print(f"Your score is {score}")
            
            game_data.remove(choice_list[other_choice])
            first_choice = choice_list[user_choice]

        else:
            print(f"Sorry, that's wrong. Your final score is {score}")
            break
    
    return score

higher_lower_game()