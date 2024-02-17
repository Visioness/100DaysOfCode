from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import os

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'pretty-new-books-collection.db')
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


    def __repr__(self):
        return f'<Book {self.title}>'

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        book_id = request.form.get('delete_id')
        print(book_id)
        book_to_delete = db.get_or_404(Book, book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
    results = db.session.execute(db.select(Book).order_by(Book.title))
    books = results.scalars()
    return render_template('index.html', books=books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book_name = request.form.get('book_name')
        author = request.form.get('author')
        rating = request.form.get('rating')
        new_book = Book(
            title= book_name,
            author= author,
            rating= rating,
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        id = request.args.get('book_id')
        book_to_update = db.session.execute(db.select(Book).where(Book.id==id)).scalar()
        new_rating = request.form.get('new_rating')
        book_to_update.rating = float(new_rating)
        db.session.commit()
        return redirect(url_for('home'))
    
    id = request.args.get('book_id')
    book_to_update = db.session.execute(db.select(Book).where(Book.id==id)).scalar()
    return render_template('edit.html', book_to_update=book_to_update)


if __name__ == "__main__":
    app.run()
