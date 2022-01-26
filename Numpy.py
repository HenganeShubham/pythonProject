'''import numpy as np

# Creating array object
arr = np.array([[1, 2, 3, 4],
                [4, 2, 5, 7],
                [7, 8, 9, 9]])

# Printing type of arr object
print("Array is of type: ", type(arr))

# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)

# Printing shape of array
print("Shape of array: ", arr.shape)

# Printing size (total number of elements) of array
print("Size of array: ", arr.size)

# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)
'''

import numpy as np

a = np.array([1, 2, 5, 3])

# add 1 to every element
print("Adding 1 to every element:", a + 1)

# subtract 3 from each element
print("Subtracting 3 from each element:", a - 3)

# multiply each element by 10
print("Multiplying each element by 10:", a * 10)

# square each element
print("Squaring each element:", a ** 2)

# modify existing array
a *= 2
print("Doubled each element of original array:", a)

# transpose of array
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])

print("\nOriginal array:\n", a)
print("Transpose of array:\n", a.T)










