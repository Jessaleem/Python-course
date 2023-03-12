numeros = [1,2,3,4,5,6,7,8,9]

#lambda crea funciones ánonimas que luego se pueden asignar a variables
multiplicar_por_dos = lambda x : x * 2

#Crear función que dice si es par o no
def es_par(num):
  if(num%2==0):
    return True

#Usar filter con una función común
numeros_pares = filter(es_par, numeros)

#Creando función de números pares con lambda
numeros_pares2 = filter(lambda numero : numero%2 == 0, numeros)

print(list(numeros_pares2))