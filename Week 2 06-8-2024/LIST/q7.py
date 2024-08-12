# Write a Python program to count the lowercase letters in a given list of word
arr = ["liKe", "ShAre", "ComMent", "SunsCRibe"]
lowerCaseCount = 0
for word in arr:
    for i in range(0, len(word)):
        if ord(word[i]) >= 65 and ord(word[i]) <= 90:
            continue
        else:
            lowerCaseCount += 1
print("Lowercase alphabet count: " + str(lowerCaseCount))
