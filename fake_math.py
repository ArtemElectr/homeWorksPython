def divide(first, second):
    if isinstance(first, int) and isinstance(second, int):
        if second != 0:
            return first / second
        else:
            return 'Ошибка'
    else:
        return f'параметры не являются числами'