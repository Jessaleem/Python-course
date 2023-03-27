#Crear mi propia excepción personalidaza
class MiExcepcion(Exception):
  def __init__(self,err):
    print(f"Impresionante, cometiste el siguiente error: {err}")

#Lanzando mi propia excepción
#raise MiExcepcion("jajajaj, persona poco culta")

#Manejando mi propia excepción
try:
  raise MiExcepcion("jajajaj, persona poco culta")
except:
  print("Como vas a cometer ese error?")