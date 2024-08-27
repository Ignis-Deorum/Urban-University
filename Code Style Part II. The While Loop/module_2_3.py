my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
elem = 1
i = 0

while i < len(my_list):
    elem = my_list[i]
    if elem < 0:
        break
    if elem != 0:
        print(elem)
    i += 1
