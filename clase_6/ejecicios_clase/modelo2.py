import matplotlib.pyplot as plt
import numpy as np

#score = np.array([0.9, 0.8, 0.7, 0.6, 0.55, 0.54, 0.53, 0.52, 0.51, 0.505, 0.4, 0.39, 0.38, 0.37, 0.36, 0.35, 0.34, 0.33, 0.30, 0.1])
score = np.random.rand(1000)

#y = np.array([1,1,0, 1, 1, 1, 0, 0, 1, 0, 1,0, 1, 0, 0, 0, 1 , 0, 1, 0])
y = np.random.randint(2, size=1000)

# agrego algunos 1 mas
for i in range(len(y)):
    if (y[i] == 0) and (score[i]>0.3) and (np.random.randint(2) == 1):
        y[i] =  1 
for i in range(len(y)):
    if (y[i] == 0) and (score[i]>0.5) and (np.random.randint(2) == 1):
        y[i] =  1 
for i in range(len(y)):
    if (y[i] == 0) and (score[i]>0.7) and (np.random.randint(2) == 1):
        y[i] =  1 
for i in range(len(y)):
    if (y[i] == 0) and (score[i]>0.7) and (np.random.randint(2) == 1):
        y[i] =  1 


#print(score)
#print(y)

# false positive rate
fpr = []

# true positive rate
tpr = []

# umbrales 0.0, 0.01, ... 1.0
thresholds = np.arange(0.0, 1.01, .01)

# obtengo el número de ejemplos positivos y negativos en el conjunto de datos
P = sum(y)
N = len(y) - P

# itero a través de todos los umbrales y determinar la fracción de 
# verdaderos positivos y falsos positivos que encontramos en este umbral
for thresh in thresholds:
    FP=0
    TP=0
    for i in range(len(score)):
        if (score[i] > thresh):
            if y[i] == 1:
                TP = TP + 1
            else:
                FP = FP + 1
    fpr.append(FP/float(N))
    tpr.append(TP/float(P))

plt.scatter(fpr, tpr)
plt.show()