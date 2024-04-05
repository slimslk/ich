# Создайте класс Rectangle для представления прямоугольника.
# Класс должен иметь атрибуты width (ширина) и height (высота) со значениями по умолчанию,
# а также методы calculate_area() для вычисления площади прямоугольника и calculate_perimeter() для вычисления
# периметра прямоугольника. Переопределить методы __str__, __repr__. Затем создайте экземпляр класса Rectangle и
# выведите информацию о нем, его площадь и периметр.


class Rectangle:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 4 * self.height * self.width

    def __str__(self):
        return f"Width is: {self.width} and height is: {self.height}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.width}, {self.height})"


rect = Rectangle(10, 20)
print(str(rect))
print(repr(rect))
print(f"The rectangle area is: {rect.calculate_area()}")
print(f"The rectangle perimeter is: {rect.calculate_area()}")
