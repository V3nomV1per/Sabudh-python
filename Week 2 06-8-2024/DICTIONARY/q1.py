# Write a Python script to sort (ascending and descending) a dictionary by value.
import operator

dictionary = {"Ajax": 21, "Broly": 26, "Cindy": 33, "Devon": 25}
ascendingSort = dict(sorted(dictionary.items(), key=operator.itemgetter(1)))
descendingSort = dict(
    sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
)
print("Ascending order sort: " + str(ascendingSort))
print("Descending order sort: " + str(descendingSort))
