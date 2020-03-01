import os
from . import db
from sqlalchemy.orm.exc import NoResultFound
import pandas as pd
from tqdm import tqdm
import csv


class CCG(db.Model):
    """
    Clinicial Commissioning
    """
    __tablename__ = "ccgs"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    ccg_code = db.Column(db.String, unique=True)
    gp_surgeries = db.relationship("Location", backref="ccg")


class LocationPatientNumbers(db.Model):
    __tablename__ = "patient_age_groups"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    total_number = db.Column(db.Integer)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    location = db.relationship("Location", backref=db.backref("location_patient_numbers", uselist=False))

    @staticmethod
    def add_patient_numbers_from_csv(csv_path):
        try:
            with open(csv_path) as csv_file:
                reader = csv.DictReader(csv_file)
                locations = db.session.query(Location).all()
                for row in reader:
                    location = next(l for l in locations if l.gp_code == row["CODE"])
                    location_patient_numbers = LocationPatientNumbers(total_number=row["NUMBER_OF_PATIENTS"],
                                                                      location=location)
                    db.session.add(location_patient_numbers)
            db.session.commit()
        except:
            import traceback
            traceback.print_exc()
            db.session.rollback()
        finally:
            db.session.close()


class Location(db.Model):
    PERMITTED_NG_CODE = ["Y63", "Y62", "Y59", "Y56", "Y60", "Y58", "Y61"]

    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    gp_code = db.Column(db.String, unique=True)
    gp_name = db.Column(db.String)
    gp_ntgroup = db.Column(db.String, nullable=True)
    gp_ons_code = db.Column(db.String, unique=True)
    gp_fulladdress = db.Column(db.String)
    gp_postcode = db.Column(db.String)
    prescriptions = db.relationship("Prescription", backref="location")
    ccg_id = db.Column(db.Integer, db.ForeignKey("ccgs.id"))

    @property
    def total_number(self):
        return self.location_patient_numbers.total_number

    @classmethod
    def get_dataframe(cls):
        df = pd.read_sql(f"SELECT * FROM {cls.__tablename__}", db.engine)
        return df

    @staticmethod
    def update_from_csv(csv_path):
        try:
            with open(csv_path) as csv_file:
                reader = csv.DictReader(csv_file, delimiter=",")
                for row in reader:
                    location = Location.query.filter(Location.gp_code == row["CODE"]).one()
                    location.gp_postcode = row["POSTCODE"]
                    try:
                        location.ccg_id = CCG.query.filter(CCG.ccg_code == row["CCG_CODE"]).one().id
                    except NoResultFound:
                        location.ccg = CCG(ccg_code=row["CCG_CODE"])
                        db.session.add(location.ccg)
            db.session.commit()
        except:
            import traceback
            traceback.print_exc()
            db.session.rollback()
        finally:
            db.session.close()

    @staticmethod
    def load_from_csv(csv_path):
        try:
            with open(csv_path) as csv_file:
                reader = csv.reader(csv_file, delimiter=",")
                for row in reader:
                    full_address = ",".join(row[4:10])
                    gp = Location(gp_code=row[0], gp_name=row[1], gp_fulladdress=full_address)
                    db.session.add(gp)
            db.session.commit()
        except:
            import traceback
            traceback.print_exc()
            db.session.rollback()
        finally:
            db.session.close()


class BNFStem(db.Model):
    __tablename__ = "bnf_stems"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    code_stem = db.Column(db.Integer, unique=True)
    code_name = db.Column(db.String)
    prescriptions = db.relationship("Prescription", backref="bnf_code")

    @classmethod
    def get_dataframe(cls):
        df = pd.read_sql(f"SELECT * FROM {cls.__tablename__}", db.engine)
        return df

    @staticmethod
    def load_from_csv(csv_path):
        """
        Create this in the engine table if it does not already exists
        :param CSV_path:
        :return:
        """
        try:
            with open(csv_path) as csv_file:
                reader = csv.reader(csv_file, delimiter=",")
                headers = next(reader, None)
                for row in reader:
                    stem = BNFStem(code_stem=row[0], code_name=row[1])
                    db.session.add(stem)
            db.session.commit()
        except:
            import traceback
            traceback.print_exc()
            db.session.rollback()
        finally:
            db.session.close()

    def __repr__(self):
        return str(self.code_stem)


class Prescription(db.Model):
    __tablename__ = "prescriptions"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    bnf_code_id = db.Column(db.Integer, db.ForeignKey("bnf_stems.id"))

    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    number_of_prescriptions = db.Column(db.Integer)
    date_span = db.Column(db.Date)

    @classmethod
    def get_dataframe(cls):
        df = pd.read_sql(f"SELECT * FROM {cls.__tablename__}", db.engine)
        return df

    @staticmethod
    def load_from_csv(BASE_DIR, prefix):
        from glob import glob
        from datetime import datetime
        all_files = glob(f"{BASE_DIR}/{prefix}**.csv")
        try:
            for file in all_files:
                base = os.path.basename(file)
                bnfcode = os.path.splitext(base)[0]
                locations = db.session.query(Location).all()
                bnfs = db.session.query(BNFStem).all()
                with open(file) as csv_file:
                    reader = csv.reader(csv_file)
                    header = next(reader, None)

                    for row in reader:
                        dict_arr = []
                        for i, h in tqdm(enumerate(header)):
                            if not row[i].isnumeric():
                                continue
                            try:
                                location = next(l for l in locations if l.gp_code == h)
                                bnf = next(b for b in bnfs if b.code_stem == int(bnfcode))
                                dict_arr.append({"location_id": location.id, "bnf_code_id": bnf.id,
                                                 "date_span": datetime.strptime(row[0], "%Y-%m-%d"),
                                                 "number_of_prescriptions": row[i]})

                            except (NoResultFound,StopIteration):
                                print(f"No results found for code:{h},bnf_code:{bnfcode}")
                        db.session.bulk_insert_mappings(Prescription, dict_arr)
                    db.session.commit()
        except:
            import traceback
            traceback.print_exc()
            db.session.rollback()
        finally:
            db.session.close()

    def __repr__(self):
        return f"Prescriptions: {self.number_of_prescriptions} of {self.bnf_code} at {self.location} on {self.date_span}"
