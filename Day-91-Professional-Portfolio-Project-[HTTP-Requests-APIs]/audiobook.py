from gtts import gTTS
from PyPDF2 import PdfReader
import requests
from dotenv import load_dotenv
import os

load_dotenv('/mnt/c/Users/VISIONESS/Projects/100DaysOfCode/100Days/keys.env')

def read_pdf(filename): 
    reader = PdfReader(filename)
    number_of_pages = len(reader.pages)
    pages = ''
    for page in reader.pages:
        pages += f'{page.extract_text()}\n\n '

    return pages


def text_to_speech(text, file_to_save):
    url = f'http://api.voicerss.org/?key={os.environ.get("VOICERRS_TTS")}'
    parameters = {
        'hl': 'en-gb',
        'v': 'Lily',
        'src': text,
    }
    response = requests.get(url=url, params=parameters)

    if response.status_code == 200:
        with open(file_to_save, 'wb') as f:
            f.write(response.content)
            print('Successfully created the audio!')
    else:
        print('Could not create the audio!')


def main():
    filename = input('Enter the PDF filename to convert to audio --> ')
    text = read_pdf(filename)
    print(text)
    file_to_save = f'{filename.split(".")[0]}_audio.mp3'
    text_to_speech(text, file_to_save)


if __name__ == '__main__':
    main()