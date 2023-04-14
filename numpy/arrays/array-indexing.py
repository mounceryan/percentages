# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Defines 'arr' as a NumPy array from 1 to 4 incluive.
arr = np.array([1, 2, 3, 4])

# Gets the first element from the array.
print(arr[0])



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Defines 'arr' as a NumPy array from 1 to 4 incluive.
arr = np.array([1, 2, 3, 4])

# Gets the second element from the array.
print(arr[1])



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Defines 'arr' as a NumPy array from 1 to 4 incluive.
arr = np.array([1, 2, 3, 4])

# Gets the third and fourth elemente from the array and adds them together.
print(arr[2] + arr[3])



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# The below creates a 2-D array.
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# Prints the element on the first row/second column.
print('2nd element on 1st row: ', arr[0, 1])



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# The below creates a 2-D array.
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# Prints the element on the second row/fifth column.
print('5th element on 2nd row: ', arr[1, 4])



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# The below creates a 3-D array.
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# This gets the third element of the second array of the first array.
# The first number represents the first dimension, as it is 0 it selects the first array.
# The second number represents the second dimension, as it is 1 it selects the second array.
# The third number represents the third dimension, as it is 2 it selects the thid value which is 6.
print(arr[0, 1, 2])



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# The below creates a 2-D array.
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# This gets the last element of the second array.
print('Last element from 2nd dim: ', arr[1, -1])