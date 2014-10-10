def next_hack(n):
    number = n + 1
    flag = True

    while flag == True:
        buf = number
        binary = []
        reversed_binary = []
        while number != 0:
            binary.append(number % 2)
            number /= 2
        binary.reverse()

        for i in binary:
            reversed_binary.append(i)
        reversed_binary.reverse()
        print(binary)
        print(reversed_binary)
        if cmp(binary, reversed_binary) == 0 and binary[0] == 1:
            flag = False
        number = buf+1
    return buf
print (next_hack(8031))
