class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area == other.area

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area < other.area

    def __le__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area <= other.area

rectangle1 = Rectangle(1, 1)
rectangle2 = Rectangle(2, 2)
rectangle3 = Rectangle(2, 2)

print(rectangle1 == rectangle2)
print(rectangle2 == rectangle3)
print(rectangle1 < rectangle2)
print(rectangle2 < rectangle3)
print(rectangle2 <= rectangle3)