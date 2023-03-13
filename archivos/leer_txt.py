archivo = open("archivos\\texto_de_muestra.txt", encoding="UTF8")

#Leer archivo completo
#archivo = archivo_sin_leer.read()

#Readlines - para archivos pequeños, en archivos grandes no se recomienda por el uso de memoria
#Leer linea por línea
#lineas = archivo.readlines()

#Leer una sola línea
linea = archivo.readline(50) #Se puede pasar un parámetro para especificar la cantidad de letras que se quiere leer, si no se pasa el parámetro, lee la primera línea
print(linea)

#Cerrar el archivo
archivo.close()
