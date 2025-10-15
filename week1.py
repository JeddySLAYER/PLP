print("welcome to our super calculator\nplease procced")
number_1 = int(input("enter your first number : "))
number_2 = int(input("enter your second number : "))
operation = input("enter your mathematical operation number ( +, -, *, / ) : ")

if operation == "+":
    print(number_1, operation, number_2, "=", number_1 + number_2)
elif operation == "-":
    print(number_1, operation, number_2, "=", number_1 - number_2)
elif operation == "*":
    print(number_1, operation, number_2, "=", number_1 * number_2)
elif operation == "/":
    print(number_1, operation, number_2, "=", number_1 / number_2)
else:
    print("invalid operation")