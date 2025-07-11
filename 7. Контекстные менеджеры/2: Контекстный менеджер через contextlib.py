import time
from contextlib import contextmanager

@contextmanager
def time_tracker():
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Время выполнения: {elapsed_time:.4f} секунд")


with time_tracker():
    time.sleep(1)