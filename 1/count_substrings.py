def count_substrings(haystack, needle):
    return haystack.count(needle, 0, len(haystack))
print (count_substrings("Python is an awesome language to program in!", "o"))
