from nhs.models import Prescription,BNFStem
from nhs.models import Location
from datetime import datetime
from nhs import db
import numpy as np
import pandas as pd
#pres = Prescription.query.join(BNFStem).filter(BNFStem.code_stem > 10000).all()

pres = Prescription.query.limit(100)
print(pres)
# prepped_data = pd.DataFrame()
prescription_df=pd.DataFrame()
for p in pres:
    prescription_df = prescription_df.append({
        "Time":p.date_span.year,
        "BNF":p.bnf_code.code_stem,
        "NT_GROUP":p.location.gp_ntgroup,
        "NUM_PRES":p.number_of_prescriptions
    },ignore_index=True)
print(prescription_df.head())
# #TIME
#print(prepped_data)
# 2) categoric to not categoric    #################################
prescription_df = pd.concat([prescription_df, pd.get_dummies(prescription_df['NT_GROUP'])], 1)  # One hot encoding
#df['ccg_code1'] = df.groupby('ccg_code').ngroup() # Turn a column into a numeric vector
#df.drop(["ccg_code", 'e8...'], axis=1, inplace = True) # Drop the categorical column
print(list(prescription_df.columns))  # Print a list fo the columns we now have
prescription_df.drop(["NT_GROUP"],axis = 1, inplace= True)
print(list(prescription_df.columns))
# 1) scale    #################################
from sklearn.preprocessing import StandardScaler

print(prescription_df["Time"])
print(prescription_df["BNF"])
sca = StandardScaler()
sca.fit(prescription_df)
scaled = sca.transform(prescription_df)

# # 3) sort out the outcome variable    #################################
#     # This will be a threshold level based on a proportion
#print(scaled)
print(len(scaled))
print(len(scaled[0]))
#outcome = #fake results

scaled  = np.append(scaled,np.random.randint(2, len(scaled)))

X = scaled[:-1]
y = scaled[-1]

# # 4) train and test split    #################################
from sklearn.model_selection import train_test_split
#X.to_numpy()
#y.to_numpy()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
# # 4.5) See what the most informative variables are   #################################
from sklearn.feature_selection import chi2, SelectKBest
sk = SelectKBest(chi2, k=5)
which_selected = sk.fit(X_train, y_train).get_support() #Returns the index of the selected columns
X.columns[which_selected]
# # 5) fit    #################################
from sklearn.linear_model import LogisticRegression
LogReg = LogisticRegression()
logregmodel = LogReg(random_state=42).fit(X_train, y_train)
# # 6) predict and assess   #################################
y_pred = logregmodel.predict(X_test)
logregmodel.score(y_pred, y_test)
logregmodel.get_params()
# Ext) Neural network for funsies because its 2AM and Imy wants to feel like Imy has made progress
from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1) # Using L2 norm regularisation
mlp.fit(X_train, y_train)
y_pred = mlp.predict(X_test)