def count_consonants(str):
    count = 0
    consonants = "bcdfghjklmnpqrstvwxz"
    str = str.lower()
    for i in range(0, len(consonants)):
        for j in range(0, len(str)):
            if consonants[i] == str[j]:
                count += 1
    return count
print (count_consonants("Theistareykjarbunga"))
