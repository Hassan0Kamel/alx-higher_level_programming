#!/usr/bin/python3
"""Define a classare."""


class Square:
    """Represent aare."""

    def __init__(self, size=0):
        """Initialize auare.

        Args:
            size (int): The sizesquare.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the curree square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current  square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Define the == compaquare."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != compauare."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparisoare."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= compato a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > compquare."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmquare."""
        return self.area() >= other.area()
