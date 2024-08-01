# Define a function which counts vowels and consonants in a word.

# Test case 1
# Input : pythonlobby
# Output :
# vowel : 2
# Consonants: 9

# Test case:2
# Input : sabudhfoundation
# Output :
# vowel : 7
# Constants: 9


def counter(s):
    vcount = 0
    ccount = 0
    vowels = {"a", "e", "i", "o", "u"}
    for i in range(0, len(s)):
        if s[i] in vowels:
            vcount += 1
        else:
            ccount += 1
    print("Vowels: " + str(vcount))
    print("Consonants: " + str(ccount))


s = input("Enter the string: ")
counter(s)
