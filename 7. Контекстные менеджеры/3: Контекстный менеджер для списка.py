from contextlib import contextmanager

@contextmanager
def list_context_manager(original_list):
    copied_list = original_list.copy()
    try:
        yield original_list
    finally:
        original_list[:] = copied_list