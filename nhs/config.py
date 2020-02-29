import os

DB = os.environ.get("POSTGRES_DB", "db")
USER = os.environ.get("POSTGRES_USER", "user")
PASSWORD = os.environ.get("POSTGRES_PWD", "")
HOSTNAME = os.environ.get("HOSTNAME", "localhost")

class Config(object):
    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOSTNAME}/{DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False