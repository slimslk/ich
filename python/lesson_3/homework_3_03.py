first_coordinates = input('Введите координаты первой точки (x1, y1): ').split(', ')
second_coordinates = input('Введите координаты второй точки (x2, y2): ').split(', ')

x1 = float(first_coordinates[0])
y1 = float(first_coordinates[1])
x2 = float(second_coordinates[0])
y2 = float(second_coordinates[1])

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print('Расстояние между точками:', distance)
