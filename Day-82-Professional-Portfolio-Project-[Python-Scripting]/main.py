import string


MORSE_ALPHABET = {
    'A': '•-', 'B':'-•••', 'C':'-•-•', 'D':'-••', 'E':'•',
    'F':'••-•', 'G':'--•', 'H':'••••', 'I':'••', 'J':'•---',
    'K':'-•-', 'L':'•-••', 'M':'--', 'N':'-•', 'O':'---',
    'P':'•--•', 'Q':'--•-', 'R':'•-•', 'S':'•••', 'T':'-',
    'U':'••-', 'V':'•••-', 'W':'•--', 'X':'-••-', 'Y':'-•--',
    'Z':'--••', '0':'-----', '1':'•----', '2':'••---',
    '3':'•••--', '4':'••••-', '5':'•••••', '6':'-••••',
    '7':'--•••', '8':'---••', '9':'----•'
}

keys = list(MORSE_ALPHABET.keys())
values = list(MORSE_ALPHABET.values())


def convert_message(message, mode):
    if mode == '1':
        result = [keys[values.index(char)] if char in values else ' ' for char in message.split()]
        result = ''.join(result).replace('/', ' ').capitalize()
    else:
        result = [MORSE_ALPHABET[char] if char in keys else ' ' for char in message]
        result = ' '.join(result).replace('   ', ' / ')

    return result if result.strip() != '' else 'This is not a valid message!'


mode = 0
while mode != '1' and mode != '2':
    mode = input('Type "1" or "2" to choose the mode.\n' 
                '1 - (Morse to Text)\n'\
                '2 - (Text to Morse)\n')

message = input('\n-- Enter your message to convert --\n').upper()

print(convert_message(message=message, mode=mode))
