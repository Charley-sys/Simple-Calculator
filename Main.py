# Prompt the user to enter the first number and convert it to a float
num1 = float(input("Enter the first number: "))

# Prompt the user to enter the second number and convert it to a float
num2 = float(input("Enter the second number: "))

# Prompt the user to enter the desired mathematical operation
operation = input("Enter the operation (+, -, *, /): ")

# Initialize a variable to store the result
result = None

# Check the entered operation and perform the corresponding calculation
if operation == '+':
    result = num1 + num2  # Perform addition
elif operation == '-':
    result = num1 - num2  # Perform subtraction
elif operation == '*':
    result = num1 * num2  # Perform multiplication
elif operation == '/':
    # Check for division by zero to prevent errors
    if num2 != 0:
        result = num1 / num2  # Perform division
    else:
        print("Error: Division by zero is not allowed.") # Inform the user about the error
else:
    print("Invalid operation. Please enter +, -, *, or /.") # Inform the user about invalid input

# If a valid operation was performed and a result was calculated, print the result
if result is not None:
    print(f"{num1} {operation} {num2} = {result}") # Display the calculation and its result
