from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.db_config import db_uri

app = Flask(__name__)
app.config.from_object('app.config')
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db_uri is stored in db_config.py

db = SQLAlchemy(app)

from . import routes, models
