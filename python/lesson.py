

print('Hello world!')
print('What is your name?') # ask for their name
myName = input()
print ('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge)+1) + ' in a year')
#functions : print function for making text appears on the scream, there is an input function, and a changing function that can convert ints to floats to strings
#boolena vlaues, datatype has two values of true and false
#comparison operators ==, !=, <, >, <=, >= } these help with boolean values
42 == 42
myAge = 26
#myAge < 30 is true
#three boolean operators : and, or and not
# true and true is true, true and false is false, false and false is false
# true or false is true, false or false is false
# not operator: not true is false, and not false is true
# float control statements: if or and else
name = 'alice'
if name == 'alice': #this is the condition statement in the expression
    print ('hi alice') #if the condition is true then the function will execute this
print ('done')
#block is signified by indentation, begin and ends by the same indentation
password = "swordfish"
if password == "swordfish":
    print ("access grantded")
else: 
    print ("wrong password")
# to create else if statements use the word "elif"
if password == "swordfish":
    print ("access grantded")
elif password == "hello":
    print ("wrong, but hello")
else: 
    print ("wrong password")
#truthy and falsey values:
#if you want to be more explicate
print ("enter a name")
name = input()
if name:
    print ("Thank you for your name, " + name)
else: 
    print ("you need to enter name")
#while statements:

spam = 0
while spam < 5:
    print  ("hi")
    spam = spam +1
# this while loop will iterate 5 times
#similar to if statements, becuase it is a conditional statement, but until the condition is false
# FOR LOOPS: 
print ("my name is ")
for i in range (5):
    print ("jimmy 5 times: " + str(i))
# don't need to add it numbers explicitly
# to specficy the range use two digits in the () EXAMPLE (1,6) : this will have a start and end integer
#with three integers in the paranthesis, it shows how much you want to increase the integer by
import random
random.randint (1, 10) #will give you a random integer betwene 1 and 10
from random import * #if you use this, then you dont need to say "random." before "randint"
#to be able to terminate the function, 
import sys 
print ("hello")
sys.exit()
print ("hi")
# in the example above, the program will print out the hello, but not hi
>>> hypotenuse (3.0, 4.0)
'''
def is_even(n):
    if n%2 == 0:
        return True
        print ("its even!")
    else:
        return False
        print ("its odd")

# this comment is called a docstring and indicates a doctest
# whenever you see a dollar sign, it means it typed into terminal below
# when you see python3, /usr/bin/python3 : copying and pasting the >>>

#!/bin/python
'''