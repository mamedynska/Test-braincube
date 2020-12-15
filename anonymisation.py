import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print("Setup Complete")

# Charger le .csv
filepath = "data/depenses.csv"
df = pd.read_csv(filepath)


# Sauvegarde
dfSaveNom = pd.DataFrame({"nom" : saveNom})
dfSaveVille = pd.DataFrame({"ville" : saveVille})

# Hashage
df["nom"] = df[["nom"]].sum(axis=1).map(hash)
df["ville"] = df[["ville"]].sum(axis=1).map(hash)

# On sauvegarde le nom non-hashé de la ville et du client.
saveNom = df.nom.unique()
saveVille = df.ville.unique()


dfSaveNom['idName'] = dfSaveNom[['nom']].sum(axis=1).map(hash)
dfSaveVille["idVille"] = dfSaveVille[["ville"]].sum(axis=1).map(hash)

def centrer_reduire(col):
    col = (col - col.mean())/col.std()
    return col

# On centre-réduit les colonnes
df.depenses=centrer_reduire(df.depenses)
df.salaire = centrer_reduire(df.salaire)
df.age = centrer_reduire(df.age)


if __name__ == "__main__":
    print("Hello")