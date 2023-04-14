# Python has the following data types:
    # strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
    # integer - used to represent integer numbers. e.g. -1, -2, -3
    # float - used to represent real numbers. e.g. 1.2, 42.42
    # boolean - used to represent True or False.
    # complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j

# NumPy has some extra data types and refers to data types with one character:
    # i - integer
    # b - boolean
    # u - unsigned integer
    # f - float
    # c - complex float
    # m - timedelta
    # M - datetime
    # O - object
    # S - string
    # U - unicode string
    # V - fixed chunk of memory for other type ( void )



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Creates an array.
arr = np.array([1, 2, 3, 4])

# Prints the data type of the array.
print(arr.dtype)



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Creates an array with the data type 'S' which means string.
arr = np.array([1, 2, 3, 4], dtype='S')

# Prints the array.
print(arr)

# Prints the data type of the array.
print(arr.dtype)



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Creates an array with the data type 'i' which means integer. With i, u, f, s and U data types we can define the size in bytes as well.
arr = np.array([1, 2, 3, 4], dtype='i4')

# Prints the array.
print(arr)

# Prints the data type of the array.
print(arr.dtype)



# Imports the NumPy Python library using the alias 'np'.
#import numpy as np

# Creates an array which will return an error as the data type is integer, but it has a string in it.
#arr = np.array(['a', '2', '3'], dtype='i')



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Creates an array.
arr = np.array([1.1, 2.1, 3.1])

# Creates a new array by changing the data type of the old array from float to integer.
newarr = arr.astype('i')

# Prints the array.
print(newarr)

# Prints the data type of the array.
print(newarr.dtype)




# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Creates an array.
arr = np.array([1.1, 2.1, 3.1])

# Creates a new array by changing the data type of the old array from float to integer, this time by using 'int' rather than 'i'.
newarr = arr.astype(int)

# Prints the array.
print(newarr)

# Prints the data type of the array.
print(newarr.dtype)



# Imports the NumPy Python library using the alias 'np'.
import numpy as np

# Creates an array.
arr = np.array([1, 0, 3])

# Creates a new array by changing the data type of the old array to boolean
newarr = arr.astype(bool)

# Prints the array.
print(newarr)

# Prints the data type of the array.
print(newarr.dtype)