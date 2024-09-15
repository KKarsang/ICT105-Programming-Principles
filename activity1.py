#Variable Declaration and types
#1.Declaring variables and assigning values for them
a= 15
b= 12
#2.Using type()function and printing 
print("The type of a is:", type(a))
print("The type of b is:", type(b))

#Basic Arithmetic Operations
#1.Addition
sum = a+b
print("a+b =", sum)
#2.Subtraction
difference = a-b 
print("a-b=",difference)
#3.Multiplication
product = a*b
print("a*b=", product)
#4.Division
quotient = a/b
print("a/b=", quotient)

#Using Variables and Type Casting
#1.Creating a new variable c that stores the result of a divided by b
c= int(a/b)
#2.Printing value and the 'type' of c
print("The value of c=", c)
print("The type of c=", type(c))
#3.converting c to a float and printing its new value and type
c= float(a/b)
print("The value of c=", c)
print("The type of c=", type(c))

#Working with Strings
#1.Declaring a string variable message with the value "The result of a divided by b is:"
a= 15
b= 12
difference= a/b
message = "The result of a divided by b is:"
print(message , difference)
#2.Concatenating the message with the value of c (converted to a string) and printing the result
link= message + "" + str(c)
print(link)

#Using Comparison Operators
#1.Comparing if a is greater than b and printing the result (True/False)
Is_a_greater= a>b 
print(Is_a_greater)
#2.Checking if a is equal to b and printing the result (True/False).
Is_a_and_b_equal = a==b
print(Is_a_and_b_equal)