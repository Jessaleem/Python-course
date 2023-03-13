# Ejercicio: Se solicitan los nombres y edades de un conjunto de personas, el mayor es el profesor, el menor es el asistente - Mostrar el profesor y asistente

#Función para obtener el asistente y profesor según la edad
def obtener_compañeros(cantidad_de_compañeros):
  #Crear la lista para almacenar los compañeros
  compañeros = []
  
  #Solicitar nombre y edad de los compañeros mediante un for
  for i in range(cantidad_de_compañeros):
    nombre = input("ingrese el nombre del compañero: ")
    edad = int(input("ingrese la edad del compañero: "))
    compañero = (nombre, edad)
    
    #Agregar la información a la lista
    compañeros.append(compañero)
  
  #Ordenar de menor a mayor según la edad
  compañeros.sort(key= lambda x:x[1])
  
  #Compañeros[x] devuelve una tupla con (nombre, edad) y después se accede al nombre para definir al asistente y profesor
  asistente = compañeros[0][0]
  profesor = compañeros[-1][0]
  
  #Se retorna una tupla
  return asistente, profesor

#Se desempaqueta la tupla
asistente, profesor = obtener_compañeros(5)

#Se muestra la información
print(f'El profesor es: {profesor} y su asistente es {asistente}')