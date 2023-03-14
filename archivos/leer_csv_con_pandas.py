import pandas as pd

#Usar la función read_csv para leer el archivo csv
df = pd.read_csv("archivos\\datos.csv")

#Obtener los datos de la columna nombre
nombres = df["nombre"]

#Ordenar por edad 
#df_ordenado = df.sort_values("edad")
print(df)