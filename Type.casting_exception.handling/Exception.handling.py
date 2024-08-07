'''
Exception handling:
python has many built-in exceptions that are raised when your program encounters an 
error. when these exceptions occur,the python interpreter stops the current 
process and passes it to calling process until it is handled.
'''

#example code 1:

try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

# Output: Error: Denominator cannot be 0. 


#example code 2:
try:
    
    even_numbers = [2,4,6,8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")

# Output: Index Out of Bound