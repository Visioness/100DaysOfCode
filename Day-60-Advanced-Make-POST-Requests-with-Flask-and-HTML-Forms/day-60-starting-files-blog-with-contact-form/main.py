from flask import Flask, render_template, request
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv('/mnt/c/Users/VISIONESS/Projects/100DaysOfPython/keys.env')

MY_EMAIL = os.environ.get('MY_EMAIL')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/04a77953a0227b8cc71b").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html", title='Contact Me')
    else:
        username, email, phone, message = request.form['name'], request.form['email'], request.form['phone'], request.form['message']
        print(f'{username}\n{email}\n{phone}\n{message}')
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg='Subject:Blog Contact\n\n'\
                                f'Username: {username}\nEmail: {email}\nPhone: {phone}\nMessage: {message}')
        return render_template("contact.html", title='Successfully sent your message!')


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
