# Write a Python program to multiply all the items in a list.
# Write a Python program to get the largest number from a list.
# Write a Python program to get the smallest number from a list.
import random

num = random.sample(range(1, 50), 10)
print("The randomly generated list:" + str(num))

num.sort()
print("The list after sorting:" + str(num))

product = 1
for i in num:
    product *= i

print("Multiplying all the elements: " + str(product))
print("Largest number in list: " + str(num[9]))
print("Smallest number in list: " + str(num[0]))
