import numpy as np
import pandas as pd
import random

##data types and atributes

a1 = np.array([1, 2, 3])

a2 = np.array([[1, 2.0, 3.0], [4, 5, 6.0]])


a3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])

print(a1)
print(a2)
print(a3)

print(a1.ndim)
print(a2.ndim)
print(a3.ndim)

print(a1.shape)
print(a2.shape)
print(a3.shape)

print(a1.size)
print(a2.size)
print(a3.size)

df = pd.DataFrame(a2)
print(df)

# creating arrays
ones = np.ones((2, 3))
print(ones)

zeros = np.zeros((2, 3))
print(zeros)


random_array = np.random.randint(0, 10, size=(3, 5))
print(random_array)

range_array = np.arange(0, 10, 2)
print(range_array)

random_array2 = np.random.random((5, 3))
print(random_array2)

#pseudorandom numbers
np.random.seed(0)
random_array3 = np.random.random((5, 3))
print(random_array3)


#viewing arrays

print(np.unique(zeros))

#manipulating and comparing arrays


arithmetic_array = np.array([1, 2, 3, 4, 5])
added_array = arithmetic_array + 5
print(added_array)

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

sum_array = array1 + array2
print(sum_array)

#reshaping arrays
array3 = np.array([[[1, 2, 3]], [[1, 2, 3]], [[1,2,3]]])
print(array3)

array4 = array3 * a3

print(array4)

#aggregation
print(np.sum(array1))

print(array3.shape)
print(array3)
print(array3.reshape(3, 3))
print(array3.reshape(3, 3, 1))

#dot product
array5 = np.random.randint(0, 10, size=(2, 3))
array6 = np.random.randint(0, 10, size=(3, 2))
dot_product = np.dot(array5, array6)
print(dot_product)