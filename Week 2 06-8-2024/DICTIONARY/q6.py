# Write a Python program to sort a given dictionary by key.
import operator

dictionary = {"Broly": 26, "Ajax": 21, "Devon": 25, "Cindy": 33}
ascendingSort = dict(sorted(dictionary.items(), key=operator.itemgetter(0)))
print(ascendingSort)
