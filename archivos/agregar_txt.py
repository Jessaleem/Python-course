with open('archivos\\texto_de_muestra.txt', "a", encoding= "UTF-8") as archivo:
  #agregando el archivo
  archivo.write("\n")
  for i in range(5):
    archivo.write(f'linea {i+1} agregada\n')
  
