# Создайте класс Rectangle для представления прямоугольника. Класс должен иметь атрибуты width (ширина) и
# height (высота), а также метод calculate_area(), который вычисляет площадь прямоугольника.
# Затем создайте экземпляр класса Rectangle с заданными значениями ширины и высоты и выведите его площадь.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


rect = Rectangle(13, 20)
print(f"Area of the rectangle is: {rect.calculate_area()}")
