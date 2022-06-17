"""
Overview Plots
==============

This module implements functions for plotting examples.
"""

# Author: Kacper Sokol <kacper@xmlx.io>
# License: MIT

import matplotlib.colors as plt_colors
import numpy as np
import scipy.interpolate as interpolate

from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

from xml_book import RANDOM_SEED


__all__ = ['local_linear_surrogate']

LINEAR_MODEL = np.array([[3.8, -1], [5.15, 9]])


def local_linear_surrogate_line(ax):
    ax.plot(LINEAR_MODEL[:, 0], LINEAR_MODEL[:, 1],
             '--', c='black', alpha=.7, linewidth=3)


def local_linear_surrogate(plot_axis=None, figsize=(10, 8), plot_line=True):
    """
    Visualises an example of a local linear surrogate in 2 dimensions.
    
    https://towardsdatascience.com/visualizing-clusters-with-pythons-matplolib-35ae03d87489
    """
    if plot_axis is None:
        fig = plt.figure(figsize=figsize)  # dpi=600
        fig, ax = plt.subplots(1, 1, figsize=figsize)
        # plt.set_size_inches(10, 8)
    else:
        fig = None
        ax = plot_axis

    # Define points
    x = np.array([0.0, 1.5, 3.0, 1.5, 3.0, 5.0, 8.5, 10.0, 8.0, 9.5, 12.5, 15.0, 14.0, 11.0])
    y = np.array([8.0, 7.5, 7.0, 2.5, 1.0, 7.5, 1.0,  3.5, 5.0, 7.0,  0.0,  6.0,  8.0,  9.0])

    # Smooth
    dist = np.sqrt((x[:-1] - x[1:])**2 + (y[:-1] - y[1:])**2)
    dist_along = np.concatenate(([0], dist.cumsum()))
    spline, u = interpolate.splprep([x, y], u=dist_along, s=0)
    interp_d = np.linspace(dist_along[0], dist_along[-1], 500)
    interp_x, interp_y = interpolate.splev(interp_d, spline)

    # Plot
    r = Rectangle((-0.5,-0.5), 16.5, 10.0,
                  color='blue', alpha=0.1, fill=True, linewidth=0)
    ax.add_patch(r)

    ax.fill(interp_x, interp_y, '--', c='red', alpha=0.2)

    if plot_line:
        local_linear_surrogate_line(ax)

    ax.set_xlim((-0.1, 15.15))
    ax.set_ylim((-0.1, 9.05))

    ax.set_xticks([])
    ax.set_yticks([])

    ax.tick_params(axis='both',
                    which='both', bottom='off', top='off', labelbottom='off',
                    right='off', left='off', labelleft='off')
    plt.tight_layout()
    return fig, ax


def local_linear_surrogate_advanced(
        plot_axis=None, figsize=(10, 8),
        plot_line=True, scale_points=True, plot_sample=True):
    """
    Visualises an example of a local linear surrogate in 2 dimensions
    with sampling and scaling.
    """
    cc = plt.get_cmap('tab10')  # Set3
    colours = [plt_colors.rgb2hex(cc(i)) for i in range(cc.N)]

    fig, ax = local_linear_surrogate(
        plot_axis=plot_axis, figsize=figsize, plot_line=plot_line)

    x_circ = (4.3, 5)

    np.random.seed(RANDOM_SEED)
    sample = np.random.normal(loc=x_circ, scale=(.75, 1.5), size=(20, 2))

    x, y = LINEAR_MODEL[:, 0], LINEAR_MODEL[:, 1]
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    def surrogate(points):
        assert len(points.shape) == 2, 'Expect 2D numpy array'
        y_ = m * points[:, 0] + c - points[:, 1]
        y = np.vectorize(lambda i: 0 if i > 0 else 1)(y_)
        return y

    sample_y = surrogate(sample)
    sample_colour = np.vectorize(lambda i: True if i else False)(sample_y)
    sample_size = 50 / np.linalg.norm(sample - x_circ, axis=1)

    scale = 250 if scale_points else 100
    scale_0 = sample_size[sample_colour] if scale_points else scale
    scale_1 = sample_size[~sample_colour] if scale_points else scale

    ax.scatter(*x_circ, marker='P', s=scale, linewidths=2,
               c=colours[3], edgecolors=colours[2], zorder=10, alpha=.9)
    if plot_sample:
        ax.scatter(sample[sample_colour, 0], sample[sample_colour, 1],
                c=colours[3], marker='P', s=scale_0, zorder=9, alpha=.8)
        ax.scatter(sample[~sample_colour, 0], sample[~sample_colour, 1],
                c=colours[0], marker='$\u25AC$', s=scale_1, zorder=9, alpha=.8)

    plt.tight_layout()
    return fig, ax
