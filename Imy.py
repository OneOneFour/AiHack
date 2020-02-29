from nhs import Session
from nhs.models import Prescription
import numpy as np
import pandas as pd

import pandas as pd
import numpy as np
#from plotnine import *

pres = Prescription.get_dataframe()
print(pres.head())

# find the number of prescriptions beginning with a 4 for each time period

# set figure margins
plt.figure(figsize=(16, 6))
# select colour scheme for the plot
cmap = sns.diverging_palette(15, 220, as_cmap=True, center="light", s = 99)
#plot time period on the x axis, sum of depression predictions on the y axis
sns.boxplot(y=pres['number_of_patients'], x=small["high_level_health_geography1"], palette="Blues")
