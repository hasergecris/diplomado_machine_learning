import pandas as pd
import numpy as np

# Importar la función de NumPy para crear arreglos de números enteros
from numpy.random import seed, randn

seed(10)  # Inicializar el generador aleatorio con una semilla de 10
a = randn()  # Generar un número aleatorio utilizando la función randn de NumPy
print(a)

# Forma rápida de crear una lista de Python desde una cadena de texto
# .split() convierte la cadena en una lista de elementos separados por espacios
print('A B C D E F G H'.split())

df = pd.DataFrame(randn(5, 4),
                  index='Lunes Martes Miercoles Jueves Viernes'.split(),
                  columns='Uvas Manzanas Peras Mangos'.split()
                  )
print(df)
print("El numero de filas y columnas del df es", df.shape)
print(df.info())
print(df.describe())
print(df.head())
print(df.tail())
print(df['Peras'])
df['Banano'] = df['Uvas'] + df['Peras']  # CREAR COLUMNAS
print(df)
print(df.shape)
# ELIMINAR COLUMNAS
df = (df.drop('Peras', axis=1))
print(df)
print(df.shape)
