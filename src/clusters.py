import matplotlib.pyplot as plt
from sklearn import datasets


print("Clusters")
import numpy as np
np.random.seed(101146010)

from palette import palette


blobs, labels = datasets.make_blobs(n_samples=1000)

plt.xticks([], [])
plt.yticks([], [])
plt.scatter(blobs[:,0], blobs[:, 1], s=3, c=palette[3])
plt.savefig('../images/generated/clusters_no_color.png', bbox_inches='tight')



for i in range(3):
    bs = blobs[labels == i]
    plt.scatter(bs[:,0], bs[:, 1], s=3, c=palette[i])
plt.xticks([], [])
plt.yticks([], [])


plt.savefig('../images/generated/clusters_color.png', bbox_inches='tight')
