def count_vowels(str):
    count = 0
    str=str.lower()
    count += str.count("a", 0, len(str))
    count += str.count("e", 0, len(str))
    count += str.count("i", 0, len(str))
    count += str.count("u", 0, len(str))
    count += str.count("o", 0, len(str))
    count += str.count("y", 0, len(str))
    return count
print (count_vowels("A nice day to code!"))
