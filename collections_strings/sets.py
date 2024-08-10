'''sets is a coolection of non repetitive elements.

properties of sets:
unordered,
unindexed,
immutable means that no change and 
con't duplicated the values.

example codes:'''
s= set() # empty set that no contain  element
print(s) 
s.add(1) 
s.add(3) 
print(s) 

#operations in sets
s1={1,4,7,0,8,3}
s2={2,8,6,7,9,0}
print(s1)
print(s2)

print(len(s1)) #find the length of set 1
print(len(s2)) #find the length of set 2

print(s1.remove(3)) #update set s1 and remove 3 from s1 set.

print(s1.union(s2)) #return the both sets s1 ans s2 whole values.

print(s1.intersection(s2)) # return the commman values from both sets s1 and s2.

print(s1.clear()) # clear the whole values from  s1 set.

print(s2.pop()) #remove arbitrary element from s2 set.


