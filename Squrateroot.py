#Using Exponentiation Operator

while True:
    num1 = float(input("Enter a number here: "))
    squareroot = num1**(0.5)
    print("the square root of the given number is", squareroot)
    again = input("Do you want to enter another number? (yes/no): ")
    if again.lower() != "yes":
        break

#Using the maths Module

import math
while True:
    num1 = float(input("Enter a number here: "))
    squareroot = math.sqrt(num1)
    print("the square root of the given number is", squareroot)