# Write a program to Use a loop to display elements from a given list present at odd index position

# Test Case 1:
# Input: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
# Output: [20, 40, 60, 80, 100]

# Test Case 2:
# Input: 23, 46, 69, 92, 115
# Output: [46, 92]

n = int(input("Enter the size of array: "))
print("Enter the numbers: ")
arr = []
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
oddArr = []
for i in range(1, n, 2):
    oddArr.append(arr[i])
print(oddArr)
