# Реализуйте абстрактный базовый класс Shape (фигура), а от него унаследуйте классы Rectangle (прямоугольник)
# и Circle (круг). Класс Shape должен иметь абстрактный метод area, который должен быть реализован в каждом дочернем
# классе. Классы Rectangle и Circle также должны иметь метод perimeter для расчета периметра.
# Выведите площадь и периметр прямоугольника и круга на экран.
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):

    def __init__(self, raduis):
        self.radius = raduis

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


rectangle = Rectangle(5, 3)
circle = Circle(2)
print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")
print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")
