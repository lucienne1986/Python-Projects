#vector - a quantity that contains more than one piece of information.
#3d vectors have 3 components: velocity, force, acceleration
#a vector with only one piece of information, i.e. a 1d is called scalar

import numpy as np

L = [1, 2, 3]
A = np.array([1, 2, 3])


L2 = []
for e in L:
    L2.append(e + e)

print(L2)

#a plus sign with lists does concatenation
#but the plus sign in an array does vector addition
A = A + A
print(A)

print(2*A)

print("e * e")
L3 = []
for e in L:
    L3.append(e*e)

print(L3)

#summary
#if we do add, multiply, square ... use lists
#you can treat a list like an array with numbers
#you can treat an array like a vector - a mathematical object to do operations on lists
