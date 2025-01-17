"""
XML Book Python Package
=======================

This library implements a collection of Python modules used by the book.
"""

# Author: Kacper Sokol <kacper@xmlx.dev>
# License: MIT

import xml_book.config as cfg

__author__ = 'Kacper Sokol'
__email__ = 'kacper@xmlx.dev'
__license__ = 'MIT'
__version__ = '0.1'

__all__ = ['RANDOM_SEED']

RANDOM_SEED = 42

cfg.setup_plotting()
