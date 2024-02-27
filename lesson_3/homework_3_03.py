first_coordinates = input('Введите координаты первой точки (x1, y1):').split(', ')
second_coordinates = input('Введите координаты второй точки (x2, y2):').split(', ')


distance = ((float(second_coordinates[0]) - float(first_coordinates[0])) ** 2
            + (float(second_coordinates[1]) - float(first_coordinates[1])) ** 2) ** 0.5

print('Расстояние между точками:', distance)
