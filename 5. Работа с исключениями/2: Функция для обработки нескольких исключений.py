data = {"x": "10", "y": "0", "z": "abc"}


def multiple_exceptions_handling(key1, key2):
    result = None
    try:
        num1 = int(data[key1])
        num2 = int(data[key2])
        division_result = num1 / num2
    except KeyError as e:
        print(f"Ошибка: ключ {e} не найден в словаре")
    except ValueError:
        print("Ошибка: невозможно преобразовать значение в число")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
    else:
        print("Ошибок не возникло")
        result = division_result
    finally:
        print("Блок finally выполнен")

    return result

print(multiple_exceptions_handling("x", "y"))
print(multiple_exceptions_handling("x", "z"))
print(multiple_exceptions_handling("x", "w"))
print(multiple_exceptions_handling("x", "y"))