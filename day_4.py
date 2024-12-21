#object oriented programming
class User:
     def __init__(self, name, color):
          self.name = name
          self.color = color
     def greet(self):
          print(f"Hi my name is {self.name}")  
     def shower(self):
          print(f"Hi, this is {self.name} and I'm jusmping in the shower!")  
     def towel_color(self):
          print(f"this is {self.name} and I'm about to jump in the shower. Don't worry, I have my own towel, it's the {self.color} one. ")        
me = User('Paul','green')
me.greet() 
me.shower()  
me.towel_color()        
leah = User("Leah", "Rust")  
leah.towel_color()