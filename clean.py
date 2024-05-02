import petl as etl
import pandas as pd


file_path = 'rog.xlsx'

df = pd.read_excel(file_path,sheet_name='projet',na_values=['-'])
df.fillna(0, inplace=True) 

df = df[~df['Subdivisions administratives du Royaume'].str.startswith('Province:')]
df = df[~df['Subdivisions administratives du Royaume'].str.startswith('Eddakhla-Oued')]
cercle_data = {}
# Iterate over rows
def split_df_by_cercle(df, population_column):
    cercle_data = {}

    # Iterate over rows
    for index, row in df.iterrows():
        if row['Subdivisions administratives du Royaume'].startswith('Cercle :'):
            cercle_name = row['Subdivisions administratives du Royaume'].split(':')[1].strip()
            if cercle_name not in cercle_data:
                cercle_data[cercle_name] = {'Subdivisions administratives du Royaume': [], population_column: []}

        cercle_data[cercle_name]['Subdivisions administratives du Royaume'].append(row['Subdivisions administratives du Royaume'])
        cercle_data[cercle_name][population_column].append(row[population_column])

    cercle_dfs = {}
    for cercle_name, data in cercle_data.items():
        cercle_dfs[cercle_name] = pd.DataFrame(data)

    return cercle_dfs
cercle_dfs = split_df_by_cercle(df, 'Population légale')

for cercle, df in cercle_dfs.items():
    df.to_json(f'pupulation_{cercle}.json', orient='records')

# Export DataFrame to JSON file
# df.to_json(json_file_path, orient='index')