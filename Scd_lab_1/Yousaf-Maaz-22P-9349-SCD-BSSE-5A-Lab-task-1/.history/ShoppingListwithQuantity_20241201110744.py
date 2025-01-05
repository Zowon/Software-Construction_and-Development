# Function to add or update items in the shopping list
def update_shopping_list(shopping_list, item, quantity):
    if item in shopping_list:
        shopping_list[item] += quantity
    else:
        shopping_list[item] = quantity

# Main program
def main():
    shopping_list = {}
    
    while True:
        # Get user input
        item = input("Enter the item (or type 'done' to finish): ").strip()
        if item.lower() == 'done':
            break
        
        try:
            quantity = int(input(f"Enter the quantity for {item}: "))
            update_shopping_list(shopping_list, item, quantity)
        except ValueError:
            print("Invalid quantity! Please enter a number.")
    
    # Display the final list
    print("\nShopping List:")
    for item, quantity in shopping_list.items():
        print(f"{item}: {quantity}")

if __name__ == "__main__":
    main()

def leapyear(year): year
    date = datetime.datetime.