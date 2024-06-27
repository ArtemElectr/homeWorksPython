def calculate_structure_sum(*data):
    sum_ = 0
    for i in data:
        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            sum_ += calculate_structure_sum(*i)
        elif isinstance(i, int):
            sum_ += i
        elif isinstance(i, str):
            sum_ += len(i)
        elif isinstance(i, dict):
            sum_ += calculate_structure_sum(*i.values())
            sum_ += calculate_structure_sum(*i.keys())
    return sum_


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(*data_structure))
