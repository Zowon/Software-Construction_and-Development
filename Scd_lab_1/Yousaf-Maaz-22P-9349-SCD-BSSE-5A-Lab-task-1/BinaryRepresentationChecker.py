# Function to check if a number is even or odd using bitwise operations
def check_even_odd(number):
    # Perform bitwise AND with 1
    if number & 1 == 0:
        return "even"
    else:
        return "odd"

# Main program
def main():
    # Prompt the user for a number
    try:
        user_input = int(input("Enter a number: "))
        result = check_even_odd(user_input)
        print(f"The number {user_input} is {result}.")
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()
    