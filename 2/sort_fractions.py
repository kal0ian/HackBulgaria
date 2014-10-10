from simplify_fraction import simplify_fraction


def sort_fractions(fractions):
    sorted_fractions = []
    for i in fractions:
        sorted_fractions.append(simplify_fraction(i))
    sorted_fractions.sort()
    return sorted_fractions
print (sort_fractions([(2, 3), (1, 2), (1, 3)]))
