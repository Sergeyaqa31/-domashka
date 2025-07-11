def filter_dict_by_value(d, threshold):
    filtered_items = filter(lambda item: item[1] > threshold, d.items())
    return dict(filtered_items)

print(filter_dict_by_value({'x': 10, 'y': 3, 'z': 7}, 5))