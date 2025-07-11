def sorted_dict_keys(d):
    return sorted(d.keys())

def sorted_dict_items_by_value(d):
    return sorted(d.items(), key=lambda item: item[1])

d = {'b': 2, 'a': 1, 'c': 3}
print(sorted_dict_keys(d))
print(sorted_dict_items_by_value(d))