import re

# Function to validate Pakistani phone number format
def validate_phone_number(phone_number):
    # Regular expression to match the phone number
    pattern = r"^\+92[-\s]?3\d{2}[-\s]?\d{7}$"
    
    # Match the pattern with the input phone number
    if re.match(pattern, phone_number):
        return "Valid"
    else:
        return "Invalid"

# Input from the user
user_input = input("Enter a Pakistani phone number in the format +92 300 1234567: ")

# Validate and print the result
print(validate_phone_number(user_input))
