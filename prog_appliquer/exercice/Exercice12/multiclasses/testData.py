import pandas as pd # analyse de données
from sklearn.model_selection import train_test_split # AA
from tensorflow.keras.models import Sequential, load_model # AA
from tensorflow.keras.layers import Dense
from sklearn.metrics import accuracy_score
import tensorflow as tf
import numpy as np
# Données de test, pas besoin de les lire
Iris_setosa1 = [[4.8,3.0,1.4,0.3]]
Iris_setosa2 = [[5.1,3.8,1.6,0.2]]
Iris_setosa3 = [[4.6,3.2,1.4,0.2]]
Iris_setosa4 = [[5.3,3.7,1.5,0.2]]
Iris_setosa5 = [[5.0,3.3,1.4,0.2]]
Iris_versicolor1 = [[5.7,3.0,4.2,1.2]]
Iris_versicolor2 = [[5.7,2.9,4.2,1.3]]
Iris_versicolor3 = [[6.2,2.9,4.3,1.3]]
Iris_versicolor4 = [[5.1,2.5,3.0,1.1]]
Iris_versicolor5 = [[5.7,2.8,4.1,1.3]]
Iris_virginica1 = [[6.7,3.0,5.2,2.3]]
Iris_virginica2 = [[6.3,2.5,5.0,1.9]]
Iris_virginica3 = [[6.5,3.0,5.2,2.0]]
Iris_virginica4 = [[6.2,3.4,5.4,2.3]]
Iris_virginica5 = [[5.9,3.0,5.1,1.8]]


model1 = tf.keras.models.load_model('./modeles/se-ve')
model2 = tf.keras.models.load_model('./modeles/se-vi')
model3 = tf.keras.models.load_model('./modeles/ve-vi')

# Assuming your input data is stored in a variable named 'input_data'
# Perform prediction
# Read data from the file

# Extract input features (assuming the data has four feature columns)
#input_data = data.iloc[:, :-1]  # Assuming the last column is the label



class_labels = {
    0: "Iris-setosa",
    1: "Iris-versicolor",
    2: "Iris-virginica"
}
prediction = model1.predict(Iris_setosa1)
print(prediction)

prediction = model3.predict(Iris_setosa1)
print(prediction)


