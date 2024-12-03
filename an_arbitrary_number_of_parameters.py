def single_root_words(root_word, *other_words):
    same_words = []
    root_word1 = root_word.lower()

    for word in other_words:
        word1 = word.lower()
        if root_word1 in word1 or word1 in root_word1:
            same_words.append(word)
        return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers',
                            'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable',
                            'Bagel')
print(result1)
print(result2)
