num1 = int(input("Enter Your First Number: "))
num2 = int(input("Enter Your Second Number: "))
operation = input("Enter Your Operation (+, -, *, /: ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("Invalid Entry")
