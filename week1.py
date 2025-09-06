# This program acts as a basic calculator.
# It takes two numbers and an operation from the user,
# performs the calculation, and prints the result.

# Step 1: Get the first number from the user.
# The input() function gets text from the user, and we use float()
# to convert that text into a number that can have decimal places.
try:
    num1 = float(input("Enter the first number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    # Exit the program if the input is not a number
    exit()

# Step 2: Get the mathematical operation from the user.
# We store the user's input as a string.
operation = input("Enter a mathematical operation (+, -, *, /): ")

# Step 3: Get the second number from the user.
# We do the same conversion and error handling as for the first number.
try:
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Step 4: Perform the calculation based on the operation.
# We use an if-elif-else block to check which operation the user chose.
if operation == '+':
    # Addition
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    # Subtraction
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    # Multiplication
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    # Division
    # We add a check to prevent division by zero, which would cause an error.
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    # Handle cases where the user enters an invalid operation.
    print("Invalid operation. Please enter +, -, *, or /.")
