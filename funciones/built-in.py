numeros = [4,7,1,42,15]

#Encontrando el número mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#Encontrando el número menor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#Redondeando a 3 decimales
numero = round(12.345678, 3)
print(numero)

#Retorna False en 0, vacio, False, None / True en distinto a 0, cadena, datos no vacíos
resulta_bool = bool()
print(resulta_bool)

#retorna True, si todos los valores son verdaderos
resultado_all = all([1, "Hello", [22,4], 0])
print(resultado_all)

#Suma todo los valores de un iterable
suma_total = sum(numeros)
print(suma_total)