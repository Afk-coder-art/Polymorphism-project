# Triangle class
class Triangle:
    def __init__(self):
        self._base = 0
        self._height = 0

    def set_dimensions(self, base, height):
        self._base = base
        self._height = height

    def calculate_area(self):
        return 0.5 * self._base * self._height

# Rectangle class
class Rectangle:
    def __init__(self):
        self._length = 0
        self._width = 0

    def set_dimensions(self, length, width):
        self._length = length
        self._width = width

    def calculate_area(self):
        return self._length * self._width

# Square class
class Square:
    def __init__(self):
        self._side = 0

    def set_dimensions(self, side):
        self._side = side

    def calculate_area(self):
        return self._side * self._side

triangle = Triangle()
rectangle = Rectangle()
square = Square()

triangle.set_dimensions(10, 5)
rectangle.set_dimensions(8, 2)
square.set_dimensions(6)

shapes = (triangle, rectangle, square)
for shape in shapes:
    print("The area is:", shape.calculate_area())
