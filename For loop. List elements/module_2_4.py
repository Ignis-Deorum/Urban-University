# Решение с использованием переменной is_prime:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = None

for number in numbers:
    if number == 1:
        continue
    for divider in range(2, number + 1):
        remainder = number % divider
        if divider != number and remainder == 0:
            is_prime = False
            break
        elif divider == number and remainder == 0:
            is_prime = True
            break
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')

# Более элегантное решение без использования переменной is_prime:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for number in numbers:
    for divider in range(2, number + 1):
        remainder = number % divider
        if number == 1:
            break
        elif divider != number and remainder == 0:
            not_primes.append(number)
            break
        elif divider == number and remainder == 0:
            primes.append(number)
            break

print(f'\nPrimes: {primes}')
print(f'Not Primes: {not_primes}')