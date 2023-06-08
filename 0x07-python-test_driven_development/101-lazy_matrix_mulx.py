#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a matrix multi using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The firrix.
        m_b (list of lists of ints/floats): The strix.
    """

    return (np.matmul(m_a, m_b))
