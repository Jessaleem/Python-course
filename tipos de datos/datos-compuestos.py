#creando una lista (se pueden modificar)
lista = ["Jessica Martínez", "Soy Jessica", True,1.60]

#creando una tupla (no se pueden modificar los elementos (añadir o eliminar))
tupla = ("Jessica Martínez", "Soy Jessica", True,1.60)

#esto es válido
lista[3]=1.63

#esto no es válido
#tupla[0]="Sofía Perez"

#creando un conjunto (set) / No puede alterar alguno de los elementos, si se puede redefinir /se puede reordenar /
#no almacena datos duplicados / Se puede iterar (bucle) / No se puede acceder a un índice
conjunto = {"Jessica Martínez", "Soy Jessica", True, 1.60}

#print(conjunto[3]) -> no puede acceder al elemento

#creando un diccionario (dict) / La estructura es 'key': 'value'
diccionario= {
  'nombre' : 'Jessica Martinez',
  'profesion' : 'Ing. Electronica',
  'esta_activa' : True,
  'estatura': 1.60,
  'dato_duplicado': 'Ing. Electronica'
}

print(diccionario['nombre'])
