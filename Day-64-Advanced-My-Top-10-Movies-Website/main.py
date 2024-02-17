from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms import validators
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv


load_dotenv('/mnt/c/Users/VISIONESS/Projects/100DaysOfPython/keys.env')

url = "https://api.themoviedb.org/3/search/movie?query="
detail_url = 'https://api.themoviedb.org/3/movie/'

headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {os.environ.get('MOVIEDB_READ')}"
        }

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'top-10-movies.db')
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()


class RatingForm(FlaskForm):
    new_rating = DecimalField(label='Your Rating Out Of 10 (e.g. 7.5)', validators=[DataRequired()], places=1, number_format='#0.0')
    new_review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')


class MovieForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Search')


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    movies = result.scalars().all()
    
    for movie in movies:
        movie.ranking = len(movies) - movies.index(movie)
    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    rating_form = RatingForm()
    id = request.args.get('id')
    if id:
        if rating_form.validate_on_submit():
            movie_to_update = db.get_or_404(Movie, id)
            movie_to_update.rating = float(rating_form.new_rating.data)
            movie_to_update.review = rating_form.new_review.data
            db.session.commit()
            return redirect(url_for('home'))
        return render_template('edit.html', rating_form=rating_form)

    movie_id = request.args.get('movie_id')
    response = requests.get(url=detail_url + movie_id, headers=headers)
    movie_detail = response.json()
    new_movie = Movie(
        title=movie_detail['title'],
        img_url=f'https://image.tmdb.org/t/p/w500{movie_detail["poster_path"]}',
        year=int(movie_detail['release_date'].split('-')[0]),
        description=movie_detail['overview'],
    )
    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for('edit', id=new_movie.id))


@app.route('/delete')
def delete():
    id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))
    

@app.route('/add', methods=['GET', 'POST'])
def add():
    movie_form = MovieForm()
    if movie_form.validate_on_submit():
        query = movie_form.title.data
        response = requests.get(url=url + query, headers=headers).json()
        movies = response['results']
        return render_template('select.html', movies=movies)
    
    return render_template('add.html', movie_form=movie_form)


if __name__ == '__main__':
    app.run()
