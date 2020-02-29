from .models import Prescription,BNFStem,Location,LocationPatientNumbers
from . import ma

class PrescriptionSchema(ma.Schema):
    class Meta:
        fields = ("number_of_perscriptions","date_span","bnf_code","location")

class BNFStemSchema(ma.Schema):
    class Meta:
        fields = ("code_stem","code_name")