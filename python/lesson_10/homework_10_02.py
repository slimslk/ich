my_text = input('Enter a sentence: ')

i = 0
not_unique_letters = ''

while i < len(my_text):
    if my_text[i].isalpha():
        if my_text.lower().find(my_text[i].lower(), i+1, len(my_text)) != -1:
            not_unique_letters += my_text[i]
    i += 1

if not not_unique_letters:
    print("The sentence contains unique letters.")
else:
    print(f'The sentence contains non-unique letters: {not_unique_letters}')
