from flask import Flask, render_template
import requests
import sys

app = Flask(__name__)

try:
    blogs = requests.get('https://api.npoint.io/04a77953a0227b8cc71b').json()
except:
    sys.exit('Could not get data!')


@app.route('/')
def homepage():
    return render_template('index.html', blogs=blogs)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:id>')
def post(id):
    for blog in blogs:
        if blog['id'] == id:
            return render_template("post.html", blog=blog)



if __name__ == '__main__':
    app.run(debug=True)