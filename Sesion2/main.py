# Importar libreria Pandas
import pandas as pd
# Define la ruta del archivo CSV que contiene los datos
# Si el archivo esta en el mismo directorio, basta poner el nombre del archivo
path = 'Sesion2/classic_rock_playlist.csv'
ClassicRock = pd.read_csv(path, encoding='latin1')
print(type(ClassicRock))
print(ClassicRock.head())