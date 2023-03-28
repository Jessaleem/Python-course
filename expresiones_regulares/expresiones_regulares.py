import re

texto = '''Hola maestro. esta es la cadena 1. como estas 
Esta es la linea abababbbb253 de ababababbbb texto
Y esta es la final (linea 3) definitiva'''

#Se puede utilizar search, findall con un tercer parámetro "flags=re.IGNORECASE para no tener en cuenta mayúsculas"
#resultado = re.findall("esta", texto)

#\d -> busca digitos numericos del 0 - 9
#resultado = re.findall(r"\d",texto)

#\D -> busca TODO MENOS digitos numericos del 0 - 9
#resultado = re.findall(r"\D",texto)

#\w -> busca caracteres alfanumericos [a-z A-Z 0-9 _]
#resultado = re.findall(r"\w",texto)

#\w -> busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9 _]
#resultado = re.findall(r"\W",texto)

#\s -> busca espacios en blanco -> espacios, tabs, saltos de linea
#resultado = re.findall(r"\s",texto)

#\S -> busca TODO MENOS espacios en blanco -> espacios, tabs, saltos de linea
#resultado = re.findall(r"\S",texto)

# . -> busca TODO MENOS saltos en linea
#resultado = re.findall(r".",texto)

#\n -> busca saltos en linea
#resultado = re.findall(r"\n",texto)

#\ -> Cancela caracteres especiales, cancela la función del punto (linea 25) y busca puntos
#resultado = re.findall(r"\.",texto)

#Armar una cadena que busque un numero, seguido de un punto y un espacio
#resultado = re.findall(r"\d\.\s",texto)

#Buscar el principio de una línea 
#^ -> Busca el comienzo de una línea
#flags=re.M activa la multilinea
#resultado = re.findall(r"^Esta",texto,flags=re.M)

#$ -> Buscar el final de una línea 
#resultado = re.findall(r"definitiva$",texto)

#{n} -> Busca n cantidad de veces el valor de la izquierda (3 números juntos)
#resultado = re.findall(r'\d{3}\s',texto)

#{n,m} -> al menos n, como máximo m
#resultado = re.findall(r'\d{1,4}',texto)

#{n,m} -> al menos n, como máximo m. Se utiliza () ó [] para especificar conjuntos y otras características en lo que se quiere buscar
#resultado = re.findall(r'(ab){1,4}',texto)

# | -> busca una cosa o la otra, condición OR
resultado = re.findall(r'\d{2,4}|Hola',texto)



print(resultado)
