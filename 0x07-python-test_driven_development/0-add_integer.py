#!/usr/bin/python3
# 0-add_integer.py
"""Defines an integer afunction."""


def add_integer(a, b=98):
    """Return the inton of a and b.

    Float arguments are typee addition is performed.

    Raises:
        TypeError: If either ofeger and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
