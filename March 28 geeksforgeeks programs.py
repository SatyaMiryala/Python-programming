'''
#1.Python program to add two numbers
a = int(input("Please enter a number"))
b = int(input("Please enter a number"))
c = a + b
print(f"Sum of {a} and {b} is {c}")

#2.Maximum of two numbers in Python
val1 = int(input("Please enter a number"))
val2 = int(input("Please enter a number"))

if val1>val2:
    print(val1)
else:
    print(val2)
#3.Python Program for factorial of a number

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial) 

#4. Python Program for simple interest

p = int(input("please enter the Principle amount"))
t = float(input("please enter the time"))
r = float(input("please enter the rate of intreset"))

simple_interest = (p*t*r)/100
print(f"The simple intrest with principle amt {p},time {t} and rate{r} is {simple_interest}")

#5.Python Program for Program to find area of a circle

r = int(input("Pleaase enter the number"))
pi = 3.14
area_circle = pi*(r**2)
print(f"The area of circle with Radius {r} is {area_circle}")


#6.Python program to print all Prime numbers in an Interval

lower = int(input("Please enter a number"))
upper = int(input("Please enter a number"))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
'''
#7.Python Program for compound interest
def compound_interest(p, r, t):
    amt = p*((1+(r/100))**t)
    ci = amt - p
    print(f"The compount interest {ci}")
compound_interest(10000, 10.25, 5)
