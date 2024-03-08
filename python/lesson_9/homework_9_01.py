from string import ascii_lowercase

my_text = input('Enter a text: ')
alphabet = ascii_lowercase

i = 0
while i < len(alphabet):
    if alphabet[i] in my_text.lower():
        i += 1
        print(i)
    else:
        print('Your text is not a pangram')
        break
else:
    print('Your text is a pangram')
