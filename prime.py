number = int(input("Enter a Number:"))

if number > 1:
    for i in range(2,number):
        if (number % i) == 0:
            print(number, "It is not a prime number")
            break
    else:
        print("The number", number, "is a prime number")