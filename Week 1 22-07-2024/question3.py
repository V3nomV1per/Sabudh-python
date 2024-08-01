# Write a program to display only those numbers from a list that satisfy the following conditions
#     The number must be divisible by five
#     If the number is greater than 150, then skip it and move to the next number
#     If the number is greater than 500, then stop the loop

# Test Case 1:
# Input : 12, 75, 150, 180, 145, 525, 50
# Output : [75, 150, 145]

# Test Case 2:
# Input : 14, 85, 625, 75
# Output : [85]

n = int(input("Enter the size of array: "))
print("Enter the numbers: ")
arr = []
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
newArr = []
for i in range(0, n):
    if arr[i] > 500:
        break
    elif arr[i] > 150:
        continue
    elif arr[i] % 5 == 0:
        newArr.append(arr[i])
print(newArr)
