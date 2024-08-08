'''Functions
In Python, a function is a group of related statements that performs a specific task.
Functions help break our program into smaller and modular chunks. As our program grows
larger and larger, functions make it more organized and manageable. Furthermore, it avoids
repetition and makes the code reusable.'''

#syntax
#function definantion
def func():
    print("helo hi")

#function call
func()    


#find sum and averge
def avg():
    n1=int(input("enter the no 1 :")) 
    n2=int(input("enter the no 2 :")) 
    n3=int(input("enter the no 3 :")) 
    sum = n1+n2+n3
    print(f"the sum is : {sum}")
    averge=sum/3
    print(f"the averge is : {averge}")
avg()

'''Partial Functions in Python:
Partial functions allow us to fix a certain number of arguments of a function and generate a new function.
 In this article, we will try to understand the concept of Partial Functions with different examples in Python.

What are Partial functions and the use of partial functions in Python?
Partial functions in Python is a function that is created by fixing a certain number 
of arguments of another function. Python provides a built-in module called functools that includes 
a function called partial that can be used to create partial functions. The partial function
takes a callable (usually another function) and a series of arguments to be pre-filled in the
new partial function. 
'''
# example 1 code:
from functools import partial

# A normal function
def f(a, b, c, x):
	return 1000*a + 100*b + 10*c + x

# A partial function that calls f with
# a as 3, b as 1 and c as 4.
g = partial(f, 3, 1, 4)

# Calling g()
print(g(5))

#example 2 code:
from functools import *

# A normal function
def add(a, b, c):
	return 100 * a + 10 * b + c

# A partial function with b = 1 and c = 2
add_part = partial(add, c = 2, b = 1)

# Calling partial function
print(add_part(3))

#function with arguments and parameters
'''function can accept som,e values of can work with . we put these values in paranthesis.
a function can return values as show below:'''
#function definantion
def greet(name):
 return name
#function call
g=greet(" ali") 
print(g)

'''defult parameter values:
A values as defult argument in function specify name containing def,this used when arguments is passed.
example code below:'''
def greet(name="ali"):
 return name
#function call
g=greet( ) # use defult paramter
print(g)


'''return function:
return function that is used to return a value when function is executed it outomatically give output.
example code:'''
def func(n):
    return n
num=func(12)    
print(num)  


#practice set of function:
#print tables 1 to 10input from user 
for i in range(1,11):
 def tables():
        n= int(input("enter the number : \n"))
        for j in range(1,11):
            print(f"{n} * {j} = {n*j}")
 tables()    
#find the greatest values from three numbers by user input
def greatest_no():
    n1=int(input("enter the no 1 :"))
    n2=int(input("enter the no 2 :"))
    n3=int(input("enter the no 3 :"))
    
    if (n1>n2 and n1>n3):
     print (n1)
    elif (n2>n1 and n2>n3):
     print (n2)
    elif (n3>n2 and n3>n2):
     print (n3)
    
greatest_no()

#find the sum of facturial number
def sum(n):
    if (n==1):
        return 1
    else:
        return sum(n-1)+1
print(sum(8))            



