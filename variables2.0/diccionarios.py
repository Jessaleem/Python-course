#Crear diccionario con dict()
diccionario = dict(nombre="Jessica", apellido='Martinez')

#Las listas no pueden ser llaves, las tuplas si pueden ser llaves, conjuntos pueden ser llaves (con frozenset)
diccionario= {("nombre","apellido"):'jessica'}
diccionario = {frozenset(['nombre','apellido']): 'jessica'}

#crear diccionarios con fromkeys() valores indefinidos, primer parametro es iterable valor por defecto: none
diccionario = dict.fromkeys(["nombre", "apellido", "edad"])

#crear diccionarios con fromkeys() cambiando el valor por defecto a "jessica" con el segundo parametro
diccionario = dict.fromkeys(["nombre", "apellido"], "jessica")

print(diccionario)
