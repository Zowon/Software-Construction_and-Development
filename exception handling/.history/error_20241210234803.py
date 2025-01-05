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




# Example of the finally block
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Division by zero.")
finally:
    # Always executes, regardless of exceptions
    print("This block always executes.")


# Example of exception chaining
try:
    # Attempting to convert an invalid string to an integer
    num = int("invalid")
except ValueError as ve:
    # Raise a new exception while keeping the original
    raise RuntimeError("Conversion failed") from ve


# Example of rethrowing exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    # Handle the exception partially
    print("Handling ZeroDivisionError")
    # Rethrow the exception to be handled elsewhere
    raise



# Define a custom exception for invalid age
class InvalidAgeError(Exception):
    """Exception raised when an invalid age is provided."""
    def __init__(self, age, message="Age must be between 0 and 120"):
        self.age = age
        self.message = message
        super().__init__(self.message)

# Example usage of custom exception
try:
    age = 150
    if age < 0 or age > 120:
        # Raise the custom exception if age is invalid
        raise InvalidAgeError(age, "Age is not valid")
    else:
        print("Valid age:", age)
except InvalidAgeError as e:
    # Catch and handle the custom exception
    print(f"Error: {e.message}. You provided: {e.age}")


# Example of using assert for debugging
def divide(a, b):
    # Ensure the divisor is not zero
    assert b != 0, "Division by zero is not allowed"
    return a / b

# Call the function with valid inputs
print(divide(10, 2))


# Example of using a context manager to handle files
try:
    # Open a file and read its contents
    with open("file.txt", "r") as f:
        data = f.read()  # No need for explicit close
except FileNotFoundError:
    # Handle file not found error
    print("File not found.")




# Example of logging exceptions
import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.ERROR)

try:
    result = 10 / 0
except ZeroDivisionError as e:
    # Log the exception with traceback
    logging.error(f"Exception occurred: {e}", exc_info=True)





# Example of handling multiple exceptions in one block
try:
    # Attempt operations that may raise ValueError or ZeroDivisionError
    num = int(input("Enter a number: "))
    result = 10 / num
except (ValueError, ZeroDivisionError) as e:
    # Handle both exceptions similarly
    print(f"Error: {e}")
