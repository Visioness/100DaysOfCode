import random

cards = {"A": [11, 1], "Q": 10, "K": 10, "J": 10, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "1": 1}
player1 = []
player2 = []
players = [player1, player2]
cards_keys = [cards.keys()]
def main():
    for i in range(2):
        player1.append(random.choice(cards_keys))
        player2.append(random.choice(cards_keys))
    
    turn = players[0]
    print(f"Your cards: {player1}\nComputer's first card: {player2[0]}")
    while not(check_value(players[0]) and check_value(players[1])):
        if input("Type 'y' to take a card, or 'n' to pass:  ") == "y":
            player1.append(random.choice(cards_keys))
        else:
            player2.append(random.choice(cards_keys))
            

def check_value(player1):
    cards_val = 0
    for card in player1:
        cards_val += cards[card]
    if cards_val > 21:
        return False


if __name__ == "__main__":
    main()