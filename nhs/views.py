from .schemas import BNFStemSchema
from . import app, db, BNFStem


@app.route("/")
def hello_world():
    ps_schema = BNFStem()
    ps = db.session(BNFStemSchema).all()
    return ps_schema.dump(ps)
