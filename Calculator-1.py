while True:
    number1 = float(input("Enter your first number:"))
    number2 = float(input("Enter your second number:"))
    print("options:")
    print("Enter '+' to add two numbers")
    print("Enter '-' to substract to numbers")
    print("Enter '*' to multiply two numbers")
    print("Enter '/' to divide two numbers")
    print("Enter 'Exit' to end the program")
    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input == "+":
        print("Summation is:", number1+number2)
    elif user_input == "-":
        print("This Calculator substract 1st number from the second one!")
        print("The result is:", number1-number2)
    elif user_input == "*":
        print("The result is:", number1*number2)
    elif user_input == "/":
        print("This program divide by second number")
        print("The result is:", number1/number2)
    else:
        print("Unknow input")
