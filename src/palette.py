import numpy as np

import matplotlib.pyplot as plt

palette = ["#54DCC6", "#7991F2", "#CF1259", "#FDBB5D", "#DD7596"]


def plot_diagrams_custom(diagrams):

    ax = plt.subplot(111, aspect='equal', xticks=[], yticks=[])


    labels = [
            "$H_0$",
            "$H_1$",
            "$H_2$",
            "$H_3$"
    ]

    size=20
    xlabel, ylabel = "Birth", "Death"

    diagrams = [dgm.astype(np.float32, copy=True) for dgm in diagrams]

    concat_dgms = np.concatenate(diagrams).flatten()
    has_inf = np.any(np.isinf(concat_dgms))
    finite_dgms = concat_dgms[np.isfinite(concat_dgms)]

    ax_min, ax_max = np.min(finite_dgms), np.max(finite_dgms)
    x_r = ax_max - ax_min

    # Give plot a nice buffer on all sides.
    # ax_range=0 when only one point,
    buffer = x_r / 5

    x_down = ax_min - buffer / 2
    x_up = ax_max + buffer

    y_down, y_up = x_down, x_up

    yr = y_up - y_down
    ax.plot([x_down, x_up], [x_down, x_up], "--", c='k')

    # Plot inf line
    if has_inf:
        # put inf line slightly below top
        b_inf = y_down + yr * 0.95
        ax.plot([x_down, x_up], [b_inf, b_inf], "--", c="k", label=r"$\infty$")

        # convert each inf in each diagram with b_inf
        for dgm in diagrams:
            dgm[np.isinf(dgm)] = b_inf

    # Plot each diagram
    for dgm, label, color in zip(diagrams, labels, palette):

        # plot persistence pairs
        ax.scatter(dgm[:, 0], dgm[:, 1], size, label=label, c=color, edgecolor=color, alpha=1.0)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.ticklabel_format()
    ax.set_xlim([x_down, x_up])
    ax.set_ylim([y_down, y_up])
    ax.set_aspect('equal', 'box')
    ax.legend(loc="lower right")
