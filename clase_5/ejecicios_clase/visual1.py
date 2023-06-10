import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Leer el archivo CSV desde la URL
archivo = pd.read_csv('https://github.com/mwaskom/seaborn-data/raw/master/anscombe.csv')
print(archivo)

# Mapear los valores de la columna 'dataset' a números enteros
archivo['dataset'] = archivo['dataset'].map({'I': 1, 'II': 2, 'III': 3, 'IV': 4})

# Calcular la media y la varianza para cada dataset
agg = archivo.groupby('dataset').agg([np.mean, np.var])
print(agg)

# Calcular la correlación para cada dataset
corr = [g.corr()['x'][1] for _, g in archivo.groupby('dataset')]
print(corr)

# Configurar el estilo de las gráficas de seaborn
sns.set(style="ticks")

# Graficar los datasets utilizando lmplot()
sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=archivo,
          col_wrap=2, ci=None, palette="muted", height=4,
          scatter_kws={"s": 50, "alpha": 1})

# Calcular los valores de la regresión lineal para cada dataset
fits = [np.polyfit(g['x'], g['y'], 1) for _, g in archivo.groupby('dataset')]

# Crear un DataFrame con los valores de las regresiones lineales
val_reg = pd.DataFrame(fits, columns=['pendiente', 'intercepto'], index='I II II IV'.split())
val_reg.index.names = ['dataset']
print(val_reg)

# Mostrar las gráficas generadas por seaborn
plt.show()
