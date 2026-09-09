def add(a, b):
    return a + b
def subtract(a, b): 
    return a - b

# Prompt the user for input
# Note: input() returns text, so we convert the values to floats for math
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Call the function and print the result
    result = add(num1, num2)
    print(f"The result of {num1} + {num2} is: {result}")
except ValueError:
    print("Invalid input. Please enter numbers only.")