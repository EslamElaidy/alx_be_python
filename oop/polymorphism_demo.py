import math

# Base class - Shape
class Shape:
    def area(self):
        raise NotImplementedError("Derived classes must implement this method")

# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Main function to demonstrate polymorphism
def main():
    # Create a list of shapes
    shapes = [
        Rectangle(4, 5),
        Circle(3)
    ]

    # Loop through each shape and print the area
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
