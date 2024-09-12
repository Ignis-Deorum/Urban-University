# Эта функция принимает аргумент целое число "number" и подсчитывает произведение ненулевых цифр этого числа.
# This function takes an integer argument "number" and calculates the product of the non-zero digits of that number.
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    str_number = str_number[1:]
    if len(str_number) == 0:
        return first
    else:
        return first * get_multiplied_digits(int(str_number))


# Проверка корректности работы функции
# Checking whether the function is working correctly
result1 = get_multiplied_digits(40203)
result2 = get_multiplied_digits(22222222)
result3 = get_multiplied_digits(345)
print(result1)
print(result2)
print(result3)