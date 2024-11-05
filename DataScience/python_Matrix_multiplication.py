import numpy as np

#create a matrix
A = np.array([[1, 2], [3, 4]])

#create an inverse
AInv = np.linalg.inv(A)
print(AInv)

#find the matrix determinant
ADet = np.linalg.det(A)
print(ADet)

#return the diagonal elements in a vector
ADia =  np.diag(A)
print(ADia)
#return the diagonal elements in a 2d array
ADia2 = np.diag([1,2])
print(ADia2)

#****INNER AND OUTER PRODUCTS ***********#
#create 2 vectors
c = np.array([1,2])
d = np.array([3,4])

#finding the outer product
print(np.outer(c,d))

#finding the inner product
print(np.inner(c,d))
#or also called the dot product
print(c.dot(d))

#*** MATRIX TRACE ***********#
#This is the sum of the diagonals of the matrix
print(np.trace(A))







