from nhs.models import Prescription
pres = Prescription.get_dataframe()
pres['month_time'] = ((pres['date_span'].year() - 2015) * 12 )+ (pres['date_span'].month() -1)
pres['longitude'] =

nomi = pgeocode.Nominatim('gb')
gp_practices = pres['gp_code'].unique()

#gp_pr_use_040101 = pd.DataFrame(gp_practices, columns=['practice_code'])
gp_pr_w_postcode = gp_pr_use_040101.merge(adresses, on='practice_code').dropna(axis=1)

gp_pr_w_postcode['longitude'] = nomi.query_postal_code(list(gp_pr_w_postcode['postcode'])).longitude
gp_pr_w_postcode['latitude'] = nomi.query_postal_code(list(gp_pr_w_postcode['postcode'])).latitude



# Train / test split
    # How do we want to define this? Temporally?



# Standardarise the values

    # Time = # months since the start


# PCA
fit(self, X, y=None)[source]¶
transform(self, X)


# Plot the out put of the PCA




# Select the features


