import csv

with open("archivos\\datos.csv") as archivo:
  file = csv.reader(archivo)
  for row in file:
    print(row)
  