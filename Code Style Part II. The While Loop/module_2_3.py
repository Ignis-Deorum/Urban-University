my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
elem = 1
i = 0

while elem >= 0:
    elem = my_list[i]
    i += 1
    if elem > 0:
        print(elem)
    if i == len(my_list):
        break
