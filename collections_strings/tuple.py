# tuple 
# Is immutable datatype in python.
'''Create a Python Tuple
We create a tuple by placing items inside parentheses ().

Tuple Characteristics:
Tuples are:
Ordered - They maintain the order of elements.
Immutable - They cannot be changed after creation.
Allow duplicates - They can contain duplicate values.

Access Tuple Items:
Each item in a tuple is associated with a number, known as a index.
The index always starts from 0, meaning the first item of a tuple is at index 0,
 the second item is at index 1, and so on.
 For example,
'''
numbers = (1, 2, -5)
print(numbers)
# Output: (1, 2, -5)

#Access Tuple Items:
languages = ('Python', 'Swift', 'C++')
# access the first item
print(languages[0])   # Python
# access the third item
print(languages[2])   # C++

#tuple examples codes:
t=( )#empty tuple
print(t)
t=(1, )# one element in tuple need with comma is must in syntax
print(t)
t=(1,5,7)# tuple is more than one elements with the comma
print(t)
#once the define a tuple's elements can't be altered OR manipulated.

'''Tuple Cannot be Modified:
Python tuples are immutable (unchangeable). We cannot add, change, or delete items of a tuple.
If we try to modify a tuple, we will get an error. For example,'''
cars = ('BMW', 'Tesla', 'Ford', 'Toyota')
# trying to modify a tuple
#cars[0] = 'Nissan'    # error      
#print(cars)


'''Iterate Through a Tuple
We use the for loop to iterate over the items of a tuple. For example,'''
fruits = ('apple','banana','orange')
# iterate through the tuple
for fruit in fruits:
    print(fruit)

#tuple methods functions:
tup =(1,4,9,1,6)
print(tup)
print(len(tup))

tup.count(1) #will return no of items 1 accure in tuple tup .
print(tup)

tup.index(9) # will return index of 9 where the element is located
print(tup)

