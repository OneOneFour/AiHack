from nhs.models import Location, BNFStem,Prescription
from nhs import Base,engine
Base.metadata.create_all(engine)
print("loading")
#Location.load_from_csv(r"C:\Users\Robert\PycharmProjects\AiHack\raw_data\nhs_data\epraccur.csv")
print("loaded locations")
#.load_from_csv(r"C:\Users\Robert\PycharmProjects\AiHack\raw_data\nhs_data\BNF_stems.csv")
print("loaded bnfs")
Prescription.load_from_csv(r"C:\Users\Robert\PycharmProjects\AiHack\raw_data\nhs_data","04")