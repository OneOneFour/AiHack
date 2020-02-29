
from nhs import Session
from nhs.models import Prescription
import numpy as np
import pandas as pd
import pandas as pd
import numpy as np
#from plotnine import *
import matplotlib.pyplot as plt
import seaborn as sns

pres = Prescription.get_dataframe()
print(pres.head())

pres['bnf_code_id'].to_string()
fours = pres[pres['bnf_code_id'].str.startswith('4')]
print(fours.head())

#fours =  # find the number of prescriptions beginning with a 4 for each time period


#fours['dep_per_person'] = #sum of all per gp / total number of predications

# select colour scheme for the plot
#cmap = sns.diverging_palette(15, 220, as_cmap=True, center="light", s = 99)
#plot time period on the x axis, sum of depression predictions on the y axis
#sns.scatterplot(x=pres['date_span'], y=pres['number_of_prescriptions'], palette="Blues")
#plt.show()


# Select all the ones that begine witha four in a column







