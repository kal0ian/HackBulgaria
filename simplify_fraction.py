def simplify_fraction(fraction):
    a = fraction[0]
    b = fraction[1]
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    fract = (fraction[0] / a, fraction[1] / a)
    return fract

#print (simplify_fraction((2, 6)))
