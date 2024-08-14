
def is_prime(func):
    def wrapper(first_, second_, third_):
        result_ = func(first_, second_, third_)
        if result_ > 1:
            count = 0
            for i in range(2, result_):
                if result_ % i == 0:
                    count += 1
                    if count > 2:
                        print("Составное")
                        return result_
            print("Простое")
            return result_
    return wrapper


@is_prime
def sum_three(first, second, third):
    return first + second + third


result = sum_three(2, 3, 46)
print(result)
