import re
from datetime import datetime

# Regular expression pattern for basic DD/MM/YYYY format validation
date_pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(1[0-9]{3}|20[0-9]{2})$"

def is_leap_year(year):
    # Check if the year is a leap year
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def validate_advanced_date(day, month, year):
    # Check for months with 30 days
    if month in [4, 6, 9, 11] and day > 30:
        return False
    # Check for February (leap year vs non-leap year)
    elif month == 2:
        if is_leap_year(year):
            return day <= 29
        else:
            return day <= 28
    return True

def validate_date(date):
    # First, validate the basic format using regex
    match = re.match(date_pattern, date)
    if match:
        day, month, year = map(int, date.split('/'))
        # Check if the day is valid for the given month and year
        if validate_advanced_date(day, month, year):
            return "Valid"
        else:
            return "Invalid (Day is not valid for the given month/year)"
    else:
        return "Invalid (Incorrect format)"

# Ask the user for a date input
user_input = input("Please enter a date in the format DD/MM/YYYY: ")

# Validate the user input and print the result
result = validate_date(user_input)
print(f"Input: {user_input} \n  Output: {result}")
