'''Object Oriented Programming (OOP):
Object-Oriented Programming(OOP), is all about creating “objects”. An object is a
group of interrelated variables and functions. These variables are often referred to as
properties of the object and functions are referred to as the behavior of the objects. These
objects provide a better and clear structure for the program.

Classes and Objects:
A class is a collection of objects. Unlike the primitive data structures, classes are data
structures that the user defines. They make the code more manageable.
When we define a class only the description or a blueprint of the object is created. There is no
memory allocation until we create its object. The objector instance contains real data or
information
Creating Classes in Python
The class keyword is used to create a new class in Python. The name of the class
 immediately follows the keyword class followed by a colon as shown below −'''
class ClassName:
   'Optional class documentation string'
   pass
'''The class has a documentation string, which can be accessed via ClassName.__doc__.
The class_suite consists of all the component statements defining class members, 
data attributes and functions.'''

#Example
class employee:
    company= "google"# start class attributes
    name ="ali"
    cnic= 34512340685
e=employee()
print(e.company,"\n",e.name,"\n",e.cnic)    

class employee:
    company= "microsoft"# start class attributes
    name ="ali"
    cnic= 34512340685
e=employee() # e that show object call the class body
e.language="python oop"# create object or instance attribute in object functions
print(e.company,"\n",e.name,"\n",e.cnic,"\n",e.language)    

#instance vs class attributes
class employee:
     name ="ali" #class attributes
     language ="english" #language datatype in class attributes
e=employee() # e that show object call the class body
e.language="python oop"# create object or instance attribute in object functions
print(e.name,"\n",e.language)    

#slef parameters:
'''slef refer to instance of class .its automatically passed with a function call from an object.'''
class Employee:
   'Common base class for all employees'
   empCount = 0
   def __init__(self, name, salary):#use constructor method
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   def displayCount(self):#use self parameter
     print ("Total Employee %d" % Employee.empCount)
   def displayEmployee(self):#use slef parameter
      print ("Name : ", self.name,  ", Salary: ", self.salary)
#explanation of this code:      
'''The variable empCount is a class variable whose value is shared among all 
instances of a this class. This can be accessed as Employee.empCount 
from inside the class or outside the class.

The first method __init__() is a special method, which is called class constructor 
or initialization method that Python calls when you create a new instance of this class.

You declare other class methods like normal functions with the exception that the first
 argument to each method is self. Python adds the self argument to the list for you; 
you do not need to include it when you call the methods. '''

'''Creating Objects of Classes in Python
To create instances of a class, you call the class using class name and pass in whatever
 arguments its __init__ method accepts.'''

'''Accessing Attributes of Objects in Python
You access the object's attributes using the dot operator with object. Class variable would 
be accessed using class name as follows −'''
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)
 # This would create first object of Employee class
emp1 = Employee("Zara", 2000)
print(emp1.name,emp1.salary)
emp1.displayCount()
emp1.displayEmployee()
# This would create second object of Employee class
emp2 = Employee("Manni", 5000)
print(emp2.name,emp2.salary)

#static method
'''some time we need a function that does not use the self parameter. we can define a static method like:'''
class employee:
    # start class attributes
    name ="ali"
    cnic= 34512340685
    salary=12000
    def employee(self):
      print (self.name,self.cnic,self.salary)  
    @staticmethod    
    def greet():
        print("this is employee data")  

e=employee() # e that show object call the class body
e.language="python oop"# create object or instance attribute in object functions
print(e.name,"\n",e.cnic,"\n",e.language,"\n",e.salary)    
e.employee()
e.greet()

#class method
''' class method is a method which is bound to the class and not object of the class.'''
class A:
    n=4
    @classmethod
    def num(cls):
        print(f"number is a :{cls.n}")
a=A()
a.n=2
print(a.n)

#super method:
'''super method is used to access the method of a super class in the derived class.'''
class employee:
    def __init__(self):
        print("constructor of employee")
    a=1
class manager(employee):
    def __init__(self):
        print("constructor of manager ")
    b=2        
class programmer(manager):
 
    def __init__(self):
        super().__init__()
        print("constructor of programmer")
    c=3           
p=programmer()
print(p.a,p.b,p.c)

#property decoratores:
'''property decoratores consider the follwing code'''
class employee:
    @property
    def name(self):
        return "{self.fname} {self.lname}"
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]
e=employee()
e.name="ali khan"
print(e.fname,e.lname)   

class A:
    
    @classmethod
    def num(cls):
        n=4
        print(f"number is a :{cls.n}")
a=A()
a.n=2
print(a.n)

#operators overloading
'''operators in python can be overloadednusing dunder methods.
These methodare called when a given operator is used in the objects.
operators in python can be overloaded using the following method.
p1+p2   p1 --add--p2
p1-p2   p1 --sub--p2
p1*p2   p1 --mul--p2
p1/p2   p1 --true.dived--p2
p1//p2   p1 --floor.dived--p2
--str--() :used to set what gets displayed upon calling str(obj)
--len__() :used to set what gets displayed upon calling __len__ or len(obj)
'''
class number:
    
    def __init__(self, n):
     self.n=n
    def __add__(self,num):
        return self.n+num.n 
n=number(1)
m=number(2)
print(n+m)        

#practice 
'''print programmer data'''
class programmer:
    company= "microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p=programmer("ali",12000,245001)
print(p.name,p.salary,p.pin)        

'''calculator to print squre,cube and squreroot '''
class calculator:
    def __init__(self,n):
        self.n=n
    def sq(self):
            print(f"squre is {self.n*self.n}")
    
    def cub(self):
            print(f"cube is {self.n*self.n*self.n}")
    
    def sqroot(self):
            print(f"squre_root is {self.n**1/2}")
c=calculator(3)
c.sq()
c.cub()
c.sqroot()    

'''store the record of train infomation using the getter function'''
from random import randint
class train:

    def __init__(self,trainNo):
        self.trainNo=trainNo
    def book (self, fro, to):
        print(f"ticket is booked in train no: {self.trainNo}  from {fro} to {to}")
    def getstatus(self):
        print(f"train number is : {self.trainNo} is runing on time")
    def getfareinfo(self, fro, to):    
        print(f"ticket is booked in train no: {self.trainNo}  from {fro} to {to} is {randint(222,3453)}")
t=train(23456)
t.book("lahor","karachi")
t.getstatus()
t.getfareinfo("islamabad","narowal")
