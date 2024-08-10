'''Create a Python List
We create a list by placing elements inside square brackets [], separated by commas. 

List Characteristics:
Lists are:
Ordered - They maintain the order of elements.
Mutable - Items can be changed after creation.
Allow duplicates - They can contain duplicate values.'''

#list method example codes:
 # a list of three elements
ages = [19, 26, 29]
print(ages)

# Output: [19, 26, 29]

friends_name=["ali","rahat","fatah","rehnma"]
print(friends_name[0])
friends_name[0]="rohan"
print(friends_name[0])

#list add() item,change() and delete() items
print(friends_name[1:4])

#methods:
l=[1,3,7,8,4,9,5,0]
l.sort() #update the list and sorted in sequences.
print(l)

l.reverse() # update the list reverse order.
print(l)

l.append(10) #that connect of add(item) at the end of list.
print(l)

l.insert(6,2) #that 6 show as a index number and 2 show that the value who add in the list.
print(l)

l.pop(3) #delete the value at the index 3.
print(l)

l.remove(8) #remave the value 8 from list.
print(l)

fruits = ['apple', 'banana', 'orange']
print('Original List:', fruits)

# using append method 
fruits.append('cherry')

print('Updated List:', fruits)