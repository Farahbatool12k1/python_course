'''Python Dictionary:
A Python dictionary is a collection of items, similar to lists and tuples. However, unlike lists and tuples, each item in a dictionary is a key-value pair (consisting of a key and a value).

Valid and Invalid Dictionaries:
Keys of a dictionary must be immutable,unordered,indexed
Keys of a dictionary must be unique and not duplicate the keys.

Create a Dictionary
We create a dictionary by placing key: value pairs inside curly brackets {}, separated by commas. 
For example,'''
# creating a dictionary
country_capitals = {
  "code_no" : 123, 
  "Canada": "Ottawa", 
  "England": "London"
}
# printing the dictionary
print(country_capitals)

'''Access Dictionary Items:
We can access the value of a dictionary item by placing the key inside square brackets.'''
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London"
}
# access the value of keys
print(country_capitals["Germany"])    # Output: Berlin
print(country_capitals["England"])    # Output: London

'''Iterate Through a Dictionary
A dictionary is an ordered collection of items (starting from Python 3.7),
therefore it maintains the order of its items.
We can iterate through dictionary keys one by one using a for loop.'''
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome" }
# print dictionary keys one by one
for country in country_capitals:
    print(country)
print()
# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)

'''ython Dictionary Methods
Here are some of the commonly used dictionary methods.

Function	Description
pop()	    Removes the item with the specified key.
update()	Adds or changes dictionary items.
clear()	    Remove all the items from the dictionary.
keys()	    Returns all the dictionary's keys.
values()	Returns all the dictionary's values.
get()	    Returns the value of the specified key.
popitem()	Returns the last inserted key and value as a tuple.
copy()	    Returns a copy of the dictionary.
'''

#methods or functions of dictionary
your_dic ={
  "name":"ali",
  "roll_no":207612,
  "programm":"BSCS",
  "institute_name":"uon"
}
print(your_dic)

print(your_dic.items()) #return a list of (key,value) intuple form.

print(len(your_dic)) #find the length of your dictionary.

#Python dictionaries are mutable (changeable). We can change the value of a dictionary
#element by referring to its key. For example,
your_dic["programm"] = " IT "
print(your_dic)

print(your_dic.update({"semester":"6th"})) #update dictionary with supplied key_value pairs.

print(your_dic.get("name")) #return value of the specified keys.

