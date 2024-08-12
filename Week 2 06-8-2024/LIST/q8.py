#     Write a Python program to extract specified number of elements from a given list, which follows each other continuously.

# ○ Original list:  [1, 1, 3, 4, 4, 5, 6, 7]
# ○ Output: [1, 4]
# ○ Original list: [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
# ○ Output: [4]

size = int(input("Enter the size of list: "))
arr = list()
numset = set()
print("Enter values: ")
for i in range(0, size):
    arr.append(int(input()))
print("Given list: " + str(arr))
for i in range(1, size):
    if arr[i - 1] == arr[i]:
        numset.add(arr[i])
result = list(numset)
print("Result: " + str(result))
