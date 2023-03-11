#Crear con set()
conjunto = set(["dato1", "dato2"])

#Meter un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato3"}

print(conjunto2)

#Teoría de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto1 > conjunto2

#Verificar si hay algún número en común / Es True cuando los conjuntos que se están comparando no tienen ni un solo número en común
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)