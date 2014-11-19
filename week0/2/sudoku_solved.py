def check(buf):
    sum = 0
    if buf.count(1) == 1 and buf.count(2) == 1 and buf.count(3) == 1 and buf.count(4) == 1 and buf.count(5) == 1 and buf.count(6) == 1 and buf.count(7) == 1 and buf.count(8) == 1 and buf.count(9) == 1:
        return True
    else:
        return False


def sudoku_solved(sudoku):
    buf = []
    for i in range(0, 9):
        for j in range(0, 9):
            buf.append(sudoku[i][j])
        if check(buf) == False:
            return False
        else:
            buf = []

    for i in range(0, 9):
        for j in range(0, 9):
            buf.append(sudoku[j][i])
        if check(buf) == False:
            return False
        else:
            buf = []

    for i in range(0, 3):
        for j in range(0, 3):
            buf.append(sudoku[i][j])
    if check(buf) == False:
        return False
    else:
        buf = []

    for i in range(0, 3):
        for j in range(3, 6):
            buf.append(sudoku[i][j])
    if check(buf) == False:
        return False
    else:
        buf = []

    for i in range(0, 3):
        for j in range(6, 9):
            buf.append(sudoku[i][j])
    if check(buf) == False:
        return False
    else:
        buf = []

    for i in range(3, 6):
        for j in range(0, 3):
            buf.append(sudoku[i][j])
    if check(buf) == False:
        return False
    else:
        buf = []

    for i in range(3, 6):
        for j in range(3, 6):
            buf.append(sudoku[i][j])
    if check(buf) == False:
        return False
    else:
        buf = []

    for i in range(3, 6):
        for j in range(6, 9):
            buf.append(sudoku[i][j])
    if check(buf) == False:
        return False
    else:
        buf = []

    for i in range(6, 9):
        for j in range(0, 3):
            buf.append(sudoku[i][j])
    if check(buf) == False:
        return False
    else:
        buf = []

    for i in range(6, 9):
        for j in range(3, 6):
            buf.append(sudoku[i][j])
    if check(buf) == False:
        return False
    else:
        buf = []

    for i in range(6, 9):
        for j in range(6, 9):
            buf.append(sudoku[i][j])
    if check(buf) == False:
        return False
    else:
        buf = []
    return True
# print (sudoku_solved([
#     [4, 5, 2, 3, 8, 9, 7, 1, 6],
#     [3, 8, 7, 4, 6, 1, 2, 9, 5],
#     [6, 1, 9, 2, 5, 7, 3, 4, 8],
#     [9, 3, 5, 1, 2, 6, 8, 7, 4],
#     [7, 6, 4, 9, 3, 8, 5, 2, 1],
#     [1, 2, 8, 5, 7, 4, 6, 3, 9],
#     [5, 7, 1, 8, 9, 2, 4, 6, 3],
#     [8, 9, 6, 7, 4, 3, 1, 5, 2],
#     [2, 4, 3, 6, 1, 5, 9, 8, 7]
# ]))
