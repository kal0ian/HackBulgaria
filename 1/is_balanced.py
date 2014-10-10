def is_number_balanced(n):
    midle = len(str(n)) // 2
    numbers_in_n = [int(x) for x in str(n)]
    first_part = numbers_in_n[:midle]
    second_part = numbers_in_n[-midle:]
    numbers_in_n = list(zip(first_part, second_part))
    sum_of_first_part = 0
    sum_of_second_part = 0
    for num1, num2 in numbers_in_n:
        sum_of_first_part += num1
        sum_of_second_part += num2
    return sum_of_first_part == sum_of_second_part
print (is_number_balanced(12340331))