# A copy is a new array and a view is just a view of the original array.

# Changes to a copy of an array do not affect the original array and vice-versa.
# Changes to a view of an array do change the original array and vice-versa.

# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# The below creates an array.
arr = np.array([1, 2, 3, 4, 5])

# The value of x is a copy of the original array.
x = arr.copy()

# This changes the first element in the original array.
arr[0] = 42

# Prints the original array.
print(arr)

# Prints the copy of the original array.
print(x)



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# The below creates an array.
arr = np.array([1, 2, 3, 4, 5])

# The value of x is a view of the original array.
x = arr.view()

# This changes the first element in the original array.
arr[0] = 42

# Prints the original array.
print(arr)

# Prints the view array.
print(x)



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# The below creates an array.
arr = np.array([1, 2, 3, 4, 5])

# The value of x is a view of the original array.
x = arr.view()

# This changes the first element in the view array.
x[0] = 31

# Prints the original array.
print(arr)

# Prints the view array.
print(x)



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# The below creates an array.
arr = np.array([1, 2, 3, 4, 5])

# The value of x is a copy of the original array.
x = arr.copy()

# The value of y is a view of the original array.
y = arr.view()

# Prints whether x owns the data or not. So if it is base it is a copy, if it is none it is a view.
print(x.base)

# Prints whether y owns the data or not. So if it is base it is a copy, if it is none it is a view.
print(y.base)