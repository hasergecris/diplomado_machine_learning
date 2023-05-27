import pandas as pd;
import numpy as np;

#MANEJO DE PD SERIES 
#Crear diferentes tipos de datos 

# labels = ['a','b','c'] #lisra de datos
# my_list = [10, 20, 30] #lista con valores 
# arr = np.array([10, 20, 30]) # Convierte la lista de valores en arreglo array
# d = {'a':10,'b':20,'c':30} 

# CREANDO SERIE 1 

ser1 = pd.Series([1,2,3,4],index =['USA','GERMANY','USSR','JAPAN'])

# CREANDO SERIE 2 
ser2 = pd.Series([1,2,3,4],index =['USA','GERMANY','ITALY','JAPAN'])

a = ser2['GERMANY']
print(a)
a = ser1 + ser2
print(a)