import numpy as np

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([[10, 20], [30, 40]])

arr3 = np.zeros((2, 3))

arr4 = np.arange(0, 10, 2)

print(arr1.shape, arr1.ndim, arr1.dtype, arr1.size)
print(arr2.shape, arr2.ndim, arr2.dtype, arr2.size)
print(arr3, arr3.ndim, arr3.dtype, arr3.size)
print(arr4, arr4.ndim, arr4.dtype, arr4.size)

print(arr1 * 2)
print(np.mean(arr1))

print(arr2 * 2)
print(np.mean(arr2))

print(arr1[arr1 > 20])
print(arr2[arr2 > 20])

arr5 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr5 + 10)

print(arr5 - np.mean(arr5))