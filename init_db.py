from nhs.models import Location, BNFStem, Prescription, CCG
from nhs import db

#
# print("loading")
# Location.load_from_csv(r"C:\Users\Robert\PycharmProjects\AiHack\raw_data\nhs_data\epraccur.csv")
# print("loaded locations")
# BNFStem.load_from_csv(r"C:\Users\Robert\PycharmProjects\AiHack\raw_data\nhs_data\BNF_stems.csv")
# print("loaded bnfs")
# Prescription.load_from_csv(r"C:\Users\Robert\PycharmProjects\AiHack\raw_data\nhs_data", "0403")
CCG.update()