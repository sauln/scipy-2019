import numpy as np
from matplotlib.patches import Circle, Wedge, Polygon, FancyArrowPatch
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
from sklearn import datasets

from palette import palette, plot_diagrams_custom

print("Loop")

# Fixing random state for reproducibility
np.random.seed(19680801)



n, radii = 50, [.7, .95]
theta = np.linspace(0, 2*np.pi, n, endpoint=True)
xs = np.outer(radii, np.cos(theta))
ys = np.outer(radii, np.sin(theta))

# in order to have a closed area, the circles
# should be traversed in opposite directions
xs[1,:] = xs[1,::-1]
ys[1,:] = ys[1,::-1]



ax = plt.subplot(131, aspect='equal', xticks=[], yticks=[])
ax.fill(np.ravel(xs), np.ravel(ys), color=palette[0], edgecolor=palette[0])
ax.axis('off')

data, _ = datasets.make_circles(noise=0.1, n_samples=1000)

ax = plt.subplot(111, aspect='equal', xticks=[], yticks=[])
ax.scatter(data[:,0], data[:,1], c=palette[4], s=5)
ax.axis('off')
plt.tight_layout()

plt.savefig('../images/generated/loop.png', bbox_inches='tight')



import ripser

ax = plt.subplot(111)

data, _ = datasets.make_circles(noise=0.1, n_samples=300)

rip = ripser.Rips(maxdim=1)
dgms = rip.fit_transform(data)

plot_diagrams_custom(dgms)

plt.savefig('../images/generated/loop_pd.png', bbox_inches='tight')
