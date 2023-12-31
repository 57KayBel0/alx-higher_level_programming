#!/usr/bin/python3
""""Define Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a object Rectangle"""

    def __init__(self, width, height):
        """
        Inicialize a Rectangle object

        Parametters
        -----------
            width (int): The Rectangle's width
            height (int): The Rectangle's width
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
