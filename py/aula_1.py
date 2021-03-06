# -*- coding: utf-8 -*-
"""Aula 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Sce-I5vdkG7Raxuzpy2XGX9DxZPiEpyg

# Introdução a Machine Learning e Classificação

## Primeiro treino e teste de um modelo de classificação

Aula da Alura "Machine Learning: Introdução a classificação com SKLearn"

### Introduzindo as features

Features (1 Sim, 0 Não)
- Pelo Longo?
- Perna Curta?
- Faz Latidos?
"""

from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC


porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1, 0]

cachorro1 = [0,1,1]
cachorro2 = [1,0,1]
cachorro3 = [1,1,1]

"""> 1 => porco, 0 => cachorro"""

treino_x = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
treino_y = [1,1,1,0,0,0]



model = LinearSVC()
model.fit(treino_x, treino_y)

animal_misterioso = [1,1,1]
model.predict([animal_misterioso])

misterio1 = [1,1,1]
misterio2 = [1,1,0]
misterio3 = [0,1,1]

testes = [misterio1, misterio2, misterio3]
model.predict(testes)

misterio1 = [1,1,1]
misterio2 = [1,1,0]
misterio3 = [0,1,1]

teste_x = [misterio1, misterio2, misterio3]
teste_y = [0,1,1]

previsoes = model.predict(teste_x)

corretos = (previsoes == teste_y).sum()
total = len(teste_x)
taxa_de_acerto = corretos/total
print("Taxa de acerto %.2f: " % (taxa_de_acerto * 100))


taxa_de_acerto = accuracy_score(teste_y, previsoes)
print("Taxa de acerto %.2f: " % (taxa_de_acerto * 100))

