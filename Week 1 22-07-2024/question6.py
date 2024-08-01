# Write a program to Reverse below given numbers without slicing

# Test Case 1:
# Input: 745633
# Output: 336547

# Test Case 2:
# Input: 65346
# Output: 64356

n = int(input("Enter the number: "))
num = ""
while n > 0:
    d = n % 10
    num += str(d)
    print(d)
    n //= 10
print(num)
