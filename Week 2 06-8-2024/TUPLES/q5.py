# Write a Python program to convert a tuple to a dictionary.
nameTuple = ("Ajax", "Broly", "Cindy", "Devon")
ageTuple = (21, 26, 33, 25)
dictionary = {}
for i in range(0, 4):
    dictionary[nameTuple[i]] = ageTuple[i]
print("Tuple of names: " + str(nameTuple))
print("Tuple of age: " + str(ageTuple))
print("Dictionary generated from the two tuples: " + str(dictionary))
