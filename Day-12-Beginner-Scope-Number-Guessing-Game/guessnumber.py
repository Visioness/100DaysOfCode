import random

def main():
    difficulty = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose the difficulty. Type 'easy' for easy, 'hard' for hard: ")
    while difficulty not in ["hard", "easy"]:
        difficulty = input("\nChoose the difficulty. Type 'easy' for easy, 'hard' for hard: ")
    lives = 10 if difficulty == "easy" else 5
    random_number = random.randint(1, 100)
    print(check_number(lives, random_number))

def check_number(lives, random_number):
    while lives > 0:
        guess = int(input(f"You have {lives} attempts to guess the number.\nMake a guess: "))
        if guess == random_number:
            return f"You got it! The number was {random_number}."
        elif guess < random_number:
            print("Too low!")
        else:
            print("Too high!")
        lives -= 1
    return f"You have run out of lives. The number was {random_number}."


if __name__ == "__main__":
    main()