from . import Session
from .models import Location

with Session() as sesh:
    sesh.query(Prescription).filter(Prescription.bnf_code("043"))
session = Session(Prescription)