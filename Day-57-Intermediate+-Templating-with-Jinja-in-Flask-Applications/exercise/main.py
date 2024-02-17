from flask import Flask
from flask import render_template
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    current_year = datetime.datetime.now().year
    return render_template('index.html', current_year=current_year)


@app.route('/guess/<name>')
def genderize(name):
    gender_response = requests.get(f'https://api.genderize.io?name={name}').json()
    age_response = requests.get(f'https://api.agify.io?name={name}').json()

    age = age_response['age']
    gender = gender_response['gender']

    return render_template('guess.html', age=age, gender=gender, name=name)
if __name__ == '__main__':
    app.run(debug=True)