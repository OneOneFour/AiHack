from nhs import Session
from nhs.models import Location,Prescription
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pres = Prescription.get_dataframe()

pres["bnf_code_id"] = pres["bnf_code_id"].astype(str)

#sesh = Session()
#print(sesh.query(Prescription).first())
#print(sesh.query(Prescription).filter(Prescription.bnf_code_id.like("0403")))
prescriptions_by_time_start = pres.filter(Prescription.bnf_code_id.like("0403"), pres.date_span <= datetime.datetime(2015, 3, 1) )
prescriptions_by_time_end = pres.filter(Prescription.bnf_code_id.like("0403"), pres.date_span <= datetime.datetime(2018, 3, 1),pres.date_span >= datetime.datetime(2018, 1, 1) )

prescriptions_start_location = set(prescriptions_by_time_start.location_id)
prescriptions_end_location = set(prescriptions_by_time_end.location_id)
change_data  = []

for i in prescriptions_start_location:
    location_specfic = prescriptions_by_time_start.filter(location_id = i)
    prescriptions_start_num_sum = np.sum(np.asarray(location_specfic.number_of_prescriptions))/3
    prescriptions_end_num_sum = np.sum(np.asarray(location_specfic.number_of_prescriptions))/3
    change_data.append(prescriptions_end_num_sum - prescriptions_start_num_sum)

results_df = pd.DataFrame([prescriptions_start_location,change_data], columns = ['location_id', 'Change'])
results_df.sort_values(by=['Change'])

data_plot = results_df.head(n)

plt.figure()
plt.plot( np.asarray(data_plot['location_id']) , np.asarray(data_plot['Change']) )
plt.show()