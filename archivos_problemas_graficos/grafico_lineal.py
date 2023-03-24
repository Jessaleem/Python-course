import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\dulces.csv")
print(df)

#Crear el gráfico
sns.lineplot(x="fecha",y="dulces",data=df)

#Crear un punto en el momento de más dulces
plt.plot("01-09",17,"o")

#Mostrar el gráfico
plt.show()