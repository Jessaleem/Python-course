#Abrir el archivo con with open
with open('archivos\\texto_de_muestra.txt', encoding= "UTF-8") as archivo:
  
  #leer el archivo
  contenido = archivo.read()
  
  #mostrar el archivo
  print(archivo.read())
  
#No es necesario cerrar!