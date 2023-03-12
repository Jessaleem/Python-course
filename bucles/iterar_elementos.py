#for in

animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [2, 10, 32, 72]

#recorrer la lista animales
for animal in animales:
  print(f'Ahora la variables animal es igual a: {animal}')
  
#Recorrer la lista numerps y multiplicando cada valor por 10
for num in numeros:
  print(f'Los números multiplicados por 10 son: {num*10}')
  
#Recorrer dos listas al mismo tiempo con zip()
for numero,animal in zip(numeros, animales):
  print(f'Recorriendo lista 2: {numero}')
  print(f'Recorriendo lista 1: {animal}')
  
#Iterar con range()
for num in range(10,20):
  print(num)

#Forma no optima de recorrer una lista con su índice (No funciona en CONJUNTOS)
for num in range(len(numeros)):
  print(numeros[num])

#Forma correcta de recorrer una lista con su índice / devuelve una tupla
for num in enumerate(numeros):
  print(num)

#Accediendo al valor del índice y del valor
for num in enumerate(numeros):
  indice = num[0]
  valor = num[1]
  print(f'El índice es: {indice} y el valor es: {valor}')

#Usando el for/else
for num in numeros:
  print(f'Ejecutando el último bucle, valor actual: {num}')
else:
  print('El bucle terminó')

#Todo lo anterior funciona para Listas, Tuplas y Conjuntos

