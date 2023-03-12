#Sumar valores en forma no óptima
def suma(lista):
  sumados = 0
  for num in lista:
    sumados = sumados + num
  return sumados

resultado = suma([5,10,15])
print(f'La suma es {resultado}')

#Forma óptima de sumar valores, con el argumento *args
def suma_total(numeros):
  return sum(*numeros)

resultados = suma_total([5,10,15])
print(resultados)

#Sumar utilizando el operador * como argumento (*args)
def suma2(nombre,*numeros):
  return nombre,sum(numeros)

nombre, numeros = suma2('Jessica', 5,10,15)
print(f'{nombre} El resultado de la suma 2 es: {numeros}')



