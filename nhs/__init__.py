from sqlalchemy import create_engine
import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB = os.environ.get("POSTGRES_DB", "db")
USER = os.environ.get("POSTGRES_USER", "user")
PASSWORD = os.environ.get("POSTGRES_PWD", "")
HOSTNAME = os.environ.get("HOSTNAME", "localhost")

engine = create_engine(f"postgresql://{USER}:{PASSWORD}@{HOSTNAME}/{DB}")
Session = sessionmaker(bind=engine)
Base = declarative_base()

