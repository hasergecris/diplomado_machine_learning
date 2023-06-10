#histogramas
import matplotlib.pyplot as plt
from random import sample
data = sample(range(1, 1000), 100)
plt.hist(data,bins = 10) # bins el numero de divisiones del histograma
plt.title("Histograma");
plt.show()