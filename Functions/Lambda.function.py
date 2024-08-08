'''Python Lambda/Anonymous Function
In Python, a lambda function is a special type of function without the function name. For example,'''
lambda : print('Hello World')
'''Python Lambda Function Declaration:
We use the lambda keyword instead of def to create a lambda function. Here's the syntax to declare the
 lambda function:'''
#lambda argument(s) : expression 
'''argument(s) - any value passed to the lambda function
expression - expression is executed and returned'''
greet = lambda : print('Hello World')
#To execute this lambda function, we need to call it. Here's how we can call the lambda function

# call the lambda
greet()

#complete example code

# declare a lambda function
greet = lambda : print('Hello World')

# call lambda function
greet()

# Output: Hello World