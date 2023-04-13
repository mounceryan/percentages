# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Defines 'arr' as a NumPy array from 1 to 5 incluive.
arr = np.array([1, 2, 3, 4, 5])

# Prints 'arr'.
print(arr)

# Prints the type of object.
print(type(arr))



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# This time we use a tuple to create the array.
arr = np.array((1, 2, 3, 4, 5))

# Prints 'arr'.
print(arr)



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# The below creates a 0-D array a.k.a. a Scalar.
arr = np.array(42)

# Prints 'arr'.
print(arr)



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# The below creates a 1-D array a.k.a. uni-dimensional array.
arr = np.array([1, 2, 3, 4, 5])

# Prints 'arr'.
print(arr)



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# The below creates a 2-D array.
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Prints 'arr'.
print(arr)



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# The below creates a 3-D array with two 2-D arrays.
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# Prints 'arr'.
print(arr)



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Various arrays are below:
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# 'ndim' returns an integer which tells us how many dimensions an array has.
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# The below creates an array. 'ndmin defines the number of dimensions.
arr = np.array([1, 2, 3, 4], ndmin=5)

# Prints 'arr'.
print(arr)

# Prints the number of dimensions in the array.
print('number of dimensions :', arr.ndim)