'''Recursion function:
Recurion function is a function which calls itself .its to directly use a mathematically fromula as a function.
Example code below:'''
#print the facturial number 
def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)
print(factorial_recursive(6))
#other example code:
def sum_recursive(current_number, accumulated_sum):
    # Base case
    # Return the final state
    if current_number == 11:
        return accumulated_sum

    # Recursive case
    # Thread the state through the recursive call
    else:
        return sum_recursive(current_number + 1, accumulated_sum + current_number)
print(sum_recursive(2,4))        