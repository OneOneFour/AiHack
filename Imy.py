from nhs import Session
from nhs.models import Prescription
import numpy as np
import pandas as pd
import pandas as pd
import numpy as np
#from plotnine import *
import matplotlib.pyplot as plt
import seaborn as sns

# Formatting the pres data
pres = Prescription.get_dataframe()
pres['bnf_code_id'].to_string()
pres['dep_per_total'] = (sum(pres[pres['bnf_code_id'].str.startswith('4')])) - sum[pres[pres['bns_code_id']]]

sns.scatterplot(x=pres['date_span'], y=pres['number_of_prescriptions'], palette="Blues")
plt.show() # plot time period on the x axis, sum of depression predictions on the y axis

### FOURS
# Creating the fours dataset
fours = pres[pres['bnf_code_id'].str.startswith('4')]
fours.shape  # find the number of prescriptions beginning with a 4 for each time period

#fours['dep_per_person'] = #sum of all per gp / total number of predications

# Plot the graph for just anti-depressants
sns.scatterplot(x=fours['date_span'], y=fours['number_of_prescriptions'], palette="Blues")
plt.show() # plot same graph but just for the fours









