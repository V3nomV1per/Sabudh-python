# You have been given a string. You need to remove all the duplicates from the string. The final output string should contain each character only once. The respective order of the characters inside the string should remain the same. You can traverse the string only once.

# Test Case 1:
# Input: abaabbbacd
# Output: abcd

# Test Case 2:
# Input: ddeefggh
# Output: defgh

str = input("Enter the string: ")
mySet = set()
newStr = ""
for i in range(len(str)):
    if str[i] in mySet:
        continue
    else:
        mySet.add(str[i])
        newStr = newStr + str[i]
print(newStr)
