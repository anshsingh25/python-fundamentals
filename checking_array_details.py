#performing multiple operations on array to check its detail

import numpy as np
#declaring an arrays for checking array details and conversion 
arr_number_1 = np.array([[1, 2, 3],
              [4, 5, 6]])

#changing the shape of array
var_reshape = arr_number_1.reshape(3,2)
print(var_reshape)

#checking the shape of array in terms of (rows,columns)
arr_shape = arr_number_1.shape
print(arr_shape)

#checking the dimension of array 
arr_dim = arr_number_1.ndim
print(arr_dim)

#checking the size of array
arr_size = arr_number_1.size
print(arr_size)

#checking the datatype of array
arr_datatype = arr_number_1.dtype
print(arr_datatype)

#checking the item-size in an memory in terms of bytes
arr_item_size = arr_number_1.itemsize
print(arr_item_size)

#checking the array-soze of an array in terms of bytes
arr_array_size = arr_number_1.nbytes
print(arr_array_size)

#changing the datatype of array
arr_name = np.array([1, 2, 3], dtype=np.int32)
changing_arr_type = arr_name.astype(np.float64)
print(changing_arr_type)

