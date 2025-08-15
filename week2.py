# 🧮 Basic Calculator with Operation Validation and Modulus

# Step 1: Get two valid numbers once
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        break
    except ValueError:
        print("Invalid input. Please enter numeric values.\n")

# Step 2: Keep asking for a valid operation until a correct one is entered
while True:
    operation = input("Enter the operation (+, -, *, /, %): ")

    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
        break
    elif operation == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
        break
    elif operation == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
        break
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
        break
    elif operation == "%":
        if num2 != 0:
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")
        else:
            print("Error: Modulus by zero is not allowed.")
        break
    else:
        print("Invalid operation. Please enter one of +, -, *, /, %.\n")
        
