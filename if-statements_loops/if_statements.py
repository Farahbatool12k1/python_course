

#if staements
#if statements is a conditional statements which the decision making in the programing code.

#exmplas and syntax:
marks=int(input("enter the marks:\n"))
# if statement 1
if(marks%2==0):
 print("marks is even marks")

 #if,elif and else statements

marks1=int(input("enter the marks:\n"))
marks2=int(input("enter the marks:"))
if(marks>=marks2):
 print("marks is grater than marks2 \t",marks)
elif(marks<0):
 print("value is invaild due to negtive marks\t",marks,marks2)
elif(marks==marks2):
 print("value is vaild due to positive marks\t",marks,marks2)
else:
 print("marks2 marks is greater then marks \t",marks,marks2)

print(" end program ")

#find greatest marks of studenst

marks1=int(input("enter the marks 1:\n"))
marks2=int(input("enter the marks 2:\n"))
marks3=int(input("enter the marks 3:\n"))
marks4=int(input("enter the marks 4:\n"))
if(marks1>marks2 and marks1>marks3 and marks1>marks4):
 print("greatest no is marks1:",marks1)
elif(marks2>marks1 and marks2>marks3 and marks2>marks4):
 print("greatest no is marks2:",marks2)
elif(marks3>marks1 and marks3>marks2 and marks3>marks4):
 print("greatest no is marks3:",marks3)
elif(marks4>marks2 and marks4>marks2 and marks4>marks3):
 print("greatest no is marks4:",marks4)
 print("greatest no is marks4:",marks4)

 #find averge if the marks is tootal 40% and ar least 30% is passed otherwise not

marks1=int(input("enter the marks 1:\n"))
marks2=int(input("enter the marks 2:\n"))
marks3=int(input("enter the marks 3:\n"))
marks4=int(input("enter the marks 4:\n"))
total_percentage = 100*(marks1+marks2+marks3+marks4)/400
if(total_percentage>=40):
 print("you are passed and congragulation:",total_percentage)
else:
 print("you failed and so saaaaaadd!..:",total_percentage)
