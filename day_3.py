# Define the inventory list
inventory = []

# Add a product to the inventory
def add_product(name, quantity, price):
    for item in inventory:
        if item["name"].lower() == name.lower():
            print(f"Product '{name}' already exists in the inventory.")
            return
    inventory.append({"name": name, "quantity": quantity, "price": price})
    print(f"Product '{name}' added successfully.")

# Display the inventory
def display_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for product in inventory:
            print(f"Name: {product['name']}, Quantity: {product['quantity']}, Price: ${product['price']}")

# Update the quantity of a product
def update_quantity(product_name, new_quantity):
    for product in inventory:
        if product["name"].lower() == product_name.lower():
            product["quantity"] = new_quantity
            print(f"{product_name} quantity updated to {new_quantity}.")
            return
    print(f"{product_name} not found in inventory.")

# Search for a product
def search_product(product_name):
    for product in inventory:
        if product["name"].lower() == product_name.lower():
            print(f"Product found: {product}")
            return
    print(f"{product_name} not found in inventory.")

# Remove a product from the inventory
def remove_product(product_name):
    for product in inventory:
        if product["name"].lower() == product_name.lower():
            inventory.remove(product)
            print(f"Product '{product_name}' removed from inventory.")
            return
    print(f"{product_name} not found in inventory.")

# Sort the inventory by name or price
def sort_inventory(by="name"):
    if by == "name":
        sorted_inventory = sorted(inventory, key=lambda x: x["name"].lower())
    elif by == "price":
        sorted_inventory = sorted(inventory, key=lambda x: x["price"])
    else:
        print("Invalid sort criteria. Sorting by name by default.")
        sorted_inventory = sorted(inventory, key=lambda x: x["name"].lower())

    print("\nSorted Inventory:")
    for product in sorted_inventory:
        print(f"Name: {product['name']}, Quantity: {product['quantity']}, Price: ${product['price']}")

# Main menu
def main():
    while True:
        print("\nMenu:")
        print("1. Add Product")
        print("2. Update Quantity")
        print("3. Search Product")
        print("4. Remove Product")
        print("5. Display Inventory")
        print("6. Sort Inventory")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            quantity = int(input("Enter product quantity: "))
            price = float(input("Enter product price: "))
            add_product(name, quantity, price)
        elif choice == "2":
            name = input("Enter product name to update: ")
            quantity = int(input("Enter new quantity: "))
            update_quantity(name, quantity)
        elif choice == "3":
            name = input("Enter product name to search: ")
            search_product(name)
        elif choice == "4":
            name = input("Enter product name to remove: ")
            remove_product(name)
        elif choice == "5":
            display_inventory()
        elif choice == "6":
            by = input("Sort by 'name' or 'price': ").lower()
            sort_inventory(by)
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
