import numpy as np

# Create a 1D Numpy array “a” containing 10 random integers between 0 and 99.
a = np.random.randint(100, size=10)
# Create a 2D Numpy array “b” of shape (3, 4) containing random integers between -10 and 10.
print("Array b: ")
b = np.random.randint(-10, 10, size=(3, 4))
# Reshape “b” into a 1D Numpy array “b_flat”.
b_flat = np.reshape(a=b, newshape=-1)
# Create a copy of “a” called “a_copy”, and set the first element of “a_copy” to -1.
a_copy = np.copy(a)
a_copy[0] = -1
# Create a 1D Numpy array “c” containing every second element of “a”.
print(a_copy)
c = a[1::2]
# Print the third element of “a”.
print("3rd element of a: ")
print(a[2])
# Print the last element of “b”.
print("Last element of b: ")
print(b[-1][-1])
# Print the first two rows and last two columns of “b”.
print("First row of b: ")
print(b[0])
print("Second row of b: ")
print(b[1])
print("Second last column of b: ")
print(b[:, -2])
print("Last column of b: ")
print(b[:, -1])
# Assign the second row of “b” to a variable called “b_row”.
b_row = b[2]
# Assign the first column of “b” to a variable called “b_col”.
b_col = b[:, 0]
# Create a 1D Numpy array “d” containing the integers from 1 to 10.
d = np.arange(1, 11)
# Add “a” and “d” element-wise to create a new Numpy array “e”.
e = np.add(a, d)
# Multiply “b” by 2 to create a new Numpy array “b_double”.
b_double = b * 2
# Calculate the dot product of “b” and “b_double” to create a new Numpy array “f”.
# f = np.dot(b, b_double)
# f = b @ b_double
# Calculate the mean of “a”,” b”, and “b_double” to create a new Numpy array “g”.
# g = np.mean(a, b, b_double)
# Find the sum of every element in “a” and assign it to a variable “a_sum”.
a_sum = np.sum(a)
print(a_sum)
# Find the minimum element in “b” and assign it to a variable “b_min”.
b_min = b[0][0]
for x in b:
    for i in x:
        if b_min > i:
            b_min = i
# Find the maximum element in “b_double” and assign it to a variable “b_double_max”.
b_double_max = b_double[0][0]
for x in b_double:
    for i in x:
        if b_double_max < i:
            b_double_max = i