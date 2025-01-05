import re

# Function to validate the date format
def validate_date(date):
    # Regular expression for validating the date in format DD-MM-YYYY
    pattern = r"^([0-2]?[0-9]|3[01])-([0]?[1-9]|1[0-2])-(\d{4})$"
    
    # Match the pattern with the input date
    if re.match(pattern, date):
        return "Valid"
    else:
        return "Invalid"

# Input from the user
user_input = input("Enter a date in the format DD-MM-YYYY: ")

# Validate and print the result
print(validate_date(user_input))
