'''Polymorphism in Python
What is Polymorphism?
The literal meaning of polymorphism is the condition of occurrence in different forms.
Polymorphism is a very important concept in programming. It refers to the use of a single 
type entity (method, operator or object) to represent different types in different scenarios.
Let's take an example:'''
num1 = 1
num2 = 2
print(num1+num2)

str1 = "Python"
str2 = "Programming"
print(str1+" "+str2)

'''Function Polymorphism in Python
There are some functions in Python which are compatible to run with multiple data types.
One such function is the len() function. It can run with many data types in Python. Let's look at some 
example use cases of the function.
Example 2: Polymorphic len() function'''
print(len("Programiz"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Nepal"}))
'''Class Polymorphism in Python
Polymorphism is a very important concept in Object-Oriented Programming.
To learn more about OOP in Python, visit: Python Object-Oriented Programming
We can use the concept of polymorphism while creating class methods as Python allows different
classes to have methods with the same name.
We can then later generalize calling these methods by disregarding the object we are working with. 
Let's look at an example:
Example 3: Polymorphism in Class Methods'''
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()

'''Polymorphism and Inheritance
Like in other programming languages, the child classes in Python also inherit methods and 
attributes from the parent class. We can redefine certain methods and attributes specifically 
to fit the child class, which is known as Method Overriding.
Polymorphism allows us to access these overridden methods and attributes that have the same 
name as the parent class.
Let's look at an example:
Example 4: Method Overriding'''
from math import pi
class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        return " area of the shape "
    def fact(self):
        
        return "I am a two-dimensional shape."
    def __str__(self):
        return self.name
class Square(Shape):
    def __init__(self, length):
        #super().__init__("Square")
        self.length = length
    def area(self):
        return self.length**2
    def fact(self):
        return "Squares have each angle equal to 90 degrees."
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    def area(self):
        return pi*self.radius**2
a = Square(4)
b = Circle(7)
print(b)
print(a.area())
print(a.fact())
print(b.fact())
print(b.area())    

