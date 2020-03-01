#from nhs import Session
from nhs.models import Location,Prescription
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

num_months = 3
pres = Prescription.get_dataframe()
print(len(pres))
#print(pres['bnf_code_id'].head(10))
print(pres['bnf_code_id'])
pres['bnf_code_id'] = pres['bnf_code_id'].astype(str)
print(pres['bnf_code_id'])
four_three = pres.loc[pres['bnf_code_id'] == '403']
print(len(four_three))
prescriptions_by_time_start = four_three.loc[four_three["date_span"] < datetime.datetime(2015, 4, 1)]
print(len(prescriptions_by_time_start))
#NEED TO FIX LIE BELOW
prescriptions_by_time_end = four_three.loc[(four_three["date_span"] >= datetime.datetime(2017, 1, 1)) and (four_three["date_span"] < datetime.datetime(2017, 4, 1))]
#prescriptions_by_time_end = four_three[(four_three["date_span"] >= datetime.datetime(2017, 1, 1)) and (four_three["date_span"] < datetime.datetime(2017, 4, 1))]
print(len(prescriptions_by_time_start))

prescriptions_start_location = prescriptions_by_time_start["location_id"].unique()
print(len(prescriptions_start_location))
print(prescriptions_start_location)
prescriptions_end_location = prescriptions_by_time_end["location_id"].unique()
print(len(prescriptions_end_location))
change_data  = []

for i in prescriptions_start_location:
    location_specfic = prescriptions_by_time_start["location_id"][i]
    prescriptions_start_num_sum = np.sum(np.asarray(location_specfic["number_of_prescriptions"]))/num_months
    prescriptions_end_num_sum = np.sum(np.asarray(location_specfic["number_of_prescriptions"]))/num_months
    change_data.append(prescriptions_end_num_sum - prescriptions_start_num_sum)

results_df = pd.DataFrame([prescriptions_start_location,change_data], columns = ['location_id', 'Change'])
results_df.sort_values(by=['Change'])

data_plot = results_df.head(10)

plt.figure()
plt.plot(np.asarray(data_plot['location_id']) , np.asarray(data_plot['Change']))
plt.show()