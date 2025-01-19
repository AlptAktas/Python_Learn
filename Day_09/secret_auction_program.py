import os

bidders = {}


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def find_highest_bidder(bidders):
    highest_bid = 0
    highest_bidder = ''
    for bidder_name in bidders:
        if bidders[bidder_name] > highest_bid:
            highest_bid = bidders[bidder_name]
            highest_bidder = bidder_name
    return highest_bidder, highest_bid




print("Welcome to the secret auction")

while True:
    clear_console()
    bidder_name = input("What is your name? ")
    bidder_bid = int(input("What is your bid? $"))

    bidders[bidder_name] = bidder_bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more_bidders == 'no':
        break

highest_bidder, highest_bid = find_highest_bidder(bidders)
print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}")
