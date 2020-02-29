from . import Session
from .models import Location

session = Session()
session.query(Location).filter(Location.gp_name="")