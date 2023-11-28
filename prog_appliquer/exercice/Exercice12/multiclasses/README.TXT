2023-11-27

L'idée est d'utiliser le classifieur à deux classes (pizza_categories.py) vu en classe pour 
classifier trois classes:
    Iris_setosa
    Iris_versicolor
    Iris_virginica
    
On commence par diviser nos 150 exemples en 3x45 exemples pour la phase de training (dossier train-data) 
et 3x5=15 exemples pour la phase de test (dossier test-data). 

Avec les données d'entraînement, on crée trois modèles (dossier modeles): $ python trainModeles.py
    se-ve pour distinguer entre Iris_setosa et Iris_versicolor
    se-vi pour distinguer entre Iris_setosa et Iris_virginica
    ve-vi pour distinguer entre Iris_versicolor et Iris_virginica

Ce programme (trainModeles.py) et les deux dossiers (test-data et train-data) vous sont fournis.
    
On teste ensuite nos 15 données de test: $ python testData.py
    si les modèles vevi et seve prédisent une Iris-versicolor, Iris-versicolor est la réponse!
    sinon si les modèles vevi et sevi prédisent une Iris-viginica, Iris-virginica est la réponse!
    sinon si les modèles sevi et seve prédisent une Iris-setosa, Iris-setosa est la réponse!
    
Votre travail est de compléter le programme testData.py en vous inspirant de (pizza_categories.py) vu en classe.

Cette approche devrait prédire correctement nos quinze données de tests!

Données de test:
===============
4.8,3.0,1.4,0.3,Iris-setosa
5.1,3.8,1.6,0.2,Iris-setosa
4.6,3.2,1.4,0.2,Iris-setosa
5.3,3.7,1.5,0.2,Iris-setosa
5.0,3.3,1.4,0.2,Iris-setosa
5.7,3.0,4.2,1.2,Iris-versicolor
5.7,2.9,4.2,1.3,Iris-versicolor
6.2,2.9,4.3,1.3,Iris-versicolor
5.1,2.5,3.0,1.1,Iris-versicolor
5.7,2.8,4.1,1.3,Iris-versicolor
6.7,3.0,5.2,2.3,Iris-virginica
6.3,2.5,5.0,1.9,Iris-virginica
6.5,3.0,5.2,2.0,Iris-virginica
6.2,3.4,5.4,2.3,Iris-virginica
5.9,3.0,5.1,1.8,Iris-virginica
Prédictions:
===========
[[6.7, 3.0, 5.2, 2.3]] est une Iris-virginica!
[[6.3, 2.5, 5.0, 1.9]] est une Iris-virginica!
[[6.5, 3.0, 5.2, 2.0]] est une Iris-virginica!
[[6.2, 3.4, 5.4, 2.3]] est une Iris-virginica!
[[5.9, 3.0, 5.1, 1.8]] est une Iris-virginica!
[[5.7, 3.0, 4.2, 1.2]] est une Iris-versicolor!
[[5.7, 2.9, 4.2, 1.3]] est une Iris-versicolor!
[[6.2, 2.9, 4.3, 1.3]] est une Iris-versicolor!
[[5.1, 2.5, 3.0, 1.1]] est une Iris-versicolor!
[[5.7, 2.8, 4.1, 1.3]] est une Iris-versicolor!
[[4.8, 3.0, 1.4, 0.3]] est une Iris-setosa!
[[5.1, 3.8, 1.6, 0.2]] est une Iris-setosa!
[[4.6, 3.2, 1.4, 0.2]] est une Iris-setosa!
[[5.3, 3.7, 1.5, 0.2]] est une Iris-setosa!
[[5.0, 3.3, 1.4, 0.2]] est une Iris-setosa!



