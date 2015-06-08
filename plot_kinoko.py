# -*- coding: utf-8 -*-

import os

import numpy as np
import matplotlib.pyplot as plt

base = os.path.dirname(os.path.abspath(__file__))
data = np.genfromtxt(os.path.join(base, 'CodeIQ_data.txt'), delimiter=' ')
eaten = np.genfromtxt(os.path.join(base, 'CodeIQ_eaten.txt'), delimiter=' ', dtype=['f8', 'f8', 'S10'])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

all_kinoko = np.array([[x[0], x[1]] for x in data]).T
ax.scatter(all_kinoko[0], all_kinoko[1], color='b')

safe_kinoko = np.array([[x[0], x[1]] for x in eaten if x[2] == b'o']).T
ax.scatter(safe_kinoko[0], safe_kinoko[1], color='g')

out_kinoko = np.array([[x[0], x[1]] for x in eaten if x[2] == b'x']).T
ax.scatter(out_kinoko[0], out_kinoko[1], color='r')

plt.legend(loc='best')
# plt.show()
plt.savefig(os.path.join(base, 'image.png'))
