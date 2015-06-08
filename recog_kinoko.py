# -*- coding: utf-8 -*-

import os

import numpy as np
from sklearn.cluster import KMeans

base = os.path.dirname(os.path.abspath(__file__))
data = np.genfromtxt(os.path.join(base, 'CodeIQ_data.txt'), delimiter=' ')
eaten = np.genfromtxt(os.path.join(base, 'CodeIQ_eaten.txt'), delimiter=' ', dtype=['f8', 'f8', 'S5'])

safe_kinoko = np.array([[x[0], x[1]] for x in eaten if x[2] == b'o'])[0]

kmeans_model = KMeans(n_clusters=3, random_state=10).fit(data)
labels = kmeans_model.labels_

safe_label = labels[np.where(data == safe_kinoko)[0]][0]

for label, feature in zip(labels, data):
    if label == safe_label:
        print(label, feature)
