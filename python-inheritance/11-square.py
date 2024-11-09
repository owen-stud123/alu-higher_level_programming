#!/usr/bin/python3
"""
Module for Square class that inherits from Rectangle.
"""


class Rectangle:
    """ Rectangle class to validate and calculate area. """
    def __init__(self, width, height):
        """ Initialize the rectangle with width and height. """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def integer_validator(self, name, value):
        """ Validates that a value is a positive integer """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ String representation of the rectangle """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """ Square class inheriting from Rectangle """

    def __init__(self, size):
        """ Initialize the square with size, validated by integer_validator """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns the area of the square """
        return self.__size ** 2

    def __str__(self):
        """ String representation of the square """
        return f"[Square] {self.__size}/{self.__size}"
