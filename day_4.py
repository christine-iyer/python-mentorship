#object oriented programming
# class User:
#      def __init__(self, name, color):
#           self.name = name
#           self.color = color
#      def greet(self):
#           print(f"Hi my name is {self.name}")  
#      def shower(self):
#           print(f"Hi, this is {self.name} and I'm jusmping in the shower!")  
#      def towel_color(self):
#           print(f"this is {self.name} and I'm about to jump in the shower. Don't worry, I have my own towel, it's the {self.color} one. ")        
# me = User('Paul','green')
# me.greet() 
# me.shower()  
# me.towel_color()        
# leah = User("Leah", "Rust")  
# leah.towel_color()

# Make a bank account
class Account:
     def __init__(self, account_type,balance,overdraft_fees=0) :
          self.account_type = account_type
          self.balance = balance
          self.overdraft_fees = overdraft_fees
        
      
     def deposit(self, amount):
          if amount > 0:
                self.balance +=amount
                print(f"you deposited ${amount}. New balance = ${self.balance}")
          else:
               print(f"Amount must be positive") 
          return self.balance     

           
     def withdraw(self,amount):
          if amount > self.balance:
               print(f"you don't have a high enough balance to make the withdrwel")
               self.overdraft_fees += 35
               self.balance -= amount + 35
          else:
               self.balance -= amount
               print(f"You have ${self.balance} after withdrawing ${amount}")     
               return self.balance
 
     def get_balance(self):
          return(self.balance)  
     
     def get_overdraft_fees(self):
        return self.overdraft_fees
 

account = Account("Checking", 500)

# Testing deposit
account.deposit(1200)

# Testing withdrawal with sufficient funds
account.withdraw(100)

# Testing withdrawal with insufficient funds
account.withdraw(700)

# Checking balance and overdraft fees
print("Final balance:", account.get_balance())
print("Total overdraft fees:", account.get_overdraft_fees())

          
          
           
                