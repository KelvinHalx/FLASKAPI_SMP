from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#Initialize Application
app = Flask(__name__)

#Setting up working folder location direction
basedir = os.path.abspath(os.path.dirname(__file__))

#Creating database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initialize the database
db = SQLAlchemy(app)

#Initialize marshmallow
ma = Marshmallow(app)

if __name__ == '__main__':
    app.run(debug=True)
