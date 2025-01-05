import string

# Function to clean the input string by removing spaces and converting to lowercase
def clean_string(s):
    # Remove punctuation and spaces, and convert to lowercase
    s = s.lower()
    return ''.join(char for char in s if char in string.ascii_lowercase)

# Recursive function to check if a string is a palindrome
def is_palindrome(s):
    # Base case: an empty string or single character is a palindrome
    if len(s) <= 1:
        return True
    # Compare the first and last characters
    if s[0] == s[-1]:
        # Recursively check the substring excluding the first and last characters
        return is_palindrome(s[1:-1])
    else:
        return False

# Main program
def main():
    # Prompt the user for a string
    user_input = input("Enter a string to check if it's a palindrome: ")
    cleaned_string = clean_string(user_input)
    if is_palindrome(cleaned_string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

if __name__ == "__main__":
    main()
