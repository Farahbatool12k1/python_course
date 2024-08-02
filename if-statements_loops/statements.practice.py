#Statements in Python

#1.Conditional Statements:
#Write a Python program to check if a given number is positive, negative, or zero.
num =int(input("Enter a number: "))

if (num > 0):
    print(f"{num} is a positive number.")
elif (num < 0):
    print(f"{num} is a negative number.")
else:
    print(f"{num} is zero.")

#Create a program to determine if a person is eligible to vote based on their age.
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
#Develop a script to find the largest of three numbers using conditional statements.


num1 =int(input("Enter first number: "))
num2 =int(input("Enter second number: "))
num3 =int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest number.")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest number.")
else:
    print(f"{num3} is the largest number.")

#Write a program to check if a year is a leap year.
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#Create a program to classify a triangle as equilateral, isosceles, or scalene based on its side lengths.

a = float(input("Enter side length a: "))
b = float(input("Enter side length b: "))
c = float(input("Enter side length c: "))

if a == b == c:
    print("The triangle is equilateral.")
elif a == b or a == c or b == c:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")

#2.Assignment Statements:

#Explain the difference between = and == operators in Python.
'''Assignment Operator (=):

The = operator is used to assign a value to a variable. It sets the value of the variable on the left side to the value on the right side.

Example: x = 5 assigns the value 5 to the variable x.

Equality Operator (==):

The == operator is used to compare two values for equality. It checks whether the values on both sides are equal and returns a boolean result (True or False).

Example: x == 5 checks whether the value of x is equal to 5 and returns True if they are equal, or False otherwise.
'''
#○What is the output of the following code: x = 5; y = x; x = 10; print(y)?
x=5
y=x
x=10
print(y)
#output is 5 in variable y

#Write a Python program to swap the values of two variables without using a temporary variable.
x = 5
y = 10

print("Before swap: x =", x, "y =", y)

# Swap values using tuple unpacking
x, y = y, x

print("After swap: x =", x, "y =", y)
#How do you assign multiple values to multiple variables in a single line?
'''In Python, you can assign multiple values to multiple variables in a single line using a feature called "tuple unpacking" or "parallel assignment". Here's the syntax:

var1, var2, ..., varN = value1, value2, ..., valueN

For example:

x, y, z = 1, 2, 3

This assigns 1 to x, 2 to y, and 3 to z in a single line.'''

