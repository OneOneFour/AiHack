from nhs import Session
from nhs.models import Prescription
import pandas
import numpy as np
from plotnine import *
import matplotlib.pyplot as plt
import seaborn as sns
print("hello")
# Formatting the pres data
pres = Prescription.get_dataframe()
#print(pres.head())
#pres['bnf_code_id'].to_string()

#(ggplot(pres, aes(x=pres['date_span'], y=pres['number_of_prescriptions']))) + geom_point()

#sns.scatterplot(x=pres['date_span'], y=pres['number_of_prescriptions'], palette="Blues")
#plt.show()   # plot time period on the x axis, sum of depression predictions on the y axis

### FOURS
# Creating the fours dataset
#fours = pres[pres['bnf_code_id'].str.startswith('4')]
#print(fours.shape)  # find the number of prescriptions beginning with a 4 for each time period

### FOR JUST ANTI-DEPRESSANTS
# Plot the graph for just anti-depressants
#sns.scatterplot(x=fours['date_span'], y=fours['number_of_prescriptions'], palette="Blues")
#plt.show()   # plot same graph but just for the fours

### Plotting per total number of prescriptions

# Group by the date
time = pres.groupby(['date_span'])['number_of_prescriptions'].sum()
time.columns = ['date_span', 'total_prescriptions']
print(time.head())
sns.scatterplot(x=time['date_span'], y=time['total_prescriptions'], palette="Blues")
plt.show()

#sns.scatterplot(x=time['bnf_code_id'], y=time['bnf_code_id'], palette="Blues")
#plt.show()
