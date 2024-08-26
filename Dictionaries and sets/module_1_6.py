# Работа со словарями:
my_dict = {'Key1': 1, 'Key2': 2, 'Key3': 3}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Key1'))
print('Not existing value:', my_dict.get('Key0'))
my_dict.update({'Key4': 4, 'Key5': 5})
print('Deleted value:', my_dict.pop('Key2'))
print('Modified dictionary:', my_dict)

# Работа с множествами:
my_set = {1, 1, 1, 3, 2, 3, 6, 8, 6, 'abc', 6, 'abc'}
print('\nSet:', my_set)
my_set.add(9)
my_set.add(4)
my_set.discard(1)
print('Modified set:', my_set)