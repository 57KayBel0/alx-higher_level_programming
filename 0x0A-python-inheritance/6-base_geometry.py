#!/usr/bin/python3
"""Define BaseGeometry class"""


class BaseGeometry:
    """Represent base geometry object"""

    def area(self):
        """Raise an Exception with the message area() is not implemented"""
        return Exception("area() is not implemented")
