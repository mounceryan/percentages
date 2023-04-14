# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Defines 'arr' as a NumPy array from 1 to 7 incluive.
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Slices the array from the second value to the fifth value inclusive. The result includes the start index, but excludes the end index.
print(arr[1:5])



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Defines 'arr' as a NumPy array from 1 to 7 incluive.
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Slices the array from the fifth value to the end value inclusive.
print(arr[4:])



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Defines 'arr' as a NumPy array from 1 to 7 incluive.
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Slices the array from the beginning value to the fourth value inclusive. The 4th index is not included.
print(arr[:4])


# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Defines 'arr' as a NumPy array from 1 to 7 incluive.
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# This slices the array from the second to last value to the third from last value inclusive.
print(arr[-3:-1])



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Defines 'arr' as a NumPy array from 1 to 7 incluive.
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Slices the array between the second and fourth values. However, every other value is missed out.
print(arr[1:5:2])



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Defines 'arr' as a NumPy array from 1 to 7 incluive.
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# This returns every other value in the array.
print(arr[::2])



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Creates a 2-D array.
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# Prints the second to fourth values in the second array.
print(arr[1, 1:4])



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Creates a 2-D array.
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

#Prints the third values from both elements. Note that we have to put 0:2 to include both the first (index 0) and second (index 1) elements.
print(arr[0:2, 2])



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Creates a 2-D array.
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])