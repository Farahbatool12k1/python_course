#Loops in Python
#1.For Loops:
#Write a program to print the numbers from 1 to 10.
for i in range(1, 11):
    print(i)

#Create a script to calculate the factorial of a given number.
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "is:", factorial)

#Develop a program to find the sum of all even numbers between 1 and 100.
sum_even = 0
for i in range(2, 101, 2):
    sum_even += i

print("Sum of even numbers between 1 and 100:", sum_even)

#Write a program to iterate through a list and print its elements.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Iterate through the list using a for loop
for element in my_list:
    print(element)
#Create a program to print the characters of a string in reverse order.  
# Define a string
my_string = "Hello World"

# Print the characters in reverse order
for i in range(len(my_string)):
    print(my_string[i])

#while loop
#Write a program to print numbers from 1 to 10 using a while loop.  
# Initialize a variable to keep track of the current number
num = 1

# Continue the loop until num is greater than 10
while num <= 10:
    # Print the current number
    print(num)
    
    # Increment num by 1
    num += 1

    #Create a script to find the sum of digits of a number.  
    # Get the number from the user
num = int(input("Enter a number: "))

# Initialize a variable to store the sum of digits
sum_of_digits = 0

# Loop until the number becomes 0
while num != 0:
    # Get the last digit of the number
    digit = num % 10
    
    # Add the digit to the sum
    sum_of_digits += digit
    
    # Remove the last digit from the number
    num //= 10

# Print the sum of digits
print("Sum of digits:", sum_of_digits)

#Develop a program to check if a number is prime or not.
# Get the number from the user
num = int(input("Enter a number: "))

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Check if the number is prime
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

#Write a program to implement a simple guessing game.    
import random

# Print a welcome message
print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 100.")
number_to_guess=random.randint(1,100)
guess=None
# Loop until the user guesses the number
while (guess!=number_to_guess):
    # Get the user's guess
    user_guess = int(input("Enter your guess: "))

    # Increment the number of attempts
    attempts=1
    attempts += 1

    # Check if the user's guess is correct
    if (user_guess==number_to_guess):
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
        number_to_guess=0
    elif (user_guess>number_to_guess):
        print("Too high!")
    elif (user_guess<number_to_guess):
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")



#Create a program to calculate the Fibonacci series up to a given number.
# Get the number from the user
n = int(input("Enter a number: "))

# Initialize the first two Fibonacci numbers
a, b = 0, 1

# Print the Fibonacci series up to the given number
print("Fibonacci series up to", n, ":")
while (a <= n):
    print(a)
    a, b = b, a + b

# Print a newline at the end
print()
