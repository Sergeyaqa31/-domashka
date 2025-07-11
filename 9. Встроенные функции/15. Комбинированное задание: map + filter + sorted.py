def process_numbers(nums):
    even_numbers = filter(lambda x: x % 2 == 0, nums)
    squared_numbers = map(lambda x: x ** 2, even_numbers)
    return sorted(squared_numbers, reverse=True)

print(process_numbers([5, 2, 7, 4, 1, 8]))