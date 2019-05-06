animals = ['cat', 'dog', 'monkey']
for a in animals:
    print(a)

#IF you want access to the index of each element within the body of a loop use enumerate
#enums are constants
#%-style formatting: %s and %r call the Enum class’s __str__() and __repr__() respectively;
#other codes (such as %i or %h for IntEnum) treat the enum member as its mixed-in type.
    
for index, a in enumerate(animals):
    print('#%d: %s' % (index + 1, a))

    
#List comprehensions:
#used when we want to transform one type of data into another

nums = [0, 1, 2, 3, 4]

#option 1
print("Option 1")
squares = []
for x in nums:
    squares.append(x**2)
print(squares)

#option 2
print("Option 2")
squares2 = [x ** 2 for x in nums]
print(squares2)

#List comprehensions can also contain conditions:
print("With conditionals")

even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)

#Dictionaries
#a dictionary stores the key, value pairs

d = {'cat' : ' cute', 'dog' : 'furry'}
print(d['cat'])
print('cat' in d) #checks if dictionary has a given key
d['fish'] = 'wet' #add another entry
print(d)
print(d.get('fish', 'N/A'))# Get an element with a default; prints "wet"

#Loops in dictionaries
d2 = {'person' : 2, 'cat' : 4, 'spider':8}
for animal in d2:
    legs = d2[animal]
    print('A %s has %d legs' % (animal, legs))

#or using items
for animal, legs in d2.items():
    print('A %s has %d legs' % (animal, legs))

#Dictionary comprehensions:
#used when we want to transform one type of data into another
print("Dictionary comprehension")
nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)  # Prints "{0: 0, 2: 4, 4: 16}"



    
