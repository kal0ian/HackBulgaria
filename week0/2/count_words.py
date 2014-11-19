def count_words(arr):
    dictionary = {}
    for item in arr:
        if item not in dictionary:
            dictionary[item] = 1
        else:
            dictionary[item] = dictionary[item] + 1
    return dictionary
#print (count_words(["python", "python"]))
