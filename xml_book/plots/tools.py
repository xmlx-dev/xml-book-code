"""
Plotting Tools
==============

This module implements plotting tools for the book.
"""

# Author: Kacper Sokol <kacper@xmlx.io>
# License: MIT

from io import StringIO
from IPython.display import SVG, display

__all__ = ['display_svg']

def display_svg(figure, dpi=300):
    """Displays a `figure` as an SVG."""
    img_data = StringIO()
    figure.savefig(img_data, format='svg', dpi=dpi, bbox_inches='tight')
    img_data.seek(0)  # rewind the data
    # svg_data = img_data.buffer  # this is svg data
    svg_data = ''.join(img_data.readlines())

    display(SVG(data=svg_data))
