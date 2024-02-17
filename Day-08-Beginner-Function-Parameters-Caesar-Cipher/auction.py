import os

bids = {}

def main():
    while True:
        os.system("clear")
        name = input("What's your name?  ")
        bid = int(input("What's your bid?  $"))
        bids[name] = bid
        if input("Are there any other bidders? Type 'yes' or 'no'.\n").lower() == "no":
            break
        
    print(auction())


def auction():
    highest_bid = 0
    winner = None
    for key in bids:
        if bids[key] > highest_bid:
            highest_bid = bids[key]
            winner = key
    
    return f"The winner is {winner} with the bid of ${highest_bid}"


if __name__ == "__main__":
    main()
        