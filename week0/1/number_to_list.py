def number_to_list(n):
    list_from_numbers = []
    while n != 0:
        list_from_numbers.append(n % 10)
        n /= 10
    list_from_numbers.reverse()
    return list_from_numbers
print number_to_list((123024))
