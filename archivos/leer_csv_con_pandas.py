import pandas as pd

#Usar la función read_csv para leer el archivo csv
df = pd.read_csv("archivos\\datos.csv")

#Obtener los datos de la columna nombre
nombre = df["nombre"]

#Ordenar por edad 
df_ordenado_ascendente = df.sort_values("edad")

#Ordenar de forma descendente
df_ordenado_descendente = df.sort_values("edad", ascending=False)
print(df.columns.tolist())