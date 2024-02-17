import string

def main():
    type = input("Type 'encode' for encrypt, 'decode' for decrypt.")
    while type != "decode" and type != "encode":
        type = input("Type 'encode' for encrypt, 'decode' for decrypt.")
        
    word = input(f"Enter the word that you want to {type}.")
    shift = int(input("Type the shift number."))

    print(caesar(word, type, shift))


def caesar(word, type, shift):
    newword = ""
    if type == "decode":
        shift *= -1
    for char in word:
        if char.islower():
            char = string.ascii_lowercase[(string.ascii_lowercase.index(char) + shift) % 26]
        elif char.isupper():
            char = string.ascii_uppercase[(string.ascii_uppercase.index(char) + shift) % 26]
        newword += char
    
    return newword


if __name__ == "__main__":
    main()