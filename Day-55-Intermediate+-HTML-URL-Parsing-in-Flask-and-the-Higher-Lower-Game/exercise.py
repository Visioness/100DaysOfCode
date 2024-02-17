from flask import Flask


app = Flask(__name__)


def make_bold(func):
    def wrapper_function():
        return f'<b>{func()}</b>'
    
    return wrapper_function


def make_emphasis(func):
    def wrapper_function():
        return f'<em>{func()}</em>'
    
    return wrapper_function


def make_underlined(func):
    def wrapper_function():
        return f'<u>{func()}</u>'
    
    return wrapper_function


@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def homepage():
    return '<h2>Bye!</h2>'


if __name__ == '__main__':
    app.run(debug=True)