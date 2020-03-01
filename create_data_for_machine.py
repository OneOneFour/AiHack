from nhs.models import Prescription,BNFStem
from nhs.models import Location
from datetime import datetime
from nhs import db
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pres = Prescription.query.all()
#pres = Prescription.query.join(BNFStem).filter(BNFStem.code_stem >= 40000).filter(BNFStem.code_stem < 50000)
prescription_df=pd.DataFrame()
for p in pres:
    try:
        total_number = p.location.total_number
        a = {
        "Time":p.date_span.year,
        "BNF":p.bnf_code.code_stem,
        "NT_GROUP":p.location.gp_ntgroup,
        "NUM_PRES":p.number_of_prescriptions,
        "PEOPLE":total_number
        #"CCG":p.gp_surgeries.ccg_code,
        }
    except:
        continue
    prescription_df = prescription_df.append(a,ignore_index=True)
prescription_df["DRUG_PROP"] = ""
NT_GROUP_list = prescription_df["NT_GROUP"].unique()
for i in NT_GROUP_list:
    given_NT_GROUP = prescription_df[prescription_df["NT_GROUP"] == i]    #df.loc[(df["B"] > 50) & (df["C"] == 900), "A"]
    given_NT_GROUP_and_0403 = given_NT_GROUP.loc[(given_NT_GROUP["BNF"] > 40300) & (given_NT_GROUP["BNF"] < 40305)]
    sum_0403 = given_NT_GROUP_and_0403["NUM_PRES"].sum()
    sum_all = given_NT_GROUP["NUM_PRES"].sum()
    print(sum_0403,sum_all)
    ratio_region = sum_0403/sum_all
    prescription_df.loc[prescription_df["NT_GROUP"] == i, 'DRUG_PROP'] = ratio_region

# #TIME
#print(prepped_data)
# 2) categoric to not categoric    #################################
prescription_df = pd.concat([prescription_df, pd.get_dummies(prescription_df['NT_GROUP'])], 1)  # One hot encoding
#df['ccg_code1'] = df.groupby('ccg_code').ngroup() # Turn a column into a numeric vector
#df.drop(["ccg_code", 'e8...'], axis=1, inplace = True) # Drop the categorical column
#print(list(prescription_df.columns))  # Print a list fo the columns we now have
prescription_df.drop(["NT_GROUP"],axis = 1, inplace= True)
#print(prescription_df.info)
#print(list(prescription_df.columns))

# 1) scale    #################################
#print(prescription_df.shape)
#sca.fit(prescription_df)
#scaled = sca.transform(prescription_df)
#print(scaled.shape)

# # 3) sort out the outcome variable    #################################
#     # This will be a threshold level based on a proportion
#print(scaled)
#outcome = #fake results

#print(prescription_arr.shape)
# a = len(prescription_arr)
# extra = np.random.randint(2,size=a)

#prescription_arr = np.transpose(prescription_arr)
#print("hey")
#print(prescription_arr.shape)

#np.append(prescription_arr, extra)
#print(prescription_arr.shape)
#prescription_arr = np.transpose(prescription_arr)
#print(prescription_arr.shape)

X = np.asarray(prescription_df.iloc[:,:-1])
y = np.asarray(prescription_df.iloc[:,-1])
#
print(X.shape,y.shape)
print(X)
print(y)

prescription_arr = np.asarray(prescription_df)

# # 4) train and test split    #################################
from sklearn.model_selection import train_test_split
#X.to_numpy()
#y.to_numpy()
#print(X.shape,y.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
from sklearn.preprocessing import StandardScaler
sca = StandardScaler()
sca.fit_transform(X_train)
sca.transform(X_test)

# # 4.5) See what the most informative variables are   #################################
from sklearn.feature_selection import chi2, SelectKBest
sk = SelectKBest(chi2, k=5)
which_selected = sk.fit(X_train, y_train).get_support() #Returns the index of the selected columns
#print(which_selected)
#attemp_X_Best = X[which_selected]
# # 5) fit    #################################
from sklearn.linear_model import LogisticRegression
#LogReg = LogisticRegression()
logregmodel = LogisticRegression(random_state=42).fit(X_train, y_train)
# # 6) predict and assess   #################################
y_pred = logregmodel.predict(X_test)
#logregmodel.score(y_pred, y_test)
print(logregmodel.get_params())
print(X_test.shape,y_test.shape,X_train.shape,y_pred.shape)
plt.figure()
plt.scatter(y_test,y_pred)
# plt.figure()
# plt.plot(np.sort(X_train,axis=0),y_pred)
plt.show()

# Ext) Neural network for funsies because its 2AM and Imy wants to feel like Imy has made progress
from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1) # Using L2 norm regularisation
mlp.fit(X_train, y_train)
y_pred = mlp.predict(X_test)