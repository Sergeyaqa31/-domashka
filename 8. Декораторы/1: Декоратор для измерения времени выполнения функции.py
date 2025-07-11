import time

def time_logger(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} — {time.time() - start:.3f} сек")
        return result
    return wrapper

@time_logger
def example_function():
    time.sleep(1)

example_function()