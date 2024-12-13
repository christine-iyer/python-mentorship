# Create an inventory management system.

#create inventory distionary
inventory=[]
#define add_product function. The product has 3 properties: name, quantity, price
def add_product(name, quantity, price):
     pass
#define show_inventory function.
def display_inventory():
     pass
#define details of add_product function
# Define the inventory list
inventory = []

def add_product(name, quantity, price):
    # Check if the product already exists in the inventory
    for item in inventory:
        if item["name"] == name:
            print(f"Product '{name}' already exists in the inventory.")
            return  # Exit the function without adding the duplicate product

    # Add the new product if it doesn't exist
    new_item = {"name": name, "quantity": quantity, "price": price}
    inventory.append(new_item)
    print(f"Product '{name}' added successfully.")
    


# Example usage
add_product("Apple", 10, 0.5)
add_product("Banana", 20, 0.3)
add_product("Apple", 5, 0.4)  # This will not be added
     
#define details of display_inventory
def display_inventory():
     for product in inventory:
        print(f"Name: {product['name']}, Quantity: {product['quantity']}, Price: {product['price']}")

def display_inventory():
    for product in inventory:
        print(f"Name: {product['name']}, Quantity: {product['quantity']}, Price: ${product['price']}")

# display_inventory()



#test
add_product("Monitor", 2, 150)
add_product("Camera", 1, 350)

print("Updated Inventory:", inventory)
          
     
     