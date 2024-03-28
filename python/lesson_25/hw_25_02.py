# Напишите программу, которая будет считывать данные о продуктах из файла и использовать аннотации типов для
# аргументов и возвращаемых значений функций. Создайте текстовый файл "products.txt", в котором каждая строка будет
# содержать информацию о продукте в формате "название, цена, количество".
#
# Например:
# Apple, 1.50, 10
# Banana, 0.75, 15
#
# В программе определите функцию calculate_total_price, которая будет принимать список продуктов и возвращать общую
# стоимость. Продумайте, какая аннотация должна быть у аргумента! Считайте данные из файла, разделите строки на
# составляющие и создайте список продуктов. Затем вызовите функцию calculate_total_price с этим списком и выведите
# результат.

def get_products_from_file(filename: str) -> list[tuple[str, float, int]]:
    product_list = []
    with open(filename) as file:
        lines = file.readlines()
    for line in lines:
        product = [item.strip() for item in line.split(",")]
        product_list.append((product[0], float(product[1]), int(product[2])))
    return product_list


def calculate_total_price(product_list: list[tuple[str, float, int]]) -> float:
    return sum([product[1] for product in product_list])


FILENAME = "products.txt"
prod_list = get_products_from_file(FILENAME)
total_price = calculate_total_price(prod_list)
print(f"Total price of all products is: {total_price}")
