#dotproducts are type of multiplication you can perform on vectors
#there are two definitions of the dotproduct:
#1. Summation of the element wise multiplication of the two vectors
#2. Magnitude of a * the magnitude of B * the cosine of the angle between A and B
#Usually we use cosine to find the angle itself by equating the two methods

import numpy as np
#create two vectors
a = np.array([1, 2])
b = np.array([2, 1])

#if we use the direct definition of the dot product you'd want to loop through both arrays
#simaltaneously * each corresponding element together and + to the final sum

dot = 0
for e, f in zip(a, b):
    dot = dot + (e*f)

print(dot)

#or

mult = a*b
sumAB = np.sum(mult)
print(sumAB)

#or
print((a*b).sum())

#using the dotproduct function
#like the sum(), the dot() is part of the numpy and can call on the object itself
print("using the dotproduct function")
dotProd = np.dot(a, b)
print(dotProd)

#use the alternative definition of the dotproduct to calculate the angle between A and B
#Step 1: find how to calculate the length of a vector, it's the sqrt of the sum of each element squared
#amag = a magnitude
amag = np.sqrt((a*a).sum())
print(amag)

#or we can use the linear algebra in numpy
amaglin = np.linalg.norm(a)
print(amaglin)

#then.. we find the angle
cosangle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
angle = np.arccos(cosangle)
print("The angle in radians is", angle)









