def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return -  None