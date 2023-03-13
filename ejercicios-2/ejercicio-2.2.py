#Crear una función que devuelva los números primos entre 0 y un argumento que se pase

#Función que verifica que un numero es primo
def es_primo(num):
  #Se verifica que el numero pasado no pueda dividirse por ningún número entre 2 y el mismo número -1
  for i in range(2,num):
    #Si es divisibles por alguno se retorna false y termina el bucle
    if num%i==0: return False
    print(num%i)
  #Si termina el bucle, significa que no fue divisible, por lo tanto es primo
  return True

#Función que retorna una lista con todos los primos
def primos_hasta(num):
  #Se crea la lista
  primos = []
  for i in range(2,num+1):
    #Se verifica si el valor es primo
    resultado = es_primo(i)
    #En caso que sea primo se agrega a la lista
    if resultado == True: primos.append(i)
  
  #Se retorna la lista
  return primos

#Se crea el resultado llamando a la función y se muestra
resultado = es_primo(9)
print(resultado)