# Эта функция составляет новый список same_words только из тех слов списка other_words, которые содержат root_word
# или наоборот root_word содержит одно из этих слов.
# This function creates a new list same_words from only those words in the list other_words that contain root_word
# or vice versa root_word contains one of these words.
def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if word.lower() in root_word.lower() or root_word.lower() in word.lower():
            same_words.append(word)
    return same_words


# Проверка корректности работы функции
# Checking whether the function is working correctly
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
