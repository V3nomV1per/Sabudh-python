# Write a Python script to merge two Python dictionaries.
dictionary1 = {"Ajax": 21, "Broly": 26, "Cindy": 33, "Devon": 25}
dictionary2 = {"Walter": 27, "Xebec": 37, "Yemba": 29, "Zico": 20}
resultDictionary = dictionary1.copy()
resultDictionary.update(dictionary2)
print(str(resultDictionary))
