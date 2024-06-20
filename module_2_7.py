def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params('str', 5.12, 34)
print_params(9.9, 'str_value')
print_params('value')

print_params(b=25)
# print_params(c = [1,2,3])  # TypeError: print_params() got an unexpected keyword argument 'c'

values_list = [99, 'element', 11.11]
values_dict = {'a': 'Artemy', "b": 1989, 'c': 14.11}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['string', 17.5]
print_params(*values_list_2, 42)
