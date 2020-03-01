from nhs.models import Prescription
from nhs.models import Location
from datetime import datetime
from nhs import db
import pandas as pd

pres = Prescription.get_dataframe()
prepped_data = pd.DataFrame()

#TIME
prepped_data["Time"] = pres['date_span'].year
#BNF CODE
prepped_data["BNF"] = pres.bnf_stems['code_stem']
#gp_ntgroup
prepped_data["NT_GROUP"] = pres.locations['gp_ntgroup']
#gp_ons_code
prepped_data["ONS_CODE"] = pres.locations['gp_ons_code']
#number of prespcriptions
prepped_data["NUM_PRESCIPTION"] = pres['number_of_prescriptions']


#Prescription.query.filter(Prescription.location.has(gp_code=code))