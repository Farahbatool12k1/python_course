'''string in python can be sliced for getting a part of the string.
syntax:
sl=name[ind_start:ind_end]
sl: is sliced symbol
ind:means index given
start index and ending index
example code:'''
name="ali"
print(len(name))
sl=name[0:2]
print(sl)
name="ali hi"
sl=name[0:6]
print(sl)

'''slicing with skip values:
slicing with skip values that jump to one character to other of give limit.
example code'''
# create string type variables
message = "I love Python."
print(message)
sl=message[1:5:2]
print(sl)
sl=message[ :6] #starting to ending limited that print "i love " only 6 characters
print(sl)
sl=message[4:] #starting to starting limited that print "ve python. " start to 4 character to ending.
print(sl)

'''string immutable :
In Python, strings are immutable. That means the characters of a string cannot be changed. example code:
'''
message = 'Hola Amigos'
print(message[0])

message[0] = 'H'
print(message)

'''Python Multiline String:
We can also create a multiline string in Python. For this, we use triple double quotes """
 or triple single quotes .For example,'''
 # multiline string 
message = """
Never gonna give you up
Never gonna let you down
"""

print(message)

