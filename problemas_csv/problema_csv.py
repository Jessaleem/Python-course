#Cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("problemas_csv\\datos.csv")

#convertir a string los datos de una columna
df["edad"] = df["edad"].astype(str)

#Mostrar el tipo de datos del primer elemento de la columna edad
print(type(df["edad"][0]))
