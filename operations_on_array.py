#performing multiple operations on array

import numpy as np
#declaring 2 arrays for operations
arr_number_1 = np.array([[1, 2, 3],
                         [4, 5, 6]])

arr_number_2 = np.array([10, 20, 30])

#Arithmetic operations using symbols
print(arr_number_1 + arr_number_2)
print(arr_number_1 - arr_number_2)
print(arr_number_1 * arr_number_2)
print(arr_number_1 ** 2)
print(arr_number_1 * 10)
print(arr_number_1 / arr_number_2)

#Arithmetic operations using functions
print("addition of all elements :",arr_number_1.sum())
print("addition of elements row wise :",arr_number_1.sum(axis=1))
print("addition of elements column wise :",arr_number_1.sum(axis=0))
