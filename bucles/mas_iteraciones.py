#Creando las listas
frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]
cadena = "hola Jess"
numeros = [2, 5, 8, 10]

#Evitar que se incluya un elemento con la sentencia "continue"
for fruta in frutas:
  if fruta == 'granada':
    continue
  print(f'Me voy a comer una {fruta}')

#Evitar que el bucle siga ejecutandose con "break"
for fruta in frutas:
  print(f'Me voy a comer una {fruta}')
  if fruta == "pera":
    break
print('bucle terminado')


#Iterar una cadena de texto
for letra in cadena:
  print(letra)

#For para duplicar los numeros
numeros_duplicados = list()
for numero in numeros:
  numeros_duplicados.append(numero*2)
print(numeros_duplicados)

#For en una sola línea de código
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)