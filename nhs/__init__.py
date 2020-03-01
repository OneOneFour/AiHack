import os

from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import Config,ProductionConfig
from flask import Flask

app = Flask(__name__)
if os.environ.get("FLASK_ENV") == "production":
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

from .models import BNFStem, Location, Prescription, LocationPatientNumbers, CCG
from .views import *

