num1 = int(input("Please enter number1: "))
num2 = int(input("Please enter number2: "))

operation = input("Please enter (+, -, * or /): ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("Your operation is not valid")