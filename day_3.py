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

add_product("Monitor", 2, 150)
add_product("Camera", 1, 350)

          
     
     
#function warm up
def add_numbers(x,y):
     sum = x+y
     print(sum)
     return sum
my_sum = add_numbers
my_sum(7,8) 

#same function with an unlimited number of args
def add_numbers(*args):
     total=sum(args)
     print(total)
     return total

my_sum = add_numbers
my_sum(5,4,3,7, 55)   

# looping and scoping
colors=["red","blue","green", "yellow", "orange"]
for color in colors:
     print(f"The color is {color}")
print("outside", color) 
 
     
     
inventory=[]
def add_product(name, quantity, price):
     product={"name":name, "quantity":quantity, "price":price}
     inventory.append(product)
     
add_product("Monitor", 2, 375)
add_product("Keyboard", 6, 80)   
print("Here's the Updated Onventory", inventory)  
# display inventory
def display_inventory(inventory):
     for product in inventory:
          print(f"Name: {product['name']}, Quantity: {product['quantity']}, Price: ${product['price']}")
          display_inventory()
# # update product
def update_quantity(product_name, new_quantity):
    for product in inventory:
        if product["name"].lower() == product_name.lower():
            product["quantity"] = new_quantity
            print(f"{product_name} quantity updated to {new_quantity}.")
            return
    print(f"{product_name} not found in inventory.")
    
# Test the function
update_quantity("monitor", 7)
update_quantity("keyboard", 7)
add_product("printer", 37, 97)
print("Updated Inventory:", inventory)     

# # search for products
def search_product(product_name):
     for product in inventory:
          if product['name'].lower()==product_name.lower():
               print(f"{product_name} found")
               return
     print(f"{product_name} not dound")
     
update_quantity("keyboard", 13) 
search_product("monitor")    
          
# # remove prosuctrs

def remove_product(product_name):
     for product in inventory:
          if product['name'].lower()== product_name.lower():
               inventory.remove(product)
               print(f"{product_name} removed")
               return   
     print(f"{product_name} not found in the inventory")   
remove_product("monitor")
print("Updated Inventory:", inventory) 
                  

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(f"{prompt}: Invalid input. Sorry error.")  # Using f-string for variable substitution.


def sort_inventory(by="name"):
    if by == "name":
        sorted_inventory = sorted(inventory, key=lambda x: x["name"])
    elif by == "price":
        sorted_inventory = sorted(inventory, key=lambda x: x["price"])
    else:
        print("Invalid sort criteria. Sorting by name by default.")
        sorted_inventory = sorted(inventory, key=lambda x: x["name"])

    for product in sorted_inventory:
        print(f"Name: {product['name']}, Quantity: {product['quantity']}, Price: ${product['price']}")

def main():
    while True:
        print("\nMenu:")
        print("1. Add Product")
        print("2. Update Quantity")
        print("3. Search Product")
        print("4. Remove Product")
        print("5. Display Inventory")
        print("6. Exit")

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
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()