#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry object"""

    def area(self):
        """Raise an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")
  
    def integer_validator(self, name, value):
        """Validate a input value"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
           raise ValueError("{} must be greater than 0".format(name))
