from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
import os

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance/cafes.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random')
def random_cafe():
    result = db.session.execute(db.select(Cafe))
    cafes = result.scalars().all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route('/all')
def all_cafes():
    result = db.session.execute(db.select(Cafe))
    cafes = result.scalars().all()
    return jsonify(all_cafes=[cafe.to_dict() for cafe in cafes])


@app.route('/search')
def find_cafe():
    location = request.args.get('loc')
    result = db.session.execute(db.select(Cafe).where(Cafe.location == location))
    cafes = result.scalars().all()
    if cafes:
        return jsonify(cafe=[cafe.to_dict() for cafe in cafes])
    return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        seats=request.form.get('seats'),
        has_toilet=bool(request.form.get('has_toilet')),
        has_wifi=bool(request.form.get('has_wifi')),
        has_sockets=bool(request.form.get('has_sockets')),
        can_take_calls=bool(request.form.get('can_take_calls')),
        coffee_price=request.form.get('coffee_price'),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={'success': 'Successfully added the new cafe.'})


# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def change_price(cafe_id):
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    new_price = request.args.get('new_price')
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(success='Successfully updated the price.')
    return jsonify(error={'Not Found': 'Sorry a cafe with that id was not found in the database.'}), 404


# HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def remove_cafe(cafe_id):
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    if cafe:
        if request.args.get('api-key') == 'TopSecretAPIKey':
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(success='Successfully deleted the cafe.')
        return jsonify(error='Sorry that\'s not allowed. Make sure you have the correct api-key.')
    return jsonify(error={'Not Found': 'Sorry a cafe with that id was not found in the database.'})


if __name__ == '__main__':
    app.run()
