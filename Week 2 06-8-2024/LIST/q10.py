# Write a Python program to print a specified list after removing the 3rd, 4th and 5th elements.
# There is a typo in the question, not 0th, it will be 3rd as in the example, 3rd to 5th element is absent
# ○ Sample List : [A, B, C, D, E, F]
# ○ Expected Output : [A, B, F]

size = int(input("Enter the size of list: "))
arr = list()
res = list()
largestOdd = 0
print("Enter values: ")
for i in range(0, size):
    # if i == 3 or i == 4 or i == 5:
    #     continue
    arr.append(input())
print("Given list: " + str(arr))
for i in range(0, size):
    if i >= 2 and i <= 4:
        continue
    res.append(arr[i])
print(str(res))
