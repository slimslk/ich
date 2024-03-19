def anagrams(list_of_words):
    angr = {}
    for word in list_of_words:
        sorter_word = ''.join(sorted(word))
        if not angr.get(sorter_word):
            angr[sorter_word] = [word]
        else:
            angr[sorter_word].append(word)
    return angr


words = ['cat', 'dog', 'tac', 'god', 'act']
result = anagrams(words)
print(*result.values())
