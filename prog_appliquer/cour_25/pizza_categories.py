import pandas as pd # analyse de données
from sklearn.model_selection import train_test_split # AA
from tensorflow.keras.models import Sequential, load_model # AA
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score
import tensorflow as tf

fd = pd.read_csv('pizza_categories.txt')
# on omet la cible et on transforme les traits non-numériques
X = pd.get_dummies(fd.drop(['Seuil-rentabilité'], axis = 1)) # les traits
y = fd['Seuil-rentabilité'] # la cible catégorique
# on divise nos données
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2)

# Ici, on choisit et paramétrise notre modèle: voir https://www.tensorflow.org/
#====================
model = Sequential()
model.add(Dense(units=32, activation = 'relu', input_dim = len(X_train.columns)))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=1, activation = 'sigmoid'))
model.compile(optimizer='sgd', loss = 'binary_crossentropy', metrics='accuracy')
#====================
# On le produit, epochs est le nombre d'itérations
# model.fit(X_train, y_train, epochs = 200)
model.fit(tf.convert_to_tensor(X_train , dtype=tf.int32),
          tf.convert_to_tensor(y_train , dtype=tf.int32), epochs = 200)

# on demande les prédictions pour X_test
y_pred = model.predict(tf.convert_to_tensor(X_test , dtype=tf.int32))
# On mappe [0,0.5] à 0 et 1 autrement
y_pred = [0 if val < 0.5 else 1 for val in y_pred]

print("La vérité:")
print(y_test) # la vérité
print("La prédiction:")
print(y_pred) # la prédiction

print("Exactitude: ", round(accuracy_score(y_test, y_pred),2))

model.save('modele_pizza')

model = load_model('modele_pizza')

