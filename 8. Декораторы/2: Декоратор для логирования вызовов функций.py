def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__} с аргументами: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@log_calls
def example_function(a, b):
    return a + b


example_function(2, 3)
example_function(a=10, b=20)
example_function(5, b=7)