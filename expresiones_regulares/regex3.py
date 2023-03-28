import re

text = "reemplazando todas las vocales por asterisco"

#los [] permiten que busque cada letra por separado, en caso de no estar, buscaría las vocales en el mismo orden
new_text = re.sub("[aeiou]", "*", text)

print(new_text)