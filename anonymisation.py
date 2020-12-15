import numpy as np
import pandas as pd

print("Setup Complete")

# Charger le .csv
filepath = "data/depenses.csv"
df = pd.read_csv(filepath)


# On sauvegarde le nom non-hashé de la ville et du client.
saveNom = df.nom.unique()
saveVille = df.ville.unique()

# Sauvegarde
dfSaveNom = pd.DataFrame({"nom" : saveNom})
dfSaveVille = pd.DataFrame({"ville" : saveVille})

# Hashage
df["nom"] = df["nom"].map(hash)
df["ville"] = df["ville"].map(hash)



dfSaveNom['idName'] = dfSaveNom[['nom']].sum(axis=1).map(hash)
dfSaveVille["idVille"] = dfSaveVille[["ville"]].sum(axis=1).map(hash)

def centrer_reduire(col):
    col = (col - col.mean())/col.std()
    return col

# On centre-réduit les colonnes
df.depenses=centrer_reduire(df.depenses)
df.salaire = centrer_reduire(df.salaire)
df.age = centrer_reduire(df.age)

# Ecriture dans depensesNormalized.csv
df.to_csv("data/depensesNormalized.csv",index=False)
