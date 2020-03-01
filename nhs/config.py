import os

import sqlalchemy

DB = os.environ.get("POSTGRES_DB", "db")
USER = os.environ.get("POSTGRES_USER", "user")
PASSWORD = os.environ.get("POSTGRES_PWD", "")
HOSTNAME = os.environ.get("HOSTNAME", "")
EXTENSION = os.environ.get("EXTENSION", "")
CLOUD_INSTANCE = "aihack2020:europe-west1:nhsdb"


class Config(object):
    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOSTNAME}/{DB}{EXTENSION}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = sqlalchemy.engine.url.URL(
        drivername="postgresql",
        username=USER,
        password=PASSWORD,
        database=DB,
        query={
            "host": '/cloudsql/{}'.format(CLOUD_INSTANCE)
        }
    )
