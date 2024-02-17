from flask import Flask
import random


app = Flask(__name__)

number = random.randint(0, 9)

@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>'\
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=400>'


@app.route('/<int:guess>')
def guess(guess):
    if guess > number:
        return '<h1 style="font-weight: bold; color: purple;">Too high, try again!</h1>'\
        '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=400>'
    elif guess < number:
        return '<h1 style="font-weight: bold; color: red;">Too low, try again!</h1>'\
        '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=400>'
    else:
        return '<h1 style="font-weight: bold; color: darkgreen;">You found me!</h1>'\
        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=400>'
    

if __name__ == '__main__':
    app.run(debug=True)