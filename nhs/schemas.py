from .models import Prescription, BNFStem, Location, LocationPatientNumbers
from . import ma


class PrescriptionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Prescription


class BNFStemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BNFStem
        exclude = ("id",)


class PrescriptionWithBNF(ma.Schema):
    class Meta:
        fields = ("date_span", "number_of_prescriptions", "bnf_code")

    bnf_code = ma.Nested(BNFStemSchema)


class LocationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Location
