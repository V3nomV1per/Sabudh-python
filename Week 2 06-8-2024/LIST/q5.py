# Write a Python program to remove duplicates from a list.
n = int(input("Enter size of list: "))
arr = list()
numset = set()
print("Enter values: ")
for i in range(0, n):
    arr.append(int(input()))
print("Given list: " + str(arr))
for i in arr:
    numset.add(i)
arr = list(numset)
print("List after removing duplicates: " + str(arr))
