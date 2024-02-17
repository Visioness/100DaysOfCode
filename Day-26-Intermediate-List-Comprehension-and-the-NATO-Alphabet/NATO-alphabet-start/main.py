student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_alphabet.to_dict())

"""nato_alphabet = nato_alphabet.to_dict()
cipher = {nato_alphabet["letter"][index]: nato_alphabet["code"][index] for index in range(len(nato_alphabet["letter"]))}"""

cipher = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
# print(cipher)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

phrase = input("Enter the phrase you want in Nato Alphabet: ").upper()

new_phrase = [cipher[letter] if letter in cipher else letter for letter in phrase]

print(new_phrase)