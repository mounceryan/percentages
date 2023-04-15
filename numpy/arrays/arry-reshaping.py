# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# The below is a new array.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# 'newarr' is a reshaped version of 'arr'. It converts the original 1-D array into a 2-D array consisting of 4 arrays each with 3 elements.
newarr = arr.reshape(4, 3)

# Prints 'newarr'.
print(newarr)



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# The below is a new array.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# This reshapes the array to be a 3-D array consisting of 2 arrays with 3 arrays in each of them and 2 elements in both of those.
newarr = arr.reshape(2, 3, 2)

# Prints 'newarr'.
print(newarr)



# Imports the NumPy Python library using the alias 'np'.
#import numpy as np

# The below is a new array.
#arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# The below will not work as we cannot create a 3 by 3 array from a 1 by 8 array.
#newarr = arr.reshape(3, 3)

# Prints 'newarr'.
#print(newarr)



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# The below is a new array.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Prints whether the reshaped array is a copy or a view. This example returns the original array so it is a view.
print(arr.reshape(2, 4).base)



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# The below is a new array.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Creates a 3-D array consisting of 2 arrays with 2 arrys in each of them. You do not need to specify the exact number for one of the dimensions, hence the '-1'.
newarr = arr.reshape(2, 2, -1)

# Prints 'newarr'.
print(newarr)



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# The below is a 2-D array.
arr = np.array([[1, 2, 3], [4, 5, 6]])

# This reshapes the 2-D array to a 1-D array. Changing it into a 1-D array is called flattening the array. 
newarr = arr.reshape(-1)

# Prints 'newarr'.
print(newarr)