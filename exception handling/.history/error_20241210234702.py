# Example of handling exceptions with try and except
try:
    # Attempt to convert input to an integer
    num = int(input("Enter a number: "))  # May raise ValueError
    result = 10 / num  # May raise ZeroDivisionError
except ZeroDivisionError:
    # Handle division by zero error
    print("Error: Division by zero is not allowed.")
except ValueError:
    # Handle invalid input error
    print("Error: Please enter a valid number.")



# Example of using the else block
try:
    # Attempt to perform the operations
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    # Handle division by zero
    print("Error: Division by zero.")
else:
    # This block runs only if no exceptions occur
    print("Success! The result is:", result)



