from functools import wraps

def cache_results(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper


@cache_results
def expensive_computation(x, y):
    return x * y


# Тестирование
print(expensive_computation(2, 3))  # Вычисляется и кэшируется
print(expensive_computation(2, 3))  # Берётся из кэша
print(expensive_computation(4, 5))  # Вычисляется и кэшируется
print(expensive_computation(4, 5))  # Берётся из кэша