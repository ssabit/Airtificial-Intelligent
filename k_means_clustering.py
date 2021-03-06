# -*- coding: utf-8 -*-
"""k_means_clustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kCjSwkjBPB3yL4ffPYho8W7jI8sfex92
"""

from google.colab import drive

drive.mount("/content/gdrive")

import numpy as np

data_path = "/content/gdrive/My Drive/data.csv"
data = np.genfromtxt(data_path, delimiter=",")

center_path = "/content/gdrive/My Drive/centers.csv"
centers = np.genfromtxt(center_path, delimiter=",")

import math
import copy
from matplotlib import pyplot as plt

data_size = data.shape[0]
print(data_size)
centers_number = centers.shape[0]
print(centers_number)

for i in range(centers_number):
    print(centers[i])

plt.scatter(data[:, 0], data[:, 1], s=7)

clusters_number = centers_number
data_row = data.shape[0]
data_column = data.shape[1]

mean = np.mean(data, axis=0)
std = np.std(data, axis=0)
centers = np.random.randn(clusters_number, data_column) * std + mean

plt.scatter(data[:, 0], data[:, 1], s=7)
plt.scatter(centers[:, 0], centers[:, 1], marker="*", c="b", s=150)

print(data.shape)
print(centers.shape)

centers_privious = np.zeros(centers.shape)
print(centers_privious)
centers_current = copy.deepcopy(centers)

data.shape
clusters = np.zeros(data_row)
distances = np.zeros((data_row, clusters_number))

error = np.linalg.norm(centers_current - centers_privious)
print(error)

while error != 0:

    for i in range(clusters_number):
        distances[:, i] = np.linalg.norm(data - centers[i], axis=1)

    clusters = np.argmin(distances, axis=1)

    centers_old = copy.deepcopy(centers_current)

    for i in range(clusters_number):
        centers_current[i] = np.mean(data[clusters == i], axis=0)
    error = np.linalg.norm(centers_current - centers_old)
centers_current

plt.scatter(data[:, 0], data[:, 1], s=7)
plt.scatter(centers_current[:, 0], centers_current[:, 1], marker="*", c="r", s=100)