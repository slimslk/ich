my_string = input('Enter a string: ')
width = int(input('Enter a width: '))

while width <= len(my_string):
    width = int(input('The width must be greater than the length of the string: '))
if len(my_string) % 2 == width % 2:
    my_string = my_string.center(width)
else:
    my_string = my_string.rjust(width)
print(my_string)
