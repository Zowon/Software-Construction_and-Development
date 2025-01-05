import re

# Regular expression pattern for strong password validation using \W for special characters
password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*\W)[A-Za-z\d\W]{8,}$"

def validate_password(password):
    # Check if the password matches the pattern
    if re.match(password_pattern, password):
        return "Valid"
    else:
        return "Invalid"

# Display instructions for the user
print("Please enter a password that meets the following criteria:")
print("1. At least 8 characters long.")
print("2. Contains at least one uppercase letter (A-Z).")
print("3. Contains at least one lowercase letter (a-z).")
print("4. Contains at least one number (0-9).")
print("5. Contains at least one special character (e.g., !, @, #, $, %, etc.).")

# Ask the user for a password input
user_input = input("\nEnter your password: ")

# Validate the user input and print the result
result = validate_password(user_input)
print(f"Input: {user_input} \n Output: {result}")
