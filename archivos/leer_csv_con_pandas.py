import pandas as pd

#Usar la función read_csv para leer el archivo csv
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

#Obtener los datos de la columna nombre
nombre = df["nombre"]

#Ordenar por edad 
df_ordenado_ascendente = df.sort_values("edad")

#Ordenar de forma descendente
df_ordenado_descendente = df.sort_values("edad", ascending=False)
#print(df.columns.tolist())

#Slicing
cadena = "0123456789"
#print(cadena[2:7]) #imprime del 2 al 6

#Concatenando los dos dataframes
df_concatenado = pd.concat([df,df2])
#print(df_concatenado)

#Accediendo a las primeras 3 filas con head()
primera_fila = df.head(3)
#print(primera_fila)

#Accediendo a las ultimas 3 filas con Tail()
ultimas_filas = df.tail(3)
#print(ultimas_filas)

#Acceder a la cantidad de filas y columnas con shape
filas,columnas = df.shape

#Obtener data estadística del dataframe, toma columna numerica arroja datos de cantidad, media, min, max, etc
df_info = df.describe()
#print(df_info)

#Acceder a un elemento especifico del df con loc (fila, columna)
elemento_especifico_loc =df.loc[2,"edad"]
#print(elemento_especifico_loc)

#Acceder al mismo elemento especifico del df con iloc (por índice)
elemento_especifico_iloc = df.iloc[2,2]
#print(elemento_especifico_iloc)

#Acceder a todos los apellidos con loc
apellidos_loc = df.loc[:,"apellido"]
#print(apellidos_loc)

#Acceder a todos los apellidos con iloc
apellidos_iloc = df.iloc[:,1]
#print(apellidos_iloc)

#Acceder a la fila 3 con loc
fila_3 = df.loc[2,:]
#print(fila_3)

#Acceder a la fila 3 con iloc
fila_3_iloc = df.loc[2,:]
#print(fila_3_iloc)

#Acceder a filas con edad mayor que 30 (condicional)
mayor_que_30 = df.loc[df["edad"]>30,:]

print(mayor_que_30)


