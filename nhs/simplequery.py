from . import Session
from .models import Prescription

with Session() as sesh:
    perscripts = sesh.query(Prescription).filter("0403" in Prescription.bnf_code).all()