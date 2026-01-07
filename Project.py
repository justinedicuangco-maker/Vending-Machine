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

# Stock system code where all products consist of 10 stocks
stock = {code: 10 for code in products}

# Suggestions for all products for a good experience to the customer
suggestions = {
    "A1": ["B6"], "A2": ["B3"], "A3": ["B8"], "A4": ["B7"],
    "A5": ["B5"], "A6": ["B2"], "A7": ["B1"], "A8": ["B5"],
    "A9": ["B4"], "A10": ["B9"], "B1": ["A7"], "B2": ["A7"],
    "B3": ["A1"], "B4": ["A9"], "B5": ["A4"], "B6": ["A1"],
    "B7": ["A6"], "B8": ["A3"], "B9": ["A10"], "B10": ["A7"]
}

# Display menu
print("--- VENDING MACHINE MENU ---")
for code, info in products.items():
    print(f"{code} - {info[0]} : {info[1]} SAR (Stock: {stock[code]})")

cart = []
total_price = 0

# Product selection loop
while True:
    code = input("Enter product code: ").strip().upper()

    if code not in products:
        print("Invalid product code. Try again.")
        continue

    if stock[code] == 0:
        print("Sorry, this item is out of stock.")
        choice = input("Do you want to choose another item? (yes/no): ").strip().lower()
        if choice == "yes":
            continue
        else:
            break

    # This lets the user buy more than 1 of the selected product
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be greater than 0.")
            elif quantity > stock[code]:
                print("Not enough stock available.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    item_name, item_price = products[code]
    cart.append(f"{item_name} x{quantity}")
    total_price += item_price * quantity
    stock[code] -= quantity

    print(f"Added {quantity} {item_name}(s)")

    # Shows suggestion
    suggested_code = suggestions[code][0]
    if stock[suggested_code] > 0:
        suggested_item, suggested_price = products[suggested_code]
        print(f"Suggestion: You might also like {suggested_item} ({suggested_price} SAR)")

    again = input("Buy another item? (yes/no): ").strip().lower()
    if again == "no":
        break

# Shows the item in your cart and the total amount of it
print("Your cart:", cart)
print("Total amount:", total_price, "SAR")

while True:
    try:
        amount = float(input("Insert money: "))
        if amount >= total_price:
            change = round(amount - total_price, 2)
            print("Thank you for your purchase!")
            if change > 0:
                print("Your change is:", change, "SAR")
            break
        else:
            print("Insufficient amount. Please add more money.")
    except ValueError:
        print("Please enter a valid number.")