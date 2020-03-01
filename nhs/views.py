from flask import jsonify

from .schemas import BNFStemSchema, LocationSchema, PrescriptionSchema, PrescriptionWithBNF
from . import app, db, BNFStem, Location, Prescription
from datetime import datetime


@app.route("/api/bnf_stems", methods=["GET"])
def get_bnf_stems():
    ps_schema = BNFStemSchema(many=True)
    ps = db.session.query(BNFStem).all()
    return jsonify(ps_schema.dump(ps))


@app.route("/api/locations", methods=["GET"])
def get_locations():
    location_schema = LocationSchema(many=True)
    locations = db.session.query(Location).all()
    return jsonify(location_schema.dump(locations))


@app.route("/api/locations/<code>", methods=["GET"])
def get_location(code):
    location_schema = LocationSchema()
    location = db.session.query(Location).filter(Location.gp_code == code).one()
    return jsonify(location_schema.dump(location))


@app.route("/api/locations/<code>/prescriptions", methods=["GET"])
def get_location_prescriptions(code):
    prescription_schema = PrescriptionWithBNF(many=True)
    prescriptions = Prescription.query.filter(Prescription.location.has(gp_code=code))
    return jsonify(prescription_schema.dump(prescriptions))


@app.route("/api/locations/<code>/<int:year>/<int:month>")
def get_location_prescriptions_in_timeframe(code, year, month):
    t = datetime(year=year, month=month, day=1)
    pres = Prescription.query.filter(Prescription.location.has(gp_code=code)).filter(Prescription.date_span == t)
    prescription_schema = PrescriptionWithBNF(many=True)
    return jsonify(prescription_schema.dump(pres))
