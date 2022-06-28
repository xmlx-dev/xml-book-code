"""
Array Display
=============

This module implements HTML displaying function for NumPy arrays.
"""

# Author: Kacper Sokol <kacper@xmlx.io>
# License: MIT

import IPython
import warnings

import numpy as np

__all__ = ['DisplayArray']

_NUMPY_NUMERICAL_KINDS = set('B?buifc')


def is_flat_dtype(dtype: np.dtype) -> bool:
    """Determines whether a numpy dtype object is flat."""
    assert isinstance(dtype, np.dtype), 'NumPy dtype object.'
    assert dtype.names is None, ('The numpy dtype object is structured. '
                                 'Only base dtype are allowed.')
    is_flat = len(dtype.shape) == 0
    return is_flat


def is_numerical_dtype(dtype: np.dtype) -> bool:
    """Determines whether a numpy dtype object is of numerical type."""
    assert isinstance(dtype, np.dtype), 'NumPy dtype object.'
    # If the dtype is complex
    assert dtype.names is None, ('The numpy dtype object is structured. '
                                 'Only base dtype are allowed.')
    is_numerical = dtype.kind in _NUMPY_NUMERICAL_KINDS
    return is_numerical


def is_structured_array(array: np.ndarray) -> bool:
    """Determines whether a numpy array-like object is a structured array."""
    assert isinstance(array, np.ndarray), 'NumPy array-like.'
    return len(array.dtype) != 0


def is_numerical_array(array: np.ndarray) -> bool:
    """Determines whether a numpy array-like object has a numerical data type."""
    assert isinstance(array, np.ndarray), 'NumPy array-like object.'
    if is_structured_array(array):
        is_numerical = True
        for i in range(len(array.dtype)):
            if not is_numerical_dtype(array.dtype[i]):
                is_numerical = False
                break
    else:
        is_numerical = is_numerical_dtype(array.dtype)
    return is_numerical


def is_2d_array(array: np.ndarray) -> bool:
    """Determines whether a numpy array-like object has 2 dimensions."""
    assert isinstance(array, np.ndarray), 'NumPy array-like.'

    if is_structured_array(array):
        if len(array.shape) == 2 and len(array.dtype) == 1:
            is_2d = False
            message = ('2-dimensional arrays with 1D structured elements are '
                       'not acceptable. Such a numpy array can be expressed '
                       'as a classic 2D numpy array with a desired type.')
            warnings.warn(message, category=UserWarning)
        elif len(array.shape) == 1 and len(array.dtype) > 0:
            is_2d = True
            for name in array.dtype.names:
                if not is_flat_dtype(array.dtype[name]):
                    # This is a complex (multi-dimensional) embedded dtype
                    is_2d = False
                    break
        else:
            is_2d = False
    else:
        is_2d = len(array.shape) == 2

    return is_2d


class DisplayArray(object):
    """
    Displays a NumPy array as either a HTML object (in the Jupyter environment)
    or a string.
    
    Inspired by <https://github.com/data-8/datascience>.
    """

    def __init__(self,
                 array: np.ndarray,
                 max_rows: int = 10,
                 column_names: list = None,
                 column_formatters: dict = None,
                 indent_size: int = 4,
                 display_head: bool = True,
                 numerical_precision: int = 3,
                 text_separator: str = ' | ',
                 centre: bool = False):
        """Initialises DisplayArray class."""
        assert isinstance(array, np.ndarray), 'NumPy array required.'
        assert is_2d_array(array), '2D NumPy array required.'
        self.array = array
        self.num_rows = array.shape[0]

        assert isinstance(max_rows, int) and max_rows > 0, 'Positive integer.'
        if max_rows > self.num_rows:
            max_rows = self.num_rows
        self.max_rows = max_rows

        assert (column_names is None
                or (isinstance(column_names, list) and column_names)), (
                    'Non-empty list or None.'
                )
        if is_structured_array(array):
            if column_names is None:
                column_names = array.dtype.names
            else:
                warnings.warn('Using custom labels.', category=UserWarning)
                assert len(array.dtype.names) == len(column_names), (
                    'The list of labels must coincide with number of columns.')
        else:
            assert (isinstance(column_names, list)
                    and len(column_names) == array.shape[1]), (
                        'Column names expected.')
        self.column_names = column_names
        self.num_columns = len(self.column_names)

        assert isinstance(indent_size, int) and indent_size >= 0, 'Non-negative int.'
        assert column_formatters is None or isinstance(column_formatters, dict), (
            'None or a dictionary of formatters.')
        _lambda_num = lambda x: f'{{:.{numerical_precision}f}}'.format(x)
        _lambda_str = lambda x: x
        if column_formatters is None:
            column_formatters = dict()
            if is_structured_array(array):
                for label, name in zip(self.column_names, array.dtype.names):
                    dtype = array.dtype[name]
                    _lambda = _lambda_num if is_numerical_dtype(dtype) else _lambda_str
                    column_formatters[label] = _lambda
            else:
                _lambda = _lambda_num if is_numerical_array(array) else _lambda_str
                for label in self.column_names:
                    column_formatters[label] = _lambda
        else:
            assert len(column_formatters) == self.num_columns, 'Correct number of columns.'
            for k, v in column_formatters.items():
                assert k in self.column_names, 'Valid column name.'
                assert callable(v), 'Python callable.'
        self.column_formatters = column_formatters

        assert isinstance(indent_size, int) and indent_size > 0, 'Positive int.'
        self.indent_size = indent_size
        assert isinstance(display_head, bool), 'Boolean.'
        self.display_head = display_head
        assert isinstance(text_separator, str) and text_separator, 'Non-empty str.'
        self.text_separator = text_separator
        assert isinstance(centre, bool), 'Boolean.'
        self.centre = centre

    def __str__(self):
        return self.as_text(max_rows=self.max_rows,
                            text_separator=self.text_separator,
                            display_head=self.display_head)

    __repr__ = __str__

    def _repr_html_(self):
        return self.as_html(max_rows=self.max_rows,
                            indent_size=self.indent_size,
                            display_head=self.display_head,
                            centre=self.centre)

    def show(self, max_rows=None, indent_size=4, display_head=True, centre=False):
        """Display the table in IPython (IPython.core.display.HTML)."""
        IPython.display.display(IPython.display.HTML(self.as_html(
            max_rows=max_rows,
            indent_size=indent_size,
            display_head=display_head,
            centre=centre)))

    def as_text(self, max_rows=None, text_separator=' | ', display_head=True):
        """Format NumPy array as text."""
        if max_rows is None or not max_rows or max_rows > self.num_rows:
            max_rows = self.num_rows
        skipped_rows = max(0, self.num_rows - max_rows)

        rows = [(i for i in self.column_names)] if display_head else []
        for row in self.array[:max_rows]:
            row_list = []
            for row_value, label in zip(row, self.column_names):
                fmt = self.column_formatters[label]
                row_list.append(fmt(row_value))
            rows.append(tuple(row_list))
        lines = [text_separator.join(row).rstrip() for row in rows]
        if skipped_rows:
            lines.append((0, f'... ({skipped_rows} rows sipped)'))

        return '\n'.join(lines)

    def as_html(self, max_rows=None, indent_size=4, display_head=True, centre=False):
        """Format table as HTML."""
        if max_rows is None or not max_rows or max_rows > self.num_rows:
            max_rows = self.num_rows
        skipped_rows = max(0, self.num_rows - max_rows)

        centre = (' style="margin-left: auto; margin-right: auto; '
                  'margin-bottom: 1em;"') if centre else ''  # margin-top: 1em;
        lines = [(0, f'<table border="1" class="dataframe"{centre}>')]

        if display_head:
            lines += [(1, '<thead>'), (2, '<tr>')]
            for label in self.column_names:
                lines.append((3, f'<th>{label}</th>'))
            lines += [(2, '</tr>'), (1, '</thead>')]

        lines.append((1, '<tbody>'))

        for row in self.array[:max_rows]:
            lines.append((2, '<tr>'))
            for row_value, label in zip(row, self.column_names):
                fmt = self.column_formatters[label]
                lines.append((3, f'<td>{fmt(row_value)}</td>'))
            lines.append((2, '</tr>'))

        lines += [(1, '</tbody>'), (0, '</table>')]
        if skipped_rows:
            lines.append((0, f'<p>... ({skipped_rows} rows sipped)</p>'))

        html = '\n'.join(
            indent_size * indent * ' ' + text for indent, text in lines)

        return html
