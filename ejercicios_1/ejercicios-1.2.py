frase = input('Dime una frase y cálculo cuanto tardarías si tuvieras que decirla: ')
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
tiempo_de_la_frase = cantidad_de_palabras / 2

print(f'tardarías {tiempo_de_la_frase} segundos en decir esa frase')
print(f'dijiste {cantidad_de_palabras} palabras')
if tiempo_de_la_frase > 60 :
  print('Pará, es muy larga esa frase')

print(f'Dalto tardaría en decirlo {tiempo_de_la_frase * 100 * 0.7 / 100} segundos')