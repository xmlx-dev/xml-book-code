"""
Set Up Execution Environment
============================

This module configures the book execution environment.
These options are loaded and initialised in the module init.
"""

# Author: Kacper Sokol <kacper@xmlx.dev>
# License: MIT

import matplotlib.pyplot as plt

from IPython.display import set_matplotlib_formats

__all__ = ['setup_plotting']

def setup_plotting():
    """Configures default plotting settings."""
    plt.style.use('seaborn')
    set_matplotlib_formats('svg')
