from flask import jsonify

from .schemas import BNFStemSchema
from . import app, db, BNFStem


@app.route("/")
def hello_world():
    ps_schema = BNFStemSchema()
    ps = db.session.query(BNFStem).all()
    return jsonify(ps_schema.dump(ps))
