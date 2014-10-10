def zero_insert(n):
    list_numbers = []
    new_list_numbers = []
    while n != 0:
        list_numbers.append(n % 10)
        n /= 10
    list_numbers.reverse()
    for i in range(0, len(list_numbers) - 1):
        if (list_numbers[i] == list_numbers[i + 1]) or ((list_numbers[i] + list_numbers[i + 1]) % 10 == 0):
            new_list_numbers.append(list_numbers[i])
            new_list_numbers.append(0)

        else:
            new_list_numbers.append(list_numbers[i])
    new_list_numbers.append(list_numbers[i + 1])
    return new_list_numbers


print(zero_insert(555))
