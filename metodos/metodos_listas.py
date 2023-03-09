#Crear una lista con list
lista = list(['Lucy', 'Bolt', 6, 10, True])

#Contar longitud de la lista (cant de elementos)
cantidad_de_elementos = len(lista)

#Agregar elemento a la lista en la última posición
lista.append('Dance')

#Agregar un elemento a lista en una posición definida
lista.insert(2, "Mama")

#Agregar varios elementos a la lista
lista.extend([False, 2023])

#Eliminar elemento a una lista (por su índice) / números negativos para contar desde la última posición -1 es el último
lista.pop(1)

#Eliminar un elemento de la lista por su valor
lista.remove(True)

#Eliminar todos los elementos de una lista
#lista.clear()

lista2 = [20, 30, 40, True, False, -1, 10]

#Ordenar de forma accendente, párametro (reverse=True) para ordenar de forma descendente
#lista2.sort(reverse=True)

#Invertir los elementos
lista2.reverse()

#Encontrar el índice de un elemento
elemento_encontrado = lista.index(6)


print(elemento_encontrado)