#numpy is used to perform operation faster on array

#declaration of array

import numpy as np

#simple declaration 
arr_name = np.array([0,1,2,3,4,5,6,7,8,9,10,11])
print(arr_name)

#multi-dimensional array declaration
arr_name_for_multidimensional = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
print(arr_name_for_multidimensional)

#declaring an array with same elements 0 of size(4,3)
arr_name_for_zeroes = np.zeros((4,3))
print(arr_name_for_zeroes)

#declaring an array with same elements 1 of size(4,3)
arr_name_for_ones = np.ones((4,3))
print(arr_name_for_ones)

#declaring an array with same elements of size(4,3)
arr_name_for_any_element = np.full((4,3),7)
print(arr_name_for_any_element)

#declaring an identity array of size 4
arr_name_identity = np.eye(4)
print(arr_name_identity)

#declaring an array using arange 
arr_name_arange_of_single_dimension = np.arange(12)
print(arr_name_arange_of_single_dimension)

#declaring an array using arange for multidimensional
arr_name_arange_of_mutli_dimension = np.arange(12).reshape(4,3)
print(arr_name_arange_of_mutli_dimension)

#declaring an array using random
arr_name_arange_using_random = np.random.rand(4,3) # elements will be [0,1]
print(arr_name_arange_using_random)

#declaring an array using random of element through-out the range
arr_name_arange_using_random_elements= np.random.randint(1,7,(4,3)) # elements will be [1,2,3,4,5,6]
print(arr_name_arange_using_random_elements)



