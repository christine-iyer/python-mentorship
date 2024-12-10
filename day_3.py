# add product
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
# update products
# search for products
# remove prosuctrs

