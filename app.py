from flask import Flask
from flask_restful import Api
from db import db
from books.resource import Review, ReviewList

app = Flask(__name__)
db.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/50043_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This turns off FlaskSQLAlchemy modification tracker but not SQLAlchemy modification tracker
api = Api(app)

api.add_resource(Review, '/review/')
api.add_resource(ReviewList, '/reviews/')

if __name__ == '__main__':
    app.run(port=5000, debug=True)