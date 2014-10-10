def magic_square(matrix):
    check = []
    sum = 0
    for i in range(len(matrix)):  # redove
        for j in range(len(matrix[i])):  # koloni
            sum += matrix[i][j]
        check.append(sum)
        sum = 0


    for j in range(len(matrix)):  # redove
        for i in range(len(matrix[i])):  # koloni
            sum += matrix[i][j]
        check.append(sum)
        sum = 0

    for i in range(len(matrix)):
    	sum+=matrix[i][i]
    check.append(sum)
    sum = 0

    sum+=matrix[0][2]
    sum+=matrix[1][1]
    sum+=matrix[2][0]
    check.append(sum)
    sum = 0

    for i in range(len(check)-1):
    	if check[i]!=check[i+1]:
    		return False
    return True
print (magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
