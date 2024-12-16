import numpy as np

arr1 = np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))   #1 dimentional array as it has only 1 list braces
print(arr1.shape)

arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2)
print(arr2.shape)
print(type(arr2))   #2 dimentional array as it has 2 list braces and if it has nested lists it will consider them as rows defaultly

arr3 = np.array([[2,3,4,5,6]])
print(arr3)
print(arr3.shape)
print(type(arr3))   #2 dimentional array as it has 2 list braces

arr4 = arr3.reshape(5,1)
print(arr4)

arr5 = np.arange(0,10)
print(arr5)

arr6 = np.arange(0, 10, 2).reshape(5,1)
print(arr6)

arr7 = np.ones((3,4))
print(arr7)
print(type(arr7))

arr8 = np.eye(3,3)
print(arr8)
print(type(arr8))


# Attributes of Numpy Array

arr = np.array([[1,2,3,4,5], [2,3,4,5,6]])

print("Array is: \n", arr)
print("Shape:", arr.shape)
print("No of Dimentions: ", arr.ndim)
print("Size: ",arr.size)
print("Data Type: ", arr.dtype)
print("Item size(in bytes): ", arr.itemsize)


#Numpy Vectorized Operations

arr9 = np.array([1,2,3,4,5])
arr10 = np.array([10,20,30,40,50])

print("Addition : ",arr9 + arr10)
print("Subtraction : ",arr9 - arr10)
print("Multiplication: ", arr9 * arr10)
print("Division: ", arr9 / arr10)

# Univeral Operations

print("Square Root: ",np.sqrt(arr10))
print("Exponential: ", np.exp(arr10))
print("Natural log: ", np.log(arr10))
print("Sine: ", np.sin(arr10))


#Slicing and Indexing in Numpy Array

arr11 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print("Array: \n ",arr11)
print("Only 1st row: ", arr11[0])
print("Only 1st Column: ", arr11[:,0])
print("Printing only the 1st & 2nd rows and from 4th column to last column: \n", arr11[0:2, 3:])
print("Printing from the 2nd row to last row and 2nd & 3rd column: \n", arr11[1: , 1:3])

arr11[0,0] = 100    # Changing the 1st row 1st column's element to 100
print(arr11)
