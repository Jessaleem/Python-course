ingreso_mensual = 500
gasto_mensual = 80000

#if anidades y elif

if ingreso_mensual > 10000:
  if ingreso_mensual - gasto_mensual < 0:
    print('estás en deficit')
  elif ingreso_mensual - gasto_mensual > 3000:
    print('estás bien')
  else:
    print('Estás gastando mucho dinero')

elif ingreso_mensual > 1000:
  print('estás bien en Lationamerica')
  
else:
  print('eres pobre')