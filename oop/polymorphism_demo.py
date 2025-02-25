import math

# Base class for Shapes
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  # Area of a rectangle

# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2  # Area of a circle using πr²
