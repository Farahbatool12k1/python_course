'''Methods of Python String
Besides those mentioned above, there are various string methods present in Python.
 Here are some of those methods:

Methods	Description
upper() 	Converts the string to uppercase
lower()	    Converts the string to lowercase
partition()	Returns a tuple
replace()	Replaces substring inside
find()	    Returns the index of the first occurrence of substring
rstrip()	Removes trailing characters
split()	    Splits string from left
startswith()	Checks if string starts with the specified string
isnumeric()	    Checks numeric characters
index()	    Returns index of substring'''

#example code
#length of string
mes="hi hello"
print(len(mes))
#upper() 	Converts the string to uppercase
print(mes.upper())
#lower()	 Converts the string to lowercase
print(mes.lower())
#startswith()	Checks if string starts with the specified string
print(mes.startswith("he"))
#endwith()	Checks if string ending with the specified string
print(mes.endswith("ll"))
#replace()	Replaces substring inside
print(mes.replace("hi","hello"),("hello","world"))
#find()	    Returns the index of the first occurrence of substring
print(mes.find("w"))




