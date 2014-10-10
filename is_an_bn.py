def is_an_bn(word):
    count = 0
    if word[0] != 'a':
        return False
    for i in range(0, len(word)):
        if word[i] == 'a':
            count += 1
        else:
            break
    i = len(word) - 1
    while i != 0:
        if word[i] == 'b':
            count -= 1
            i -= 1
        else:
            break
    if count != 0:
        return False
    return True
print (is_an_bn("psabb"))
