from math import inf


def divide(first, second):
    if type(first) == int and type(second) == int:
        if second != 0:
            return first / second
        else:
            return inf
    else:
        return f'параметры не являются числами'
