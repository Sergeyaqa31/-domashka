def sort_words(words):
    sorted_list = sorted(words)

    words_copy = words.copy()
    words_copy.sort()

    return sorted_list, words_copy

words = ["banana", "apple", "cherry"]
sorted_with_sorted, sorted_with_sort = sort_words(words)

print("Сортировка через sorted:", sorted_with_sorted)
print("Сортировка через .sort():", sorted_with_sort)