import random
from game_data import data
from art import logo, vs
import os

score = 0
def main():
    person_a = get_data(data)
    person_b = get_data(data)
    os.system("clear")
    compare_person(person_a, person_b)
        

def get_data(data):
    return data.pop(random.randint(0, len(data) - 1))


def compare_person(person_a, person_b):
    global score
    print(logo)
    print(f"Compare A: {person_a['name']}, a/an {person_a['description']}, from {person_a['country']}")
    print(vs)
    print(f"Against B: {person_b['name']}, a/an {person_b['description']}, from {person_b['country']}")
    guess = input("Who has more followers? Type 'A' or 'B': ")
    while guess not in ["A", "B"]:
        guess = input("Who has more followers? Type 'A' or 'B': ")
    
    guess, other = (person_a, person_b) if guess == "A" else (person_b, person_a)
    
    if guess["follower_count"] >= other["follower_count"]:
        score += 1
        os.system("clear")
        print(f"Correct! Current score is -> {score}")
        if data:
            compare_person(person_b, get_data(data))
        else:
            print(f"You won! Total score is {score}.")

    else:
        print(f"Wrong answer! Your score is -> {score}")


if __name__ == "__main__":
    main()