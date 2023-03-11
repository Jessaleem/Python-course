#promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_prom = 4
este_curso = 1.5

#Duración de Crudos
crudo_promedio = 5
crudo_este_curso = 3.5

#Diferencias de duración
diferencia_con_min = 100 - este_curso / otros_cursos_min * 100
diferencia_con_max = 100 - este_curso * 1000 // otros_cursos_max / 10
diferencia_con_prom = 100 - este_curso / otros_cursos_prom * 100

#Procentaje de tiempo vacío removido
tiempo_vacío_promedio = 100 - otros_cursos_prom * 1000 // crudo_promedio /10
tiempo_vacío_este_curso = 100 - este_curso * 1000 // crudo_este_curso /10

#Diferencia de duración
print('___________________________')
print('Este curso dura:')
print(f'un {diferencia_con_min}% menos que el más rápido')
print(f'un {diferencia_con_max}% menos que el más lento')
print(f'un {diferencia_con_prom}% menos que el promedio')
print('___________________________')

#Cantidad de espacios vacíos que se remueven 
print(f'Un curso promedio elimina un {tiempo_vacío_promedio}% de tiempo vacío')
print(f'Este curso promedio elimina un {tiempo_vacío_este_curso}% de tiempo vacío')
print('___________________________')

#Mostrar diferencias si los cursos duraran 10 horas
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_prom * 100 // este_curso /10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {este_curso * 100 // otros_cursos_prom /10} horas de este curso')
print('___________________________')