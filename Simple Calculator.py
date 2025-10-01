#simple calculator (My Code)

##Ask for the Number
while True:

    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))

    ##Ask for the Function

    print("\nChoose Function of Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Muliplication")
    print("4. Division")
    print("5. Modulus")

    choice = input("Choose Operation Function: ")

    ## Caluclations for the function and print

    if choice == "1":
        print("The sum of two Numbers is:", num1+num2)
    elif choice == "2":
        print("The Difference of the two numbers is:", num1-num2)
    elif choice == "3":
        print("The product of the two numbers is:", num1*num2)
    elif choice == "4":
        if num2 != 0:
            print("The quotient of the two numbers is:", num1/num2)
        else:
            print("Number can't be divided by Zero you Asshole")
    elif choice == "5":
        print("The Module of the two numbers is:", num1%num2)
    else:
        print("Error: Add a Number from 1-5") 
    print("\n")