# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Creates an array.
arr = np.array([1, 2, 3])

# Iterates through each element in the array.
for x in arr:
  # Prints each element as it iterates through them.
  print(x)



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Creates a 2-D array.
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Iterates through each 1-D array in the 2-D array. If we iterate on a n-D array it will go through n-1th dimension one by one.
for x in arr:
  # Prints each array as it iterates through them.
  print(x)



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Creates a 2-D array.
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Iterates through each 1-D array in the 2-D array.
for x in arr:
  # Iterates through each element in the 1-D arrays.
  for y in x:
    # Prints each element as it iterates through them.
    print(y)



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Creates a 3-D array.
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Iterates through each 2-D array in the 3-D array.
for x in arr:
  # Prints each 2-D array as it iterates through them.
  print(x)



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Creates a 3-D array.
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Iterates through each 2-D array in the 3-D array.
for x in arr:
  # Iterates through each 1-D array in the 2-D array.
  for y in x:
    # Iterates through each element in the 1-D arrays.
    for z in y:
      # Prints each element as it iterates through them.
      print(z)