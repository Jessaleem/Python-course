import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\dispersion.csv")
print(df)

#Crear el gráfico
sns.scatterplot(x="tiempo",y="dinero",data=df)


#Mostrar el gráfico
plt.show()