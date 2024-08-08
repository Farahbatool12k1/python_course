#Monkey Patching in Python (Dynamic Behavior)

'''In Python, the term monkey patch refers to dynamic (or run-time) modifications of a class or module.
 In Python, we can actually change the behavior of code at run-time.'''
 # monk.py 
class A: 
	def func(self): 
		print ("func() is being called") 
 
'''We use above module (monk) in below code and change behavior of func() at run-time by assigning
  different value.'''
import monk 
def monkey_f(self): 
	print ("monkey_f() is being called") 

# replacing address of "func" with "monkey_f" 
monk.A.func = monkey_f 
obj = monk.A() 
# calling function "func" whose address got replaced 
# with function "monkey_f()" 
obj.func() 
