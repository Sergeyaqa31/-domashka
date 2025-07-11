import random

def generate_random_list(n, start, end):
    return [random.randint(start, end) for _ in range(n)]

print(generate_random_list(5, 1, 10))