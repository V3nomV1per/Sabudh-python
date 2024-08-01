# Write a program to count the total number of digits in a number using a while loop

# Test Case 1:
# Input: 75869
# Output: 5

# Test Case 2:
# Input: 654
# Output: 3

n = int(input("Enter the number: "))
counter = 0
while n > 0:
    n //= 10
    counter += 1
print(counter)
