#Creando una función de 3 parametros
def frase(nombre, apellido, adjetivo):
  return f'Hola {nombre} {apellido} {adjetivo}'

#Utilizando keyword arguments
frase_respuesta1 = frase(adjetivo= 'mamacita',nombre= 'jessica', apellido= 'martinez')
print(frase_respuesta1)

#Creando la misma función con un parametro opcional y un valor por defecto
def frase2(nombre, apellido, adjetivo = "brillante"):
  return f'Hola {nombre} {apellido}, eres muy {adjetivo}'

frase_respuesta2 = frase2('jessica','martinez')
print(frase_respuesta2)
