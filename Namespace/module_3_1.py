calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(str_arg: str):
    count_calls()
    result = (len(str_arg), str_arg.upper(), str_arg.lower())
    return result


def is_contains(str_arg: str, list_arg: list):
    count_calls()
    str_arg = str_arg.lower()
    list_arg = [str(elem).lower() for elem in list_arg]
    if str_arg in list_arg:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
