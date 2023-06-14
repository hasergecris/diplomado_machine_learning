import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

archivo = pd.read_csv('https://github.com/mwaskom/seaborn-data/raw/master/anscombe.csv')
print(archivo)

agg = archivo.groupby('dataset').agg([np.mean, np.var])
print(agg)

corr = archivo.groupby('dataset').corr()['x'].unstack(level=1).iloc[:, 1].tolist()
print(corr)

sns.set(style="ticks")
sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=archivo,
           col_wrap=2, ci=None, palette="muted", height=4,
           scatter_kws={"s": 50, "alpha": 1})

fits = [np.polyfit(g['x'], g['y'], 1) for _, g in archivo.groupby('dataset')]
val_reg = pd.DataFrame(fits, columns=['pendiente', 'intercepto'], index='I II II IV'.split())
val_reg.index.names = ['dataset']
print(val_reg)

plt.show()  # Mostrar las gráficas
