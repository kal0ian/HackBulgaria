def list_to_number(digits):
    number = 0
    for i in digits:
        number *= 10
        number += i
    return number
print (list_to_number([1, 2, 3, 0, 2, 3]))
