n = int(input())

for number in range(1, n + 1):
    special_number_found = False
    number_to_string = str(number)
    result = 0
    for symbol in number_to_string:
        value = int(symbol)
        result += value
        if result == 5 or result == 7 or result == 11:
            special_number_found = True
    print(f'{number} -> {special_number_found}')


