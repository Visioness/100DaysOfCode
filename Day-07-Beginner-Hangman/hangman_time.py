import random
import timeit
import string
from hangman_words import words_list
from hangman_stages import hangman

def my_function():
    print("\n\n--- Welcome to the Hangman MK.I by Visioness ---\n")
    print(" || Try guessing letters from the chosen word || ")

    chosen_list = []
    guesses = []
    lives = 6
    outoflives = False
    chosen = random.choice(words_list)

    for char in range(len(chosen)):
        chosen_list.append("_")
        print("_", end=" ")
    print()
    while lives > 0:
        print(hangman[lives])
        for char in chosen_list:
            print(char, end=" ")

        guess = random.choice(string.ascii_lowercase)

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

    if outoflives:
        print(hangman[0], f"\n\n   --- Out of lives. Game over! The word was --> {chosen} ---\n")
    else:
        print(f"\n\n --- Congratulations! The word was --> {chosen} --- \n")

def angela_function():
    #Step 5

    chosen_word = random.choice(words_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    #Create blanks
    display = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        guess = random.choice(string.ascii_lowercase)

        #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
        if guess in display:
            print(f"You've already guessed {guess}")

        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter

        #Check if user is wrong.
        if guess not in chosen_word:
            #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

        #Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        #Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")

        print(hangman[lives])


time1 = timeit.timeit(my_function, number=1000)
time2 = timeit.timeit(angela_function, number=1000)

print(f"Code 1 time: {time1}, Code 2 time: {time2}")