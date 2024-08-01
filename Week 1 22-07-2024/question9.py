# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

# Test case 1
# input = 4
# output = 24

# Test case 2
# input = 2
# output = 2


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


num = int(input("Enter the number: "))
print(fact(num))
