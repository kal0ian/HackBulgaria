def sum_matrix(m):
    sum = 0
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            sum += m[i][j]
    return sum
print (sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))
