# Write a Python program to find the median of three values.

# Test case 1
# Input:
# Input first number: 15
# Input second number: 26
# Input third number: 29
# Output : 26

# Test case 2
# Input:
# Input first number: 10
# Input second number: 20
# Input third number: 5
# Output : 10

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a < b < c or c < b < a:
    print(b)
elif a < c < b or b < c < a:
    print(c)
elif b < a < c or c < a < b:
    print(a)
