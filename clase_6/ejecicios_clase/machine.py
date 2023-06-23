# Importar Librerias
from sklearn import neighbors, datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score

# Cargar Dataset
iris = datasets.load_iris()
print("iris", iris)

# Definir cuál es la columna de salida
X, y = iris.data[:, :2], iris.target

# Division del dataset en datos de entrenamiento y de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33)

# Standarizacion de los valores
scaler = preprocessing.StandardScaler().fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Seleccion del algoritmo de macchine learning
knn = neighbors.KNeighborsClassifier(n_neighbors=5)

# Entrenamiento del Modelo
knn.fit(X_train, y_train)

# Prediccion
y_pred = knn.predict(X_test)

# Evaluacion
crossval = cross_val_score(knn, X_train, y_train, cv=4)

print("accuracy", accuracy_score(y_test, y_pred))
# Salida:0.631578947368421 precision del modelo

print("confusion", confusion_matrix(y_test, y_pred))
# matris confuncion

print("clasificacion", classification_report(y_test, y_pred))

print("%0.2f de precision con una desviacion estadar de %0.2f" %
      (crossval.mean(), crossval.std()))
# 0.79 de precision con una desviacion estadar de 0.04

# print("cross", cross_val_score(knn, X_train, y_train, cv=4))
