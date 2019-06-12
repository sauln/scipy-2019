import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np


from tadasets import dsphere
from sklearn import datasets
from palette import palette, plot_diagrams_custom


print("Sphere")

sphere = dsphere(d=2, n=1000)
circlehoriz, _ = datasets.make_circles()

ns = np.linspace(0, 2 * np.pi, 100)
xs = np.cos(ns)*1
ys = np.sin(ns)*1


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(sphere[:,0], sphere[:,1], sphere[:,2], c=palette[0], s=3)
ax.plot(xs, ys, c='k', linewidth=2)
# ax.plot(np.zeros_like(xs), xs, ys, c='k', linewidth=2)
# ax.plot(xs, np.zeros_like(xs), ys, c='k', linewidth=2)

ax.axis('square')
ax.axis('off')

r = 0.6
ax.set_xlim3d(-r, r)
ax.set_ylim3d(-r, r)
ax.set_zlim3d(-r, r)
ax.view_init(elev=10., azim=-57)

plt.savefig('../images/generated/sphere.png', bbox_inches='tight')


import ripser

ax = plt.subplot(111)
sphere = dsphere(d=2, n=400)
rip = ripser.Rips(maxdim=2)
dgms = rip.fit_transform(sphere)

plot_diagrams_custom(dgms)

plt.savefig('../images/generated/sphere_pd.png', bbox_inches='tight')
