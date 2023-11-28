import pandas as pd # analyse de données
from sklearn.model_selection import train_test_split # AA
from tensorflow.keras.models import Sequential, load_model # AA
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score
import tensorflow as tf
# Lecture des données d'entraînement
fd1 = pd.read_csv(".\\train-data\\iris-se-vi.data")
fd2 = pd.read_csv('.\\train-data\\iris-ve-vi.data')
fd3 = pd.read_csv('.\\train-data\\iris-se-ve.data')
# Substitution de la classe par une valeur numérique
fd1.replace({'Iris-setosa':1,'Iris-virginica':0}, inplace = True)
fd2.replace({'Iris-versicolor':1,'Iris-virginica':0}, inplace = True)
fd3.replace({'Iris-setosa':1,'Iris-versicolor':0}, inplace = True)
# Données
X1 = pd.get_dummies(fd1.drop(['Classe'], axis = 1)) # les traits
X2 = pd.get_dummies(fd2.drop(['Classe'], axis = 1)) # les traits
X3 = pd.get_dummies(fd3.drop(['Classe'], axis = 1)) # les traits
# Classes
y1 = fd1['Classe'] # la cible catégorique
y2 = fd2['Classe'] # la cible catégorique
y3 = fd3['Classe'] # la cible catégorique
# On s'entraîne sur toutes les données
X1_train = X1
y1_train = y1
X2_train = X2
y2_train = y2
X3_train = X3
y3_train = y3

# Ici, on choisit et paramétrise notre modèle: voir https://www.tensorflow.org/
model1 = Sequential()
model1.add(Dense(units=32, activation = 'relu', input_dim = len(X1_train.columns)))
model1.add(Dense(units=64, activation='relu'))
model1.add(Dense(units=1, activation = 'sigmoid'))
model1.compile(optimizer='sgd', loss = 'binary_crossentropy', metrics='accuracy')
model2 = Sequential()
model2.add(Dense(units=32, activation = 'relu', input_dim = len(X2_train.columns)))
model2.add(Dense(units=64, activation='relu'))
model2.add(Dense(units=1, activation = 'sigmoid'))
model2.compile(optimizer='sgd', loss = 'binary_crossentropy', metrics='accuracy')
model3 = Sequential()
model3.add(Dense(units=32, activation = 'relu', input_dim = len(X3_train.columns)))
model3.add(Dense(units=64, activation='relu'))
model3.add(Dense(units=1, activation = 'sigmoid'))
model3.compile(optimizer='sgd', loss = 'binary_crossentropy', metrics='accuracy')

# On le produit, epochs est le nombre d'itérations
model1.fit(tf.convert_to_tensor(X1_train, dtype=tf.int32), tf.convert_to_tensor(y1_train , dtype=tf.int32), epochs = 200)
model2.fit(tf.convert_to_tensor(X2_train, dtype=tf.int32), tf.convert_to_tensor(y2_train , dtype=tf.int32), epochs = 200)
model3.fit(tf.convert_to_tensor(X3_train, dtype=tf.int32), tf.convert_to_tensor(y3_train , dtype=tf.int32), epochs = 200)

# On le sauvegarde
model1.save('.\\modeles\\se-vi')
model2.save('.\\modeles\\ve-vi')
model3.save('.\\modeles\\se-ve')


