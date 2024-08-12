# Write a Python program to sum all the items in a dictionary.
# Write a Python program to multiply all the items in a dictionary.
dictionary = {1: 2, 3: 5, 7: 3}
sum = 0
product = 1
for key, value in dictionary.items():
    sum = sum + key + value
    product = product * key * value
print("Summation: " + str(sum))
print("Product: " + str(product))
