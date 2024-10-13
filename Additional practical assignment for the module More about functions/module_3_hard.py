# Задает исходные переменные программы
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    """Данная функция подсчитывает сумму всех чисел и длин всех строк внутри переменной *args."""
    # Задает исходные переменные функции
    data = [*args]
    answer = 0
    flag = True
    # Превращает исходные данные в плоский список
    while flag:
        for elem in data:
            if isinstance(elem, int):
                continue
            if (isinstance(elem, tuple) or isinstance(elem, str)) or isinstance(elem, list) or isinstance(elem, set):
                data.extend(elem)
                data.remove(elem)
            elif isinstance(elem, dict):
                data.extend(elem.items())
                data.remove(elem)
        for elem in data:
            flag = False
            if isinstance(elem, int):
                continue
            elif len(elem) != 1:
                flag = True
                break
    # Подсчитывает итоговую сумму
    for elem in data:
        if isinstance(elem, int):
            answer += elem
        else:
            answer += len(elem)
    # Возвращает итоговую сумму
    return answer


# Возвращает результаты работы функции
result = calculate_structure_sum(data_structure)
print(result)
