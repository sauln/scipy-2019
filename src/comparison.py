import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np


import tadasets
from sklearn import datasets
from palette import palette, plot_diagrams_custom

print("Torus")


r=3
r2=2

torus = tadasets.torus(n=1000)
circlehoriz, _ = datasets.make_circles()

ns = np.linspace(0, 2 * np.pi, 100)
xs = np.cos(ns)*1
ys = np.sin(ns)*1

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(torus[:,0], torus[:,1], torus[:,2], c=palette[1], s=3, alpha=0.5)
ax.plot(xs, ys, c='k', linewidth=2, zorder=9999)
# ax.plot(xs*r, ys*r, c='k', linewidth=2)
ax.plot(np.zeros_like(xs), r2+xs, ys, c='k', linewidth=2, zorder=99999)

ax.view_init(elev=18., azim=4)

plt.tight_layout()



ax.axis('square')
ax.axis('off')
r = 1.7
xr = 1.5
ax.set_xlim3d(-r, r)
ax.set_ylim3d(-r, r)
ax.set_zlim3d(-xr, xr)
plt.savefig('../images/generated/torus.png', bbox_inches='tight')
# plt.show()



import ripser

ax = plt.subplot(111)

torus = tadasets.torus(n=400)
rip = ripser.Rips(maxdim=2)
dgms = rip.fit_transform(torus)

plot_diagrams_custom(dgms)

plt.savefig('../images/generated/torus_pd.png', bbox_inches='tight')
