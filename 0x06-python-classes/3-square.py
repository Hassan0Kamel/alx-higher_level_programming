#!/usr/bin/python3
"""Define auare."""


class Square:
    """Represare."""

    def __init__(self, size=0):
        """Initialiuare.

        Args:
            size (int): The sisquare.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the currenthe square."""
        return (self.__size * self.__size)
