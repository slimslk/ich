num = int(input("Enter a number: "))

for i in range(1, num + 1):
    for j in range(1, num + 1):
        result = f'{(i * j):<5}'
        print(result, end='')
    print()
