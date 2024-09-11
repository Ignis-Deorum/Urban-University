def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ['abc', False, 27]
values_dict = {'a': 23, 'b': False, 'c': 'test'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['qwerty', 90]
print_params(*values_list_2, 42)

