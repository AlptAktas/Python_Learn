import random



class Blackjack:
    _cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    @staticmethod
    def _deal_card():
        """Returns a random card from the deck"""

        card = random.choice(Blackjack._cards)
        return card

    @staticmethod
    def _calculate_score(cards):
        """Returns the score of the player or computer"""

        return sum(cards)

    @staticmethod
    def blackjack():
        """Starts the game of Blackjack"""

        player_cards = []
        computer_cards = []

        for _ in range(2):
            player_cards.append(Blackjack._deal_card())
            computer_cards.append(Blackjack._deal_card())

        print(f"Your cards: {player_cards}, current score: {Blackjack._calculate_score(player_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")

        while sum(player_cards) < 21:
            draw_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if draw_card == 'y':
                player_cards.append(Blackjack._deal_card())
                print(f"Your cards: {player_cards}, current score: {Blackjack._calculate_score(player_cards)}")
            else:
                break

        while sum(computer_cards) < 17:
            computer_cards.append(Blackjack._deal_card())

        print(f"Your final hand: {player_cards}, final score: {Blackjack._calculate_score(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {Blackjack._calculate_score(computer_cards)}")

        if Blackjack._calculate_score(player_cards) > 21:
            print("You went over. You lose.")
        elif Blackjack._calculate_score(computer_cards) > 21:
            print("Computer went over. You win.")
        elif Blackjack._calculate_score(player_cards) > Blackjack._calculate_score(computer_cards):
            print("You win.")
        elif Blackjack._calculate_score(player_cards) < Blackjack._calculate_score(computer_cards):
            print("You lose.")
        else:
            print("It's a draw.")


while True:
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_again == 'n':
        print("Goodbye!")
        break
    elif play_again == 'y':
        Blackjack.blackjack()
    else:
        print("Invalid input. Please try again.")
        continue
