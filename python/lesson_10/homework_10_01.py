my_text = input("Enter a string: ")

vowels = "aeiouAEIOU"
i = 0

while i < len(vowels):
    if vowels[i] in my_text:
        my_text = my_text.replace(vowels[i], '')
    i += 1

print(f'The string without vowels is: {my_text}')
