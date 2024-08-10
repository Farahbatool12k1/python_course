'''Python String Operations:
Many operations can be performed with strings, which makes 
it one of the most used data types in Python.'''

1#. Compare Two Strings
'''We use the == operator to compare two strings. If two strings are equal, the operator returns True. 
Otherwise, it returns False. For example,'''

str1 = "Hello, world!"
str2 = "I love Swift."
str3 = "Hello, world!"

# compare str1 and str2
print(str1 == str2)

# compare str1 and str3
print(str1 == str3)

#2. Join Two or More Strings
'''In Python, we can join (concatenate) two or more strings using the + operator. 
example code'''
greet = "Hello, "
name = "ali"

# using + operator
result = greet + name
print(result)

#Iterate Through a Python String
'''We can iterate through a string using a for loop. For example,'''
greet = 'Hello'

# iterating through greet string
for letter in greet:
    print(letter)

#Python String Length
'''In Python, we use the len() method to find the length of a string. For example,
'''
greet = 'Hello'

# count length of greet string
print(len(greet))

'''String Membership Test:
We can test if a substring exists within a string or not, using the keyword in.
'''
print('a' in 'program') # True
print('at' not in 'battle') # False
