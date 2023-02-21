import pandas as pd
import numpy as np
import re

data = pd.read_csv('operations.csv')


# pour afficher uniquement les variables qui ont des valeurs manquantes
nb_na = data.isnull().sum()
print(nb_na[nb_na>0])
print(data.loc[data['montant'].isnull(),:])
print(data.loc[data['montant'].isnull(),:])
# on stocke le df des valeurs manquantes dans un nouveau df
data_na = data.loc[data['montant'].isnull(),:]

# pour chaque ligne de mon df, on récupère les index (qui ne changent pas au travers du .loc)
for index in data_na.index:
    # calcul du montant à partir des soldes précédents et actuels

    data.loc[data['libelle'] == 'PRELEVEMENT XX TELEPHONE XX XX', :]
    data.loc[data['categ'].isnull(), 'categ'] = 'FACTURE TELEPHONE'
    data.loc[index, 'montant'] = data.loc[index+1, 'solde_avt_ope'] - data.loc[index, 'solde_avt_ope']
    
    data.drop_duplicates(subset=['date_operation', 'libelle', 'montant', 'solde_avt_ope'], inplace=True, ignore_index=True)
    
data.to_csv('operation.csv', index=False)