import time

def your_decorator(sleep_seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(sleep_seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator