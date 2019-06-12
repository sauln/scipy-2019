import numpy as np
from matplotlib.patches import Circle, Wedge, Polygon, FancyArrowPatch
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
from sklearn import datasets

from palette import palette

print("Circles")

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

data, _ = datasets.make_circles(noise=0.1)

ax = plt.subplot(132, xticks=[], yticks=[])
# ax.annotate("", xy=(0.5, 0.5), xytext=(0, 0), arrowprops=dict(arrowstyle="->"))

x_tail = 0.0
y_tail = 0.5
x_head = 0.9
y_head = 1.0
dx = x_head - x_tail
dy = y_head - y_tail

arrow = FancyArrowPatch((x_tail, y_tail), (dx, dy),
                                 mutation_scale=30,
                                 color=palette[3])
ax.add_patch(arrow)
ax.axis('off')

ax = plt.subplot(133, aspect='equal', xticks=[], yticks=[])
ax.scatter(data[:,0], data[:,1], c=palette[0])
ax.axis('off')
plt.tight_layout()

plt.savefig('../images/generated/circles.png', bbox_inches='tight')

