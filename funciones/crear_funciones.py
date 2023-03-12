#Crear una función simple
def saludar():
  print("Hello Jess, you are doing it great")

#Ejecutando una función simple
saludar()

def saludar2(nombre, sexo):
  sexo = sexo.lower()
  if sexo == "mujer":
    adjetivo= "reina"
  elif sexo == "hombre":
    adjetivo = "chico"
  else:
    adjetivo = "amor"

  print(f"Hello {nombre}, mi {adjetivo} como estás?")
  
saludar2("Jessica", "Mujer")

#Crear una función que retorne multiples valores

def crear_contrasena(num):
  chars = "abcdefghij"
  num_entero = str(num)
  num = int (num_entero[0])
  c1 = num - 2
  c2 = num
  c3 = num - 5
  contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
  return contraseña,num

#Desempaquetando la función
password, primer_numero = crear_contrasena(5)

#Mostrando los resultados obtenidos
print(f"Tu contraseña es: {password}")
print(f"El primer numero utilizado para usarla fue el: {primer_numero}")