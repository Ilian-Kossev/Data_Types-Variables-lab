n = int(input())
for number in range(1, n + 1):
    digit_1 = number // 10
    digit_2 = number % 10
    result = digit_1 + digit_2
    if result == 5 or result == 7 or result == 11:
        special_number_found = True
    else:
        special_number_found = False
    print(f'{number} -> {special_number_found}')

