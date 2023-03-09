diccionario = {
  "nombre": 'jessica',
  "apellido": 'martinez',
  "edad":35
}

#Método keys -> devuelve las llaves y permite iterar
llaves = diccionario.keys()

#Método get -> devuelve el valor de una llave (Si no encuentra la llave el programa continúa, no lanza una excepción, accediendo con diccionario['llave'] se para el programa porque lanza una excepción)
valor = diccionario.get('apellido')

#Eliminar un elemento del diccionario
diccionario.pop('apellido')

#Obtener un elemento dict_items iterable
diccionario_iterable = diccionario.items()

#Elimina todo del diccionario
#diccionario.clear()

print(diccionario_iterable)