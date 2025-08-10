# polymorphism_demo.py
import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    def __init__(self, length, width):
        if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
            raise TypeError("Length and width must be numbers.")
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive values.")

        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number.")
        if radius <= 0:
            raise ValueError("Radius must be a positive value.")

        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
