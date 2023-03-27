import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\ingresos.csv")
print(df)

#Crear el gráfico
sns.barplot(x="fuente",y="ingresos",data=df)

#Obtener el total de ingresos
total_ingresos = df['ingresos'].sum()

#Mostrar el total de ingresos
print(f"El total de ingresos es de: {total_ingresos} USD")


#Mostrar el gráfico
plt.show()