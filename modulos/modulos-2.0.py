#Carpeta dentro de la misma ruta
#import funciones_buenas.saludar as m_saludar
#print(m_saludar.saludar("Jess"))

import sys

#Carpeta fuera de la misma ruta
sys.path.append('C:\\Users\\aleej\\Documents\\GitHub\\Python-course\\funciones_buenas')
# print(sys.path) permite ver las rutas de las carpetas

import saludar
print(saludar.saludar("Jess"))