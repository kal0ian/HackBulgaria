def iterations_of_nan_expand(expanded):
    expand = expanded.split()
    count = 0
    for i in range(len(expand) - 2):
        if expand[i] != "Not" and expand[i + 1] != "a":
            return False
        if expand[-1] != "NaN":
            return False
    for i in range(0,len(expand)):
        if expand[i] == "Not":
            count += 1
    return count

print (iterations_of_nan_expand("Not a NaN"))
