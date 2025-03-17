import math

class Shape:
    """Base class representing a generic shape."""
    def area(self):
        """Method to calculate area - must be overridden in derived classes."""
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    """Derived class representing a rectangle."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Overrides the area method to calculate the area of a rectangle."""
        return self.length * self.width

class Circle(Shape):
    """Derived class representing a circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Overrides the area method to calculate the area of a circle."""
        return math.pi * (self.radius ** 2)
