def prepare_meal(x):
    egg = ''
    while x != 1:
        if x % 3 != 0:
            return ''
        else:
            x /= 3
            egg = egg + 'spam '
        if x == 5:
            egg = egg + 'and eggs'
            x /= 5
    return egg
print(prepare_meal(15))
