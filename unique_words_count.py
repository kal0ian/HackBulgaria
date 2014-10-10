def unique_words_count(arr):
    dictionary = {}
    count = 0
    for item in arr:
        if item not in dictionary:
            dictionary[item] = 1
            count += 1
    return count
print (unique_words_count(["apple", "banana", "apple", "pie"]))
