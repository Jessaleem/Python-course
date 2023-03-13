with open('archivos\\texto_de_muestra.txt', "w", encoding= "UTF-8") as archivo:
  #Sobreescribir el achivo
  #archivo.write("nuevo texto")
  
  #Sobreescribir varias lineas \n permite agregar un salto de línea
  archivo.writelines(["Maravilloso\n", "tu puedes lograrlo!\n"])