#Formas de importar módulos

#1. import carpeta.nombre (sin extensión) se utiliza "as" para reasignar un nombre (opcional)
import modulos_saludar as saluditos

saludo = saluditos.saludar("Jessica")
print(saludo)

#2. importar solo alguna(s) función(es) especificas del módulo con from carpeta.nombre import función1, función2 también se puede cambiar el nombre con "as"

from modulos_saludar import saludar, saludar2

saludo = saludar("Jessica")
saludo2 = saludar2("Jessica")

#Mostrar los resultados
print(saludo)
print(saludo2)

#Para ver las propiedades y métodos de el namespace
#print(dir(namespace))

#Acceder al nombre del módulo
print(__name__)

#Acceder al nombre del módulo llamado cuando se renombre
print(saluditos.__name__)