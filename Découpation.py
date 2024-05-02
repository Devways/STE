import petl as etl
import pandas as pd


file_path = 'rog.xlsx'

df = pd.read_excel(file_path,sheet_name='projet',na_values=['-'])
df

indices=df.loc[:,'Subdivisions administratives du Royaume']

df=df.set_index(indices)
df=df.iloc[0:,1:]
df.fillna(0, inplace=True) 

df=df.apply(pd.to_numeric, errors='coerce')
population = df.loc[:, ['Population municipale', 'Ménage', 'Taille moyenne']]
type_de_longement = df.loc[:, ['Villa', 'Appartement', 'Maison marocaine', 'Habitat sommaire', 'Logement de type rural', 'Autre']]
statue_occupation = df.loc[:, ['Propriétaire', 'Locataire', 'Autre']]
anciennete_du_logement = df.loc[:, ['Moins de 10 ans', 'Entre 10 et 19 ans', 'Entre 20 et 49 ans', '50 ans et plus']]
equipements_de_base_du_logement=df.loc[:, ['Cuisine', 'W.-C.', 'Bain', 'Électricité', 'Eau courante']]
mode_evacuation_des_déchets  = df.loc[:, ['Bac à ordures de la commune', 'Camion commun ou privé', 'Autre']]
mode_de_cuisson = df.loc[:, ['Gaz', 'Électricité', 'Charbon', 'Bois', 'Déchets des animaux']]
autres_equipements = df.loc[:, ['Télévision', 'Radio', 'Téléphone portable', 'Téléphone fixe', 'Internet', 'Ordinateur', 'Parabole', 'Réfrigérateur']]

print(autres_equipements)
json_file_path = 'population_data.json'

# Export DataFrame to JSON file
# df.to_json(json_file_path, orient='index')