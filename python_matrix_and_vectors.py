#A matrix is that it is a 2d array or a list of lists
#you can use a list of lists to initialize a matrix
import numpy as np

#USING numpy array
M = np.array([[1, 2],[3, 4]]) #having two arrays of the same size
#gets the first element of the first row
print(M[0][0]) #prints 1
#or
print(M[0,0]) #prints 1

#USING numpy matrix BUT it is not ideal to use matrix, convert to array if you find one
M2 = np.matrix([[1, 2],[3, 4]])
print(M2)
#convert to array
A = np.array(M2)
print(A.T) #A.T gives us the transpose of A

#USING list of lists
L = [[1, 2], [3, 4]]
#get the first row
print(L[0]) #prints [1,2]
#get the first element of row 1
print(L[0][0]) #prints 1

#summary:
#A matrix is really just a 2d numpy array. Contains numbers.
#Vector is 1d numpy array. Contains numbers.
#Hence, a matrix is like a 2d vector

