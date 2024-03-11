first_num = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

sum_num = first_num + second_number
mult_num = first_num * second_number

result_as_string_1 = "Сумма: {sum:.2f}, Произведение: {product:.2f}".format(sum=sum_num, product=mult_num)
result_as_string_2 = f"Сумма: {sum_num:.2f}, Произведение: {mult_num:.2f}"

print(result_as_string_1)
print(result_as_string_2)
