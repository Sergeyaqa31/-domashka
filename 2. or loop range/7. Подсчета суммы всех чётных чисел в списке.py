numbers = [1, 2, 3, 4, 5, 6]
sum_even = 0

for number in numbers:
    if number % 2 == 0:
        sum_even += number

print(sum_even)