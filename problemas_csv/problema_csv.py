#Cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("problemas_csv\\datos.csv")

#convertir a string los datos de una columna
df["edad"] = df["edad"].astype(str)

#Mostrar el tipo de datos del primer elemento de la columna edad
print(type(df["edad"][0]))


#Reemplazar el nombre "Jessica" por "Paola" con replace
df["nombre"].replace("Jessica","Paola",inplace=True)
#print(df["nombre"])

#Elimina las filas con datos faltantes, para eliminar las columnas se pasa como parámetro axis=1
df = df.dropna()
#print(df)

#Elimina filas repetidas
df = df.drop_duplicates()
#print(df)

#Crear un csv con el df resultante (limpio)
df.to_csv("problemas_csv\\datos_limpios.csv") 
