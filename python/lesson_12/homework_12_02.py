first_list = input('Enter elements of a first list separated by spaces: ')
second_list = input('Enter elements of a second list separated by spaces: ')

first_list = first_list.split(' ')
second_list = second_list.split(' ')

comb_list = list(zip(first_list, second_list))

print(comb_list)