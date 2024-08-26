immutable_var = ([4, 5], 'abc', 3, 1.2, True)
print('Immutable tuple:', immutable_var)

# Единственный объект, который в данном случае возможно изменить - список внутри кортежа.
# Остальные объекты внутри кортежа изменить не получится и при попытке мы получим ошибку.
immutable_var[0][0] = 3
print('Immutable tuple:', immutable_var)

mutable_list = [5, 8, 0, 'xyz']
mutable_list[2] = 1
print('Mutable list:', mutable_list)