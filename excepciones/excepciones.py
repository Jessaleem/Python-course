#Crear función que suma numeros
def sumar_dos():
  #Inicia un bucle
  while True:
    #Solicita números
    a = input("Numero 1: ")
    b = input("Numero 2: ")
    #Intentar convertirlos a entero y sumarlos
    try:
      resultado = int(a) + int(b)
    #Si lanzó una excepción, pedirle que reingrese los datos
    except ValueError as e:
      print("El valor debe ser numerico")
      print(f"ERROR: {type(e).__name__}")
    #Si todo sale pedir finaliza el bucle
    else:
      break
    #finally se ejecuta siempre
    finally:
      print("Esto se ejecuta siempre")
  
  return resultado

print(sumar_dos())