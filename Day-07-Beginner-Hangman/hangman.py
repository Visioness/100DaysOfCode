import random
import os
from hangman_words import words_list
from hangman_stages import hangman

chosen_list = []
guesses = []
lives = 6
outoflives = False
chosen = random.choice(words_list)

for char in range(len(chosen)):
    chosen_list.append("_")

while lives > 0:
    os.system('clear')
    print("\n\n--- Welcome to the Hangman MK.I by Visioness ---\n")
    print(" || Try guessing letters from the chosen word || ")
    print(hangman[lives])
    for char in chosen_list:
        print(char, end=" ")

    guess = input(" \t- Make a guess! - \n\nGuess --> ").lower()

    if guess == chosen:
        break

    if guess in chosen and guess not in guesses:
        print(f"\n-- You found letter --> {guess} --\n------------------------------------ ")
        for i, char in enumerate(chosen):
            if guess == chosen[i]:
                chosen_list[i] = guess
        guesses.append(guess)

    else:
        print("\n -- Not found in the chosen word --\n------------------------------------ ")
        lives -= 1
        if lives == 0:
            outoflives = True
            break

    if '_' not in chosen_list:
        break

os.system('clear')
if outoflives:    
    print(hangman[0], f"\n\n   --- Out of lives. Game over! The word was --> {chosen} ---\n")
else:
    print(hangman[lives], f"\n\n --- Congratulations! The word was --> {chosen} --- \n")
