def square_odds(nums):
    odd_numbers = filter(lambda x: x % 2 != 0, nums)
    squared_odds = map(lambda x: x ** 2, odd_numbers)
    return list(squared_odds)

print(square_odds([1, 2, 3, 4, 5]))