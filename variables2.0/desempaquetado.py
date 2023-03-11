#Creando una tupla
datos_en_tupla = ('Jessica', 'Martinez', 35)
datos_en_lista = ['Jessica', 'Martinez', 35]
datos_en_set = {'Jessica', 'Martinez', 35}

#Desempaquetado de datos, la cantidad de variables debe ser igual a la cantidad de elementos de la tupla, se puede utilizar con tuplas, listas 
nombre, apellido, edad = datos_en_tupla
nombre_lista, apellido_lista, edad_lista = datos_en_lista

#En conjuntos (set) no permite desempaquetar números
nombre_set, apellido_set, edad_set = datos_en_set

print(edad_set)