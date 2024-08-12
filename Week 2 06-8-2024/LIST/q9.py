# Write a Python program to find the largest odd number in a given list of integers.

# ○ Sample Data:
# ([0, 9, 2, 4, 5, 6]) -> 9
# ([-4, 0, 6, 1, 0, 2]) -> 1
# ([1, 2, 3])           -> 3
# ([-4, 0, 5, 1, 0, 1]) -> 5

size = int(input("Enter the size of list: "))
arr = list()
largestOdd = 0
print("Enter values: ")
for i in range(0, size):
    arr.append(int(input()))
print("Given list: " + str(arr))
arr.sort()
for i in range(size - 1, -1, -1):
    if arr[i] % 2 != 0:
        largestOdd = arr[i]
        break
print("Largest odd: " + str(largestOdd))
