cadena1 = "Mi nombre es jessica no" #"Mi nombre es jessica"
cadena2 = "Soy desarrolladora web"

#print(dir(cadena1)) -> dir permite ver la lista de atributos válidos del objeto pasado, es una función

#convierte a mayusculas
mayusc = cadena1.upper()

#convierte a minusculas
minusc = cadena1.lower()

#primera letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

#buscar una cadena en otra cadena, si no encuentra coincidencia, devuelve -1
busqueda_find = cadena1.find('juana')

#buscar cadena en otra cadena, si no encuentra coincidencia, lanza una excepción
#busqueda_index = cadena1.index('9')

#si es numerico devuelve True, si no devuelve False
es_numerico = cadena1.isnumeric()

#si es alfa-numerico devuelve True, si no devuelve False
es_alfanumerico = cadena1.isalpha()

#Cuenta coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencia = cadena1.count("no")

#Cuenta cuantos caracteres tiene una cadena, es una función
contar_caracteres = len(cadena1)

#Verificar si una cadena empieza con otra cadena dad, si es así, devuelve True
empieza_con = cadena1.startswith('Mi')

#Verificar si una cadena termina con otra cadena dad, si es así, devuelve True
termina_con = cadena1.endswith('no')

#reemplaza un pedazo de la cadena dada,por otra cadena
cadena_nueva= cadena1.replace('Je', "je")

#Separa cadena con la cadena que se le pase
separa_cadena = cadena1.split(' ')


#resultado = dir(cadena1)

print(separa_cadena[1])