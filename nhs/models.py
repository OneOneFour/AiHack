import os

from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import NoResultFound

from . import Base, Session
import csv


class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, nullable=False)
    gp_code = Column(String, unique=True)
    gp_name = Column(String)
    gp_fulladdress = Column(String)
    prescriptions = relationship("Prescription", backref="location")

    def __repr__(self):
        return f"{self.gp_code} : {self.gp_fulladdress}"

    @staticmethod
    def load_from_csv(csv_path):
        session = Session()
        try:
            with open(csv_path) as csv_file:
                reader = csv.reader(csv_file, delimiter=",")
                headers = next(reader, None)
                for row in reader:
                    full_address = ",".join(row[4:9])
                    gp = Location(gp_code=row[0], gp_name=row[1], gp_fulladdress=full_address)
                    session.add(gp)
            session.commit()
        except:
            import traceback
            traceback.print_exc()
            session.rollback()
        finally:
            session.close()


class BNFStem(Base):
    __tablename__ = "bnf_stems"
    id = Column(Integer, primary_key=True, nullable=False)
    code_stem = Column(Integer, unique=True)
    code_name = Column(String)
    prescriptions = relationship("Prescription", backref="bnf_code")

    @staticmethod
    def load_from_csv(csv_path):
        """
        Create this in the engine table if it does not already exists
        :param CSV_path:
        :return:
        """
        session = Session()
        try:
            with open(csv_path) as csv_file:
                reader = csv.reader(csv_file, delimiter=",")
                headers = next(reader, None)
                for row in reader:
                    stem = BNFStem(code_stem=row[0], code_name=row[1])
                    session.add(stem)
            session.commit()
        except:
            import traceback
            traceback.print_exc()
            session.rollback()
        finally:
            session.close()

    def __repr__(self):
        return f"{self.code_stem} : {self.code_name}"


class Prescription(Base):
    __tablename__ = "prescriptions"
    id = Column(Integer, primary_key=True, nullable=False)
    bnf_code_id = Column(Integer, ForeignKey("bnf_stems.id"))

    location_id = Column(Integer, ForeignKey("locations.id"))
    number_of_prescriptions = Column(Integer)
    date_span = Column(Date)

    @staticmethod
    def load_from_csv(BASE_DIR, prefix):
        from glob import glob
        from datetime import datetime
        all_files = glob(f"{BASE_DIR}/{prefix}**.csv")
        session = Session()
        try:
            for file in all_files:
                base = os.path.basename(file)
                bnfcode = os.path.splitext(base)[0]
                with open(file) as csv_file:
                    reader = csv.reader(csv_file)
                    header = next(reader, None)
                    for row in reader:
                        for i, h in enumerate(header):
                            if not row[i].isnumeric():
                                continue
                            try:
                                location = session.query(Location).filter(Location.gp_code == h).one()
                                bnf = session.query(BNFStem).filter(BNFStem.code_stem == bnfcode).one()
                                p = Prescription(date_span=datetime.strptime(row[0], "%Y-%m-%d"),
                                                 location=location, bnf_code=bnf, number_of_prescriptions=row[i])
                            except NoResultFound:
                                print(f"No results found for code:{h},bnf_code:{bnfcode}")
                            session.add(p)
                session.commit()
        except:
            import traceback
            traceback.print_exc()
            session.rollback()
        finally:
            session.close()

    def __repr__(self):
        return f"Perscriptions: {self.number_of_prescriptions} of {self.bnf_code} at {self.location} on {self.date_span}"
