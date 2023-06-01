#!/usr/bin/python3
"""Define a MagicClass matching ovided b."""

import math


class MagicClass:
    """Represrcle."""

    def __init__(self, radius=0):
        """InitializClass.

        Arg:
            radius (float or int): The radi MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return theicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumfcClass."""
        return (2 * math.pi * self.__radius)
