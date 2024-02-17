from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap5
import smtplib
import os
from dotenv import load_dotenv


load_dotenv('/mnt/c/Users/VISIONESS/Projects/100DaysOfPython/keys.env')

MY_EMAIL = os.environ.get('MY_EMAIL')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
SECRET_KEY = os.environ.get('SECRET_KEY')

app = Flask(__name__)
app.secret_key = SECRET_KEY
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/projects')
def show_projects():
    return render_template('projects.html')


@app.route('/about')
def show_info():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def get_contact():
    is_sent = False

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if name and email and message:
            with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg='Subject:Portfolio Connect\n\n'\
                    f'{message}\n\n\n'\
                    f'\t\t\t\t{name}\n'\
                    f'\t\t\t{email}\n\n\n',
                )
            is_sent = True
            flash('Sent your message!')
        else:
            flash('Name, email and message required. Please try again!')
            
    return render_template('contact.html', is_sent=is_sent)


if __name__ == '__main__':
    app.run(debug=True)