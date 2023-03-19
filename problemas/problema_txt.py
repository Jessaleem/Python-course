# 2 listas, una con nombre otra con apellidos

nombres = ["Roberto","Rodrigo","Guillermo","Cristian","Eugenio"]
apellidos = ["Fuentes","Vergara","Sanchez","Restrepo","Sabbag"]

with open("problemas\\nombres_y_apellidos.txt","w",encoding="UTF-8") as archivo:
  archivo.writelines("Los datos son:\n\n")
  [archivo.writelines(f"Nombre:{n}\nApellido_ {a}\n-------------\n") for n,a in zip(nombres,apellidos)] #[] crea una lista en cada iteración del bucle