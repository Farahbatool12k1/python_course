'''inheritance:
inheritance is a way of creating a new class from an existing class.


Benefits of Using Inheritance in Python
Inheritance in Python offers several advantages that significantly benefit developers 
in building efficient and maintainable code.

Code reuse: Inheritance enables the reuse of established code to create new classes.
Developers inherit existing methods and attributes from parent classes. Using 
pre-existing functionalities and structures minimizes repetition and saves time and effort.

Access to parent class features: When a class inherits from another, it gains access to the
entirety of the parent class’s methods and attributes. This inheritance enables the use of
established functionalities and encourages a systematic coding approach where common features
are centralized in a base class and shared across various subclasses.

Reliability through tested code: Inherited code often originates from thoroughly tested base
classes, providing a sense of trust and validation for the functionalities inherited by 
subclasses when integrated into new contexts.

Time and cost efficiency: Reusing tested and validated code significantly reduces development
time and costs. Leveraging existing functionalities diminishes the need to build new features
from scratch, streamlining the development process and optimizing resource utilization.

Consistent interfaces: Inheritance fosters the maintenance of consistent interfaces across
related classes. Standardizing how methods and attributes are accessed and used enhances 
code readability and comprehensibility, facilitating better understanding and management of the codebase.

Reducing redundancy: Centralizing shared functionalities in a base class through inheritance 
minimizes redundant code segments. This consolidation reduces the need for duplicating code and
helps avoid inconsistencies or errors within the codebase while enhancing its maintainability.

Support for extensions and customization: Inheritance permits the extension and 
customization of existing functionalities. New classes inherit from base classes and can
modify or supplement specific methods or attributes, allowing developers to tailor
functionalities to meet specific requirements while retaining the core features provided by the base class.

Simplified class libraries development: With inheritance, developers can create reusable
class libraries effortlessly. Establishing hierarchical relationships among classes with
shared functionalities promotes modular code development. These libraries can be easily
reused across different projects, encouraging consistent and efficient development practices.'''


#examples:
class employee:
    company="microsoft system "
    
class programmer(employee):
    company1="software development"
    
p=programmer()
print(p.company)
print(p.company1)

#example
class Grandparent:

    def __init__(self, eye_color, hair_type):

        self.eye_color = eye_color

        self.hair_type = hair_type

    def describe(self):

        return f"Eye color: {self.eye_color}, Hair type: {self.hair_type}"

# Parent class inheriting from Grandparent

class Parent(Grandparent):
     def __init__(self, eye_color, hair_type, profession):

        super().__init__(eye_color, hair_type)

        self.profession = profession

     def describe(self):

        return f"{super().describe()}, Profession: {self.profession}"

# Child class inheriting from Parent

class Child(Parent):

     def __init__(self, eye_color, hair_type, profession, hobby):

        super().__init__(eye_color, hair_type, profession)

        self.hobby = hobby

     def describe(self):
          return f"{super().describe()}, Hobby: {self.hobby}"

# Creating instances
grandparent = Grandparent("Brown", "Curly")
parent = Parent("Brown", "Curly", "Engineer")
child = Child("Blue", "Straight", "Student", "Playing Guitar")
# Description
print("Grandparent:", grandparent.describe())
print("Parent:", parent.describe())
print("Child:", child.describe())
    
#types of inheritance
'''What Are The Types of Inheritance in Python?
Inheritance is categorized based on the hierarchy followed and the number of parent classes and
subclasses involved.
Python supports five types of inheritance: single inheritance, multiple inheritance,
multilevel inheritance, hierarchical inheritance, and hybrid inheritance. Single inheritance
allows a class to inherit from one parent class, enabling straightforward extensions. Multiple
inheritance enables a class to inherit from multiple parent classes, combining functionalities 
but with added complexity. Multilevel inheritance involves a class inheriting from another class, 
which in turn inherits from a third class, creating a chain. Hierarchical inheritance occurs when
multiple classes inherit from a single parent class, promoting shared functionality across
different classes. Hybrid inheritance is a mix of two or more types of inheritance, providing flexibility 
and reusability by combining the features of different inheritance models.

Single Inheritance
Multiple Inheritance
Multilevel Inheritance
Hierarchical Inheritance
Hybrid Inheritance'''
#single inheritance
'''Single Inheritance
What is single inheritance in python? This type of inheritance enables a subclass or derived class 
to inherit properties and characteristics of the parent class, this avoids duplication of code and 
improves code reusability.
It is fundamental and straightforward, enabling the subclass to acquire all the attributes and 
methods of its parent class.
By implementing single inheritance, classes can organize their relationships in a linear structure,
 where a class inherits from a single parent. This helps avoid redundancy in code by allowing the 
 subclass to access and utilize the functionalities defined in the parent class.
Single inheritance promotes code reusability and supports the principle of DRY (Don’t Repeat Yourself), 
as it eliminates the need to duplicate code. It simplifies the class hierarchy, making it easier to 
understand and maintain. However, while single inheritance provides a clear and manageable structure, 
it may not cover scenarios where a class needs traits from multiple sources, where multiple inheritance
 might be more suitable.
Here is an example illustrating this Python class inheritance:
'''
#Single inheritance in Python example

#parent class
class Above:
    i = 5
    def fun1(self):
        print("Hey there, you are in the parent class")

#subclass
class Below(Above):
    i=10
    def fun2(self):
        print("Hey there, you are in the sub class")

temp1=Below()
temp2=Above()
temp1.fun1()
temp1.fun2()
temp2.fun1()
print(temp1.i)
print(temp2.i)

'''Multiple Inheritance:
What is multiple inheritance in python? This inheritance enables a child class to inherit from more than
one parent class. This type of inheritance is not supported by java classes, but python does support this
kind of inheritance. It has a massive advantage if we have a requirement of gathering multiple 
characteristics from different classes.
Multiple inheritance in Python lets a class use traits from more than one parent class. 
This helps create flexible classes that combine different behaviors and features. However,
handling multiple inheritances requires careful thought to keep the code clear and avoid 
complications from interactions between the different parent classes.
To help define this inheritance in Python, here is an illustrated example: '''

#Multiple inheritance in python example:
#parent class 1
class A:
    demo1=0
    def fun1(self):
        print(self.demo1)

#parent class 2
class B:
    demo2=0
    def fun2(self):
        print(self.demo2)

#child class
class C(A, B):
    def fun3(self):
        print("Hey there, you are in the child class")

# Main code
c = C()
c.demo1 = 10
c.demo2 = 5
c.fun3()
print("first number is :" ,c.demo1)
print("second number is : ",c.demo2)

#Multilevel Inheritance
'''What is multilevel inheritance?
In multilevel inheritance, the transfer of the properties of characteristics is done to more than one
class hierarchically. To get a better visualization we can consider it as an ancestor to grandchildren
relation or a root to leaf in a tree with more than one level.
It is a hierarchical inheritance in Python where a subclass is created from another subclass,
which itself is derived from a parent class. This creates a chain or hierarchy of classes, 
where each subclass inherits traits from its immediate parent and from the classes further 
up in the hierarchy. This way, the properties trickle down the chain, allowing for the inheritance 
of attributes and methods from multiple levels.
Multilevel inheritance in Python example
'''
#parent class 1
class vehicle:
    def functioning(self):
        print("vehicles are used for transportation")

#child class 1
class car(vehicle):
    def wheels(self):
        print("a car has 4 wheels")
       
#child class 2
class electric_car(car):
    def speciality(self):
        print("electric car runs on electricity")

electric=electric_car()
electric.speciality()
electric.wheels()
electric.functioning()

#Hierarchical Inheritance
'''What is hierarchical inheritance? 
This inheritance allows a class to host as a parent class for more than one child class or subclass. 
This provides a benefit of sharing the functioning of methods with multiple child classes, hence avoiding 
code duplication.
In hierarchical inheritance, a parent class allows multiple child classes to inherit its attributes and 
methods. This setup avoids repeating code by sharing common functionalities among subclasses. The parent 
class’s methods and attributes are accessible to all its child classes, promoting code reuse and improving 
organizational efficiency.Developers use this Python class inheritance to create a well-organized class 
system. This approach minimizes redundancy and streamlines development with shared functionalities across 
related classes. '''
#Hierarchial inheritance in Python example

#parent class
class Parent:
    def fun1(self):
        print("Hey there, you are in the parent class")
 #child class 1
class child1(Parent):
    def fun2(self):
        print("Hey there, you are in the child class 1")
#child class 2 
class child2(Parent):
    def fun3(self):
        print("Hey there, you are in the child class 2") 
#child class 3
class child3(Parent):
    def fun4(self):
        print("Hey there, you are in the child class 3")
# main program
child_obj1 = child3()
child_obj2 = child2()
child_obj3 = child1()
child_obj1.fun1()
child_obj1.fun4()
child_obj2.fun1()
child_obj2.fun3()
child_obj3.fun1()
child_obj3.fun2()

'''Hybrid Inheritance:
What is hybrid inheritance?
An inheritance is said hybrid inheritance if more than one type of inheritance is implemented 
in the same code. This feature enables the user to utilize the feature of inheritance at its best. 
This satisfies the requirement of implementing a code that needs multiple inheritances in implementation.
This feature enables developers to combine various inheritance types, creating complex class relationships. 
By using multiple forms of inheritance, programmers can design classes that meet specific requirements 
demanding multiple inheritances.'''

#Hierarchical inheritance in Python example

class A:
 def fun1(self):
  print("Hey there, you are in class A")
class B(A):
 def fun2(self):
  print("Hey there, you are in class B")
class C(A):
 def fun3(self):
  print("Hey there, you are in class C")
class D(C,A): 
 def fun4(self):
  print("Hey there, you are in the class D")#main program
ref = D()
ref.fun4()
ref.fun3()
ref.fun1()
#practice:
'''print twoDvector and threeDvector'''
class twoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"{self.i}i+{self.j}j ")
class threeDvector(twoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f"{self.i}i+{self.j}j+{self.k}k")
t=threeDvector(1,2,3)
t.show()

'''class animal to derived class pets to dog speek bark "bow bow"'''
class animals:
    pass
class pets(animals):
    pass
class dog(pets):
    @staticmethod
    def bark():
        print("bow bow")        
d=dog()
d.bark()        

'''create class employee and add salary and increament properties it and salary after increament is .'''
class employee:
    salary=230
    increament=20
    @property
    def salaryafterincreament(self):
        return(self.salary+self.salary*(self.increament/100))
    @salaryafterincreament.setter
    def salaryafterincreament(self,salary):
        self.increament=((salary/self.salary)-1)*100
e=employee()
e.salaryafterincreament=234
print(e.increament)        

'''print complex numbers along with operator overloaded "+"
and "*" them.'''
class complex:
    def __init__(self,r,i):
        self.r=r 
        self.i=i
    def __add__(self,c2):
        return complex(self.r+c2.r,self.i+c2.i)
    def __str__(self):
        return f"{self.r} + {self.i}i"   
    def __mul__(self,c2):
        real_part=self.r*c2.r-self.i*c2.i    
        imag_part=self.r*c2.i +self.i*c2.r  
        return complex(real_part,imag_part)  
c1=complex(3,2)
#c2=complex(4,6)
print(c1+c1)          
print(c1*c1)          



