import numpy as np

#generate an array of all zeros
Z = np.zeros(10)
print(Z) #outputs a vector of 10 with all zeros

#create a matrix of size 10 X 10 of all zeros
ZMat = np.zeros((10,10)) #having a tuple containing each dimension
print(ZMat)

#create a matrix of size 10 X 10 of all ones
OMat = np.ones((10,10))
print(OMat)

#create a matrix of size 10 X 10 of all random numbers
RMat = np.random.random((10,10))
print(RMat) #returns distributed random numbers between 0 and 1

#returns a matrix with Gaussian distributed random numbers
GMat = np.random.randn(10,10)
print(GMat) #returns gaussian distribution with mean 0 and variance 1

#return the mean
print(GMat.mean())

#return the variance
print(GMat.var())
