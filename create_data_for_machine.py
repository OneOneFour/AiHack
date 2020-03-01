from nhs.models import Prescription
from nhs.models import Location
from datetime import datetime
from nhs import db
import pandas as pd

pres = Prescription.query.limit(100).all()
#Patient.query.filter(Patient.mother.has(phenoscore=10))
#Prescription.get_dataframe()
#print(len(pres))
#exit()
prepped_data = pd.DataFrame()
for p in pres:
    prepped_data = prepped_data.append({
        "Time":p.date_span.year,
        "BNF":p.bnf_code,
        "NT_GROUP":p.location.gp_ntgroup,
        "NUM_PRESCRIPTION":p.number_of_prescriptions
    },ignore_index=True)

#TIME
print(prepped_data.head())


#Prescription.query.filter(Prescription.location.has(gp_code=code))