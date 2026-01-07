# Menu storing all products: code -> [name, price]
products = {
    "A1": ["Coke", 3.0],
    "A2": ["Pepsi", 3.0],
    "A3": ["Sprite", 3.0],
    "A4": ["Water", 1.0],
    "A5": ["Juice", 4.0],
    "A6": ["Iced Tea", 3.5],
    "A7": ["Coffee", 5.0],
    "A8": ["Strawberry Milk", 3.0],
    "A9": ["Mirinda Citrus", 2.5],
    "A10": ["Chocolate Milk", 2.5],
    "B1": ["Biscuits", 3.5],
    "B2": ["Cookies", 3.0],
    "B3": ["Skittles", 3.0],
    "B4": ["Mentos", 2.0],
    "B5": ["Sandwich", 10.0],
    "B6": ["Cheetos", 4.0],
    "B7": ["Granola Bar", 5.0],
    "B8": ["Doritos", 3.5],
    "B9": ["Ice Cream", 2.0],
    "B10": ["Bagel", 5.0]
}

# Suggestions: key item -> list of recommended product codes
suggestions = {
    "A7": ["B1"],       # Coffee -> suggest Biscuits
    "B2": ["A7"],       # Cookies -> suggest Coffee
    "A1": ["B6"],       # Coke -> suggest Cheetos
    "A3": ["B8"],       # Sprite -> suggest Doritos
    "A8": ["B6"]        # Strawberry Milk -> suggest Sandwich
}

# Display vending machine menu
print("---VENDING MACHINE MENU---")
for code, info in products.items():  # Loop through each product
    print(f"{code} - {info[0]} : {info[1]} SAR")  # Show code, name, price

# Initialize shopping cart and total price
total_price = 0
cart = []

# Loop for selecting products
while True:
    code = input("Enter product code: ").strip().upper()  # Get input and standardize it

    if code in products:  # Check if code exists
        item_name = products[code][0]  # Get product name
        item_price = products[code][1]  # Get product price

        cart.append(item_name)  # Add item to cart
        total_price += item_price  # Add price to total

        print(f"Added: {item_name} - {item_price} SAR")  # Confirm addition

        # Check for intelligent suggestion
        if code in suggestions:
            for suggested_code in suggestions[code]:
                suggested_item = products[suggested_code][0]
                suggested_price = products[suggested_code][1]
                print(f"Suggestion: You might also want to buy {suggested_item} ({suggested_price} SAR)!")

    else:
        print("Invalid product code. Try again.")  # Error for wrong code
        continue  # Go back to start of loop

    # Ask if user wants to buy another item
    again = input("Do you want to purchase another item? (yes/no): ").strip().lower()
    if again == "no":  # If no, exit the loop
        break

# Displays final cart and the total price of the items
print("Your cart:", cart)
print("Total amount:", total_price, "SAR")

# Payment process with loop for insufficient amount
while True:
    amount = float(input("Please enter the amount to the machine: "))  # Get money from user

    if amount >= total_price:
        change = amount - total_price  # Calculate change if overpaid
        print("Thank you for your purchase!")
        if change > 0:
            print("Your change is:", round(change, 2), "SAR")  # Return change
        break  # Exit loop when enough money is entered
    else:
        shortage = total_price - amount
        print("Insufficient amount! You are short by:", round(shortage, 2), "SAR")
        print("Please enter additional amount.")
