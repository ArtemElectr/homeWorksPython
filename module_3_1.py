calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    if isinstance(string, str):
        return tuple([len(string), string.upper(), string.lower()])
    else:
        return f'{string} не является строкой'


def is_contains(string, list_to_searсh):
    count_calls()
    string = string.lower()

    if isinstance(string, str) and isinstance(list_to_searсh, list):
        for i in list_to_searсh:
            i = i.lower()
            if i.count(string):
                return True
        return False
    else:
        return 'неверные параметры'


print(string_info("Capybara"))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('BeGIn', ['cyclic', 'beginning']))
print(is_contains('BeGIn', ['cyclic', 'begi']))
print(calls)
