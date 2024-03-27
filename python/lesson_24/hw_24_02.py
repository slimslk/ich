# Напишите генератор, который будет генерировать арифметическую прогрессию

def arithmetic_progression(start_number, step):
    while True:
        yield start_number
        start_number += step


nums = list(map(int, input("Enter the start number and progression step separated by a space: ").split()))
ap = arithmetic_progression(nums[0], nums[1])
count = int(input("Enter the number of sequence elements to display: "))
for _ in range(count):
    print(next(ap))
ap.close()
