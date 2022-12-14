# -*- coding: utf-8 -*-
"""Untitled16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U19fdD0ymJ6kIVYIDrodCO-a8AN8CwYb
"""

# Criando clusters com dados sinteticos
import numpy as np
from sklearn.cluster import KMeans

s = np.random.uniform(0, 1, 200)

x = np.random.uniform(0, 1, 200)
x

matriz = np.dstack((s, x))
matriz[0]

# metodo do Cotovelo
nClusters = 10
Wc = []
for i in range(nClusters):
  i +=1
  kmeans = KMeans(i)
  kmeans.fit(matriz[0])
  # Aqui temos a media da distancia euclidiana 
  # para todos pontos do cluster
  print(' Clusters: ', i, ' W(c): ', kmeans.inertia_)
  Wc.append(kmeans.inertia_)

# Plotamos a distancia media para os diferentes 
# clusters de 1 a 10
import matplotlib.pyplot as plt
plt.plot(range(1, 11), Wc)
# plt.show()

# Clusterizamos os dados em 4 grupos
kmeans = KMeans(4)
kmeans.fit(matriz[0])

colors = [ 'g.', 'r.', 'b.', 'c.']
matriz = matriz[0]
for i in range(len(matriz)):
  # print(' coordenada do objeto: ', matriz[i], 
  # 'nome do cluster (label): ', kmeans.labels_[i])
  plt.plot(matriz[i][0], matriz[i][1], 
           colors[kmeans.labels_[i]], markersize=10)

