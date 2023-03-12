diccionario = {
  "nombre": "jessica",
  "apellido": "martinez",
  "edad": 34
}

#Recorrer diccionario para obtener las llaves
for key in diccionario:
  print(key)
  
#Recorrer diccionario para obtener las llaves y los valores
for data in diccionario.items():
  key = data[0]
  value = data[1]
  print(f'La clave es: {key} y el valor es: {value}')
 