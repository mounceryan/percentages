# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# The below creates a 2-D array.
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# The below prints the shape of the array. This exmaple is where the first dimension has 2 elements and the second dimension has 4 elements.
print(arr.shape)



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# This creates and array with 5 dimensions.
arr = np.array([1, 2, 3, 4], ndmin=5)

# Prints the array.
print(arr)

# The below prints the shape of the array. It verifies the last dimension has four elements.
print('shape of array :', arr.shape)