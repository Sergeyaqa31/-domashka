def merge_lists(a, b):
    merged_extend = a.copy()
    merged_extend.extend(b)

    merged_plus = a + b

    return merged_plus

print(merge_lists([1, 2], [3, 4]))