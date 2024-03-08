my_text = input('Enter a text: ').lower()

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxyz.'

vowel_letters = ''
consonant_letters = ''

i = 0
while i < len(my_text):
    if my_text[i] in vowels:
        vowel_letters += my_text[i]
    if my_text[i] in consonants:
        consonant_letters += my_text[i]
    i += 1

print(f'Vowels: "{vowel_letters}", length: {len(vowel_letters)}')
print(f'Consonants: "{consonant_letters}", length: {len(consonant_letters)}')
