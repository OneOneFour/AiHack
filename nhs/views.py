import pandas as pd
from flask import jsonify
from flask_cors import cross_origin

from .schemas import BNFStemSchema, LocationSchema, PrescriptionSchema, PrescriptionWithBNF, CCGSchema
from . import app, db, BNFStem, Location, Prescription, CCG
from datetime import datetime


@app.route("/api/bnf_stems", methods=["GET"])
def get_bnf_stems():
    ps_schema = BNFStemSchema(many=True)
    ps = BNFStem.query.all()
    return jsonify(ps_schema.dump(ps))


@app.route("/api/locations", methods=["GET"])
def get_locations():
    location_schema = LocationSchema(many=True)
    locations = Location.query.all()
    return jsonify(location_schema.dump(locations))


@app.route("/api/locations/<code>", methods=["GET"])
def get_location(code):
    location_schema = LocationSchema()
    location = Location.query.filter(Location.gp_code == code).one()
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


@app.route("/api/ccg")
@cross_origin()
def get_ccgs():
    ccgs_schema = CCGSchema(many=True)
    ccgs = CCG.query.all()
    return jsonify(ccgs_schema.dump(ccgs))


@app.route("/api/graph/<code>/relative_usage")
def graph_of_relative_usage(code):
    for area_code in Prescription.PERMITTED_NG_CODE:
        prescriptions = Prescription.query.join(BNFStem).filter(BNFStem.code_stem == code).sort_by(
            Prescription.date_span).all()

