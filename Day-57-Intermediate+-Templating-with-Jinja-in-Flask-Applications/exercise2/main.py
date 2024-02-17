from flask import Flask
from flask import render_template
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    current_year = datetime.datetime.now().year
    return render_template('index.html', current_year=current_year)


@app.route('/blog')
def blog_post():
    blog_data = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()

    return render_template('blog.html', blog_data=blog_data)
if __name__ == '__main__':
    app.run(debug=True)