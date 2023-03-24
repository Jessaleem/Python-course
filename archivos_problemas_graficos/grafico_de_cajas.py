import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\bigotes.csv")
print(df)

#Crear el gráfico
sns.boxplot(x="categoria",y="valor",data=df)


#Mostrar el gráfico
plt.show()