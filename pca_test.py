from nhs.models import Prescription
from nhs.models import Location
from datetime import datetime
from nhs import db


print("hello1")
# Reconfigure the prescription dataframe for ML
pres = db.session.query(Prescription).limit(10).all()
print("heyy")

#pres['month_time'] = ((pres['date_span'].year - 2015) * 12 )+ (pres['date_span'].month -1)
#pres['longitude'] =
#loc = Location.get_dataframe()  # Taking a very very long time to run
print("hello2")
print(pres)
print("hello3")
exit()
#gp_practices = pres['gp_code'].unique()
#gp_pr_use_040101 = pd.DataFrame(gp_practices, columns=['practice_code'])
#gp_pr_w_postcode = gp_pr_use_040101.merge(adresses, on='practice_code').dropna(axis=1)
#gp_pr_w_postcode['longitude'] = nomi.query_postal_code(list(gp_pr_w_postcode['postcode'])).longitude
#gp_pr_w_postcode['latitude'] = nomi.query_postal_code(list(gp_pr_w_postcode['postcode'])).latitude
# Train / test split ####################################################
    # How do we want to define this? Temporally?
from sklearn.model_selection import train_test_split
# Standardarise the values ####################################################
#from sklearn.preprocessing import StandardScaler
#scaler = StandardScaler()
#scaler.fit(history)
#scaled = scaler.transform(history)
# PCA   ####################################################
import numpy as np
#from sklearn.decomposition import PCA
#X = np.array(
#pca = PCA(n_components=2)
#pca.fit(X)
# Plot the out put of the PCA  ####################################################
#print(pca.explained_variance_ratio_)
#print(pca.singular_values_