#!/usr/bin/python3
"""DefinSquare."""


class Square:
    """Represare."""

    def __init__(self, size=0):
        """Initialuare.

        Args:
            size (int): The size square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
