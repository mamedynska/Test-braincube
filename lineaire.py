import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


# Charger le .csv
filepath = "data/depensesNormalized.csv"
df = pd.read_csv(filepath)

print("Setup Complete")

# Charger le .csv
filepath = "data/depensesNormalized.csv"
df = pd.read_csv(filepath)
print("Setup Complete")


# Prédiction juste avec le salaire :
X = df[["salaire"]]
y =  df["depenses"]
regSal = LinearRegression().fit(X,y)

regSal.score(X, y)
pred=regSal.predict(X)
dfResultat = pd.DataFrame({"salaire":X["salaire"],"depenses":y, "Depenses Preditent":pred})
print(dfResultat)
print("Coef : ", regSal.coef_)
print("Intercept : ", regSal.intercept_)
print("Score : ",regSal.score(X, y))
# Coef :  [0.67845169]
# Intercept :  3.487717762891342e-16
# Score :  0.46029670093656905

# Ecriture dans prediction1.csv
dfResultat.to_csv("data/prediction_1.csv",index=False)


# Prédiction avec le salaire et l'age
X2 = df[["salaire","age"]]
y2 =  df["depenses"]
regSalAge = LinearRegression().fit(X2,y2)
print("Coef : ", regSalAge.coef_)
print("Intercept : ", regSalAge.intercept_)
print("Score : ",regSalAge.score(X2, y2))
pred2=regSalAge.predict(X2)
dfResultat2 = pd.DataFrame({"salaire":X2["salaire"], "age":X2["age"],"depenses":y2, "Depenses Preditent":pred2})
print(dfResultat2)
# Coef :  [0.67519274 0.1395618 ]
# Intercept :  3.724175540664552e-16
# Score :  0.4797635759377238

# Ecriture dans prediction2_depense.csv
dfResultat2.to_csv("data/prediction2_depense.csv",index=False)