
# 1) scale    #################################
from sklearn.preprocessing import StandardScaler
sca = StandardScaler()
sca.fit(df)
scaled = sca.transform(df)

# 2) categoric to not categoric    #################################
X_hot = pd.concat([df, pd.get_dummies(df['CATEGORICALCOLUMN'])], 1)  # One hot encoding
df['ccg_code1'] = df.groupby('ccg_code').ngroup() # Turn a column into a numeric vector
df.drop(["ccg_code", 'e8...'], axis=1, inplace = True) # Drop the categorical column
print(list(df.columns))  # Print a list fo the columns we now have

# 3) sort out the outcome variable    #################################
    # This will be a threshold level based on a proportion

X = df[,0:x]
y = df[,-1]

# 4) train and test split    #################################
from sklearn.model_selection import train_test_split as tts
import numpy as np
df.to_numpy()
X_train, X_test, y_train, y_test = tts(X, y, test_size=0.33, random_state=42)

# 4.5) See what the most informative variables are   #################################
from sklearn.feature_selection import chi2, SelectKBest
sk = SelectKBest(chi2, k=20)
which_selected = sk.fit(X_train, y_train).get_support() #Returns the index of the selected columns
X.columns[which_selected]

# 5) fit    #################################
from sklearn.linear_model import LogisticRegression
LogReg = LogisticRegression()
logregmodel = LogReg(random_state=42).fit(X_train, y_train)

# 6) predict and assess   #################################
y_pred = logregmodel.predict(y_test)
logregmodel.score(y_pred, y_test)
logregmodel.get_params()

# Ext) Neural network for funsies because its 2AM and Imy wants to feel like Imy has made progress
from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1) # Using L2 norm regularisation
mlp.fit(X_train, y_train)
y_pred = mlp.predict(X_test)




