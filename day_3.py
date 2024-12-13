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
#           display_inventory()
# # update products
# # search for products
# # remove prosuctrs

# print('hi')