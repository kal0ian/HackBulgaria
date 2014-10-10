def biggest_difference(arr):
    min = arr[0]
    max = arr[0]
    for i in arr:
        if i < min:
            min = i
        if i > max:
            max = i
    return min - max
print(biggest_difference([-10, -9, -1]))
