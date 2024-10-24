import pandas as pd
import json

# Charger les fichiers CSV
df1 = pd.read_csv('/home/grami/tp_nouvelle_bases/piple_line_project/test.csv')
df2 = pd.read_csv('/home/grami/tp_nouvelle_bases/piple_line_project/test1.csv')

# Supposons que les fichiers CSV ont les colonnes 'Prenom' et 'Nom'
# Créer une nouvelle colonne 'Prenom Nom' pour la jointure
df1['Prenom Nom'] = df1['Prenom'] + ' ' + df1['Nom']
df2['Prenom Nom'] = df2['Prenom'] + ' ' + df2['Nom']

# Effectuer la jointure
jointure_df = pd.merge(df1, df2, on='Prenom Nom', how='inner')  # Vous pouvez utiliser 'outer', 'left', ou 'right' selon vos besoins

# Convertir le DataFrame joint en JSON
resultat_json = jointure_df.to_json(orient='records')

# Sauvegarder le résultat en fichier JSON
with open('jointure_result.json', 'w') as json_file:
    json.dump(json.loads(resultat_json), json_file, indent=4)

print("La jointure a été effectuée et le résultat est enregistré dans 'jointure_result.json'.")
