# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.


def lastele(tup):
    return tup[-1]


def sort(tuplist):
    return sorted(tuplist, key=lastele)


tuplist = [(1, 3), (2, 2), (3, 1)]
print("Sorted in increasing order by the last element")
print(sort(tuplist))
