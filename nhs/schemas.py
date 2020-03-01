from .models import Prescription, BNFStem, Location, LocationPatientNumbers, CCG
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
        exclude = ("id",)


class CCGSchema(ma.Schema):
    class Meta:
        fields = ("ccg_code", "gp_surgeries")

    gp_surgeries = ma.Nested(LocationSchema,many=True)
