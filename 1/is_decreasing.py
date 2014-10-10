def is_decreasing(seq):
    for i in range(0, len(seq) - 1):
        if seq[i] <= seq[i + 1]:
            return False
    return True
print (is_decreasing([3, 5, 1]))
