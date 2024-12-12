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
def add_product(name, quantity, price):
     item= [{"name": name, "quantity":quantity, "price":price}]
     inventory.append(item)
#define details of display_inventory
def display_inventory():
     for product in inventory:
        print(f"Name: {product['name']}, Quantity: {product['quantity']}, Price: {product['price']}")

display_inventory()


#test
add_product("Monitor", 2, 150)
display_inventory()
# print("Updated Inventory:", inventory)
          
     
     