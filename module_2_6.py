# Первый вариант функции использует in для поиска фрагмента в слове
def single_root_words_v1(root_word, *other_words):
    same_words = []
    same_words_v2 = []
    root_word = root_word.lower()

    for i in range(len(other_words)):
        next_word = other_words[i].lower()

        if (root_word in next_word) and (len(root_word) <= len(next_word)):
            same_words.append(other_words[i])
            continue
        elif (next_word in root_word) and (len(next_word) < len(root_word)):
            same_words.append(other_words[i])

    return same_words


# Второй вариант функции использует count для поиска фрагмента в слове
def single_root_words_v2(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()

    for i in range(len(other_words)):
        next_word = other_words[i].lower()

        if (next_word.count(root_word) > 0) and (len(root_word) <= len(next_word)):
            same_words.append(other_words[i])
            continue
        elif (root_word.count(next_word) > 0) and (len(next_word) < len(root_word)):
            same_words.append(other_words[i])
            continue

    return same_words


result1 = single_root_words_v1('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words_v1('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print('-----------var1 - Поиск фрагмента с помощью in-----------')
print(result1)
print(result2)

print('-----------var2 - Поиск фрагмента с помощью count--------')
result1 = single_root_words_v2('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words_v2('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
